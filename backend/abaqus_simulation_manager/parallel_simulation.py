import os
import psutil
import logging
import requests
import traceback
import threading
import subprocess
import concurrent.futures
from zoneinfo import ZoneInfo
from datetime import datetime
from PySide6.QtCore import QTimer
from typing import List, Tuple, Optional
import time
from backend.abaqus_results_extractor.results_manager import SimulationResultHandler


class ParallelSimulation():
    """
    Handles the parallel execution of Abaqus simulations, including job reservation,
    command preparation, execution, and result extraction.
    """
    def __init__(self, main, cores_per_simulation: int, computer_id: str):
        """
        Initializes the simulation manager.

        Args:
            main: Main application context with Supabase and UI access.
            cores_per_simulation: Number of CPU cores allocated per simulation.
            computer_id: Identifier for the current computer (e.g., 'cp01').
        """
        self.main = main
        self.cores_per_simulation = cores_per_simulation
        self.computer_id = computer_id
        self.is_running = False
    
    
    def run_all_simulations(self) -> None:
        """
        Starts the simulation process and schedules periodic status updates.
        """
        # Schedule status updates every 20 minutes
        self._schedule(lambda: self._update_status_and_timestamp(), 1200)

        # Run initial check
        self._check_and_run_simulations()

        if self.computer_id != "cp01":
            logging.info("⏱️ Starting periodic simulation timer...")
            self._schedule(lambda: self._check_and_run_simulations(), 1200)


    def _check_and_run_simulations(self) -> None:
        """
        Checks for pending simulations and executes them if available.
        """
        if self.is_running:
            logging.info("⏳ Already running. Waiting for the next check.")            
            return
        
    
        if self._has_pending_simulations():
            logging.info("🟢 Pending simulations found.")
            self.is_running = True
            self._execute_simulation_batch()
            
        else:
            self.is_running = False
            logging.info("⚪ No simulations available to run.")


    def _has_pending_simulations(self) -> bool:
        """
        Checks if there are any pending simulation jobs.

        Returns:
            bool: True if pending jobs exist, False otherwise.
        """
        response = self.main.supabase.table("simulation_commands").select("id").eq("project_id", self.main.project_id).eq("status", 'false').limit(1).execute()
        return bool(response.data)


    def _execute_simulation_batch(self) -> None:
        """
        Executes a batch of simulations based on available system resources.
        """
        jobs_to_run = self._calculate_parallel_jobs()
        reserved_paths  = self._reserve_jobs(jobs_to_run)
        commands = self._prepare_simulation_commands(reserved_paths)
        self._run_simulations_concurrently(commands, jobs_to_run)
        self._extract_simulation_results(commands)
        self.is_running = False
        self._check_and_run_simulations() # Re-check for remaining jobs
    

    def _calculate_parallel_jobs(self) -> int:
        """
        Determines how many simulations can run in parallel based on CPU usage.

        Returns:
            int: Number of parallel jobs (minimum 3).
        """
        threshold = 10  # max %CPU usage per core considered free
        usages = psutil.cpu_percent(interval=1, percpu=True)
        physical_cores = psutil.cpu_count(logical=False)
        available = sum(1 for i, usage in enumerate(usages) if usage < threshold and i < physical_cores)
        jobs = (available - 2) // self.cores_per_simulation
        return min(max(jobs, 2), 3)


    def _reserve_jobs(self, num_files) -> List[str]:
        """
        Reserves simulation jobs for execution.

        Args:
            num_jobs: Number of jobs to reserve.

        Returns:
            List[str]: List of input file URLs.
        """
        jobs = self.main.supabase.table("simulation_commands")\
            .select("*")\
            .eq("project_id", self.main.project_id)\
            .eq("status", "false")\
            .execute().data[:num_files]

        reserved_paths = []
        for job in jobs:
            updated = self.main.supabase.table("simulation_commands")\
                .update({"status": "running","computer_id": self.computer_id})\
                .eq("id", job["id"])\
                .eq("status", "false")\
                .execute()
            
            if updated.data:
                reserved_paths.append(job["command"])
        return reserved_paths


    def _prepare_simulation_commands(self, input_urls) -> List[Tuple[str, str]]:
        """
        Downloads input files and prepares Abaqus command strings.

        Args:
            input_urls: List of input file URLs.

        Returns:
            List[Tuple[str, str]]: List of (directory, command) tuples.
        """
        simulation_dirs = []
        for url in input_urls:
            filename = os.path.splitext(os.path.basename(url.split("?")[0]))[0]

            dir_path  = os.path.join(self.main.simulation_folder, filename)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            simulation_dirs.append(dir_path)

            self._prepare_directory(url, dir_path, filename)

        # Build command list
        commands = []
        for folder in simulation_dirs:
            if os.path.isdir(folder):
                for file in os.listdir(folder):         
                    source_path = os.path.join(folder, file)                  
                    if file.endswith('.inp'):
                        inp_dir = os.path.dirname(source_path)
                        job_name = os.path.basename(source_path).replace(".inp", "")
                        command = rf'call {self.main.abaqus_path} job={job_name} input={job_name} cpus={self.cores_per_simulation} interactive'
                        commands.append((inp_dir, command))
        return commands


    def _prepare_directory(self, url, dir_path, filename):
        """
        Downloads the input file and supporting files into the specified simulation directory.

        This method retrieves the `.inp` file from the provided URL and stores it locally.
        It also downloads a predefined set of auxiliary files required for Abaqus simulations
        from Supabase storage and saves them in the same directory.

        Args:
            url (str): Public URL of the `.inp` file.
            dir_path (str): Local directory path where files will be stored.
            filename (str): Base name used to save the `.inp` file.
        """
        # Download .inp file
        inp_response = requests.get(url.split("?")[0])
        if inp_response.status_code == 200:
            inp_path = os.path.join(dir_path, f"{filename}.inp")
            with open(inp_path, "wb") as f:
                f.write(inp_response.content)
                
        # Download default files
        source_path_list = ["abaqus_v6.env", "explicitU-D.dll", "explicitU.dll"]
        bucket_name = "inp-default-files"

        for file in source_path_list:
            storage_path = f"subrotine/{file}"
            file_url = self.main.supabase_storage.storage.from_(bucket_name).get_public_url(storage_path)
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(os.path.join(dir_path, file), "wb") as f:
                    f.write(response.content)
            else:
                logging.error(f"❌ Failed to download: {file_url}")


    def _run_simulations_concurrently(self, commands, num_file) -> None:
        """
        Executes simulations concurrently using threads.

        Args:
            commands: List of (directory, command) tuples.
            max_workers: Number of concurrent threads.
        """
        def aux_run_simulations(inp_dir, command) -> Optional[str]:
            retries = 3
            job_name = command.split('job=')[1].split()[0]
            output_file = os.path.join(inp_dir, f"{job_name}.odb")
            
            for attempt in range(1, retries + 1):
                try:
                    print(f"▶️  Running: {command}")
                    logging.info(f"▶️ Attempt {attempt}: Executing command: {command}")
                    os.chdir(inp_dir)
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    process.wait()
                    time.sleep(15)

                    if os.path.exists(output_file):
                        print(f"✅ Found output file: {output_file}")
                        return
                    else:
                        logging.warning(f"⚠️ Output file not found for job '{job_name}'. Retrying...")
                except Exception as e:
                    logging.error(f"❌ Failed to execute: {command}. Error: {str(e)}")
                    logging.debug("🔍 Traceback:\n%s", traceback.format_exc())
                    return f"Failed: {command}. Error: {str(e)}"
                            
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_file) as executor:
            futures = {executor.submit(aux_run_simulations, inp_dir, command): command for inp_dir, command in commands}
            for future in concurrent.futures.as_completed(futures):
                command = futures[future]
                try:                 
                    future.result()
                except Exception as e:
                    logging.error("❌ Error during parallel execution: %s", str(e))
                    logging.debug("🔍 Traceback:\n%s", traceback.format_exc())

        for inp_dir, command in commands:
            job_name = command.split('job=')[1].split()[0]
            odb_path = os.path.join(inp_dir, f"{job_name}.odb")

            # print("odb_path:", odb_path)
            # print("odb_path:", os.path.getsize(odb_path))
            while not os.path.exists(odb_path) or os.path.getsize(odb_path) < 450000 * 1024:
                print(f"⏳ Waiting for {job_name}.odb ({os.path.getsize(odb_path)/1024:.1f} KB)" if os.path.exists(odb_path) else f"⏳ Waiting for {job_name}.odb (not yet created)")
                time.sleep(600)


    def _extract_simulation_results(self, commands) -> None:
        """
        Extracts results from completed simulations and marks them as finished.

        Args:
            commands: List of (directory, command) tuples.
        """
        result_extractor = SimulationResultHandler(self.main)

        try:
            for inp_dir, command in commands:
                job_name = command.split('job=')[1].split()[0]
                # print(f"🔧 Job name: {job_name}")

                output_file = os.path.join(inp_dir, f"{job_name}.odb")
                result_extractor.run_result_call(output_file)  

                time.sleep(30)

                parts = job_name.split('_')
                condition = parts[1]  # cond01
                iteration_number = int(parts[3])  # 1
                set_number = int(parts[5])  # 1
                existing = self.main.supabase.table("results").select("*")\
                .eq("project_id", self.main.project_id)\
                .eq("iteration_number", iteration_number)\
                .eq("parameter_set", set_number)\
                .eq("condition_name", condition)\
                .execute()

                result_row = existing.data[0] if existing.data else None
                erro = result_row.get("error") if result_row else None

                if not erro:
                    print("📤 Attempting result extraction for job '%s'", job_name)
                    logging.info("📤 Attempting result extraction for job '%s'", job_name)
                    result_extractor.run_result_call(output_file)
                    self._mark_jobs_as_completed(job_name)
                else:
                    logging.info("✅ Job '%s' already has error recorded, skipping extraction", job_name)
                    print("✅ Job '%s' already has error recorded, skipping extraction", job_name)
                    self._mark_jobs_as_completed(job_name)

        except Exception as e:
            logging.error("❌ Error in SimulationResultHandler: %s", str(e))
            logging.debug("🔍 Traceback:\n%s", traceback.format_exc())
            raise


    def _mark_jobs_as_completed(self, job_name: str) -> None:
        """
        Marks a simulation command as completed in the DB.

        Args:
            job_name (str): Name of the job that finished.
        """
        response = self.main.supabase.table("simulation_commands").update({"status": "True"}).eq("project_id", self.main.project_id).like("command", f"%{job_name}%").eq("status", "running").execute()
        if response.data:
            logging.info(f"✅ Job '{job_name}' marked as completed.")
        else:
            logging.warning(f"⚠️ Job '{job_name}' not found or already marked as completed.")

    
    def _update_status_and_timestamp(self) -> None:
        """
        Updates the status and timestamp of the current computer in the database.

        This method sets the computer's status to active and records the current time
        (in the Berlin timezone) as the last update. It ensures that the system knows
        this computer is still participating in the simulation process.

        The update is applied to the 'computers' table for the current project and computer ID.
        """
        now = datetime.now(ZoneInfo("Europe/Berlin")).isoformat()
        self.main.supabase.table("computers").update({"status": True,"last_update": now}).eq("project_id", self.main.project_id).eq("computer_id", self.main.pc_id).execute()


    @staticmethod
    def _schedule(func: callable, interval_seconds: int) -> None:
        """
        Schedules a function to run periodically in a background daemon thread.

        This method uses Python's threading and Timer to repeatedly execute the given
        function at fixed intervals (in seconds). It is useful for tasks like status
        updates or health checks that need to run continuously without blocking the main thread.

        Args:
            func (callable): The function to be executed periodically.
            interval_seconds (int): The interval between executions, in seconds.
        """
        def wrapper():
            func()
            threading.Timer(interval_seconds, wrapper).start()
        threading.Thread(target=wrapper, daemon=True).start()

