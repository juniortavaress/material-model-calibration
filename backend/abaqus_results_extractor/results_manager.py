# -*- coding: utf-8 -*-
import os
import sys
import logging
import traceback
import subprocess
from typing import Tuple, Optional
from PySide6.QtCore import QMetaObject, Qt, Q_ARG
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.dont_write_bytecode = True

from backend.abaqus_results_extractor.convert_datas_to_excel.process_chip import ChipProcessor
from backend.abaqus_results_extractor.convert_datas_to_excel.process_forces import ForceProcessor
from backend.abaqus_results_extractor.convert_datas_to_excel.results_processor import ResultsManager



class SimulationResultHandler:
    """
    Handles the complete workflow of extracting, processing, and storing simulation results,
    including force and chip geometry data.
    """
    def __init__(self, main):
        self.main = main
        import platform
        self.debug_file = os.path.join(os.getcwd(), f"{platform.node()}_debug_steps.txt")


    def _log_debug(self, message: str):
        """Writes debug messages to a local TXT file."""

        with open(self.debug_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")
        print(message)  # opcional, mostra no console também


    def run_result_call(self, odb_file: str) -> Tuple[Optional[dict], Optional[dict]]:
        """
        Executes the full result extraction and processing pipeline.

        Args:
            odb_file (str): Path to the Abaqus output database file.

        Returns:
            Tuple[Optional[dict], Optional[dict]]: Processed force and chip summaries.
        """
        log = os.path.join(self.main.log_files, os.path.splitext(os.path.basename(odb_file))[0])
        if not os.path.exists(log):
            os.makedirs(log)

        os.environ.update({
            "OBJ_DIRECTORY": self.main.obj_path,
            "JSON_DIRECTORY": self.main.json_default_path,
            "ODB_FILE": str(odb_file),
            "LOG_DIRECTORY": log
        })      

        self._log_debug("\n\n\n--- STEP 01 ---")
        print("Extraindo info do: ", odb_file)
        self._run_abaqus_scripts(odb_file)
        self._log_debug("\n\n\n--- STEP 02 ---")
        self._clean_directory()
        self._log_debug("\n\n\n--- STEP 03 ---")
        self._process_simulation_outputs(odb_file)
        self._log_debug("\n\n\n--- STEP FINAL ---")
        

    def _run_abaqus_scripts(self, odb_file) -> None:
        """
        Runs Abaqus scripts in parallel to extract simulation data.

        Args:
            odb_file (str): Path to the Abaqus output database file.
        """
        try:
            commands = []
            if self.main.forces:
                script_path = os.path.join(self.main.scripts_path, "get_forces.py")
                abaqus_command_forces = rf'{self.main.abaqus_path} python {script_path} {self.main.json_default_path} {odb_file}'
                commands.append(abaqus_command_forces)

            if self.main.chip:
                script_path = os.path.join(self.main.scripts_path, "get_chip_obj_file.py")
                abaqus_command_chip_obj = rf'{self.main.abaqus_path} cae script={script_path}'
                commands.append(abaqus_command_chip_obj)
            
            def run_command(command: str) -> bool:
                """Executes a shell command and returns True if an error occurred."""
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    return "Error" in result.stdout or "Error" in result.stderr
                except subprocess.CalledProcessError:
                    return True

            self.main.error_tracking = False
            with ThreadPoolExecutor(max_workers=len(commands)) as executor:
                futures = {executor.submit(run_command, cmd): cmd for cmd in commands}
                for future in as_completed(futures):
                    if future.result():
                        self.main.error_tracking = True

        except Exception as e:
            print("❌ Error in SimulationResultHandler:", e)
            traceback.print_exc()
            logging.error("❌ Error in SimulationResultHandler: %s", str(e))
            logging.error("🔍 Traceback:\n%s", traceback.format_exc())
            raise


    def _process_simulation_outputs(self, odb_file) -> Tuple[Optional[dict], Optional[dict], Optional[dict]]:
        """
        Processes extracted simulation data and stores results.

        Args:
            odb_file (str): Path to the Abaqus output database file.

        Returns:
            Tuple[Optional[dict], Optional[dict]]: Force and chip summaries.
        """

        self._log_debug("--- Starting _process_simulation_outputs ---")
        self._log_debug(f"ODB: {odb_file}")

        try:
            forces_summary, chip_summary = None, None
            processor01 = ForceProcessor(self.main)
            processor03 = ChipProcessor(self.main)

            # iteration_tag = f"it_{str(self.main.current_opt).zfill(2)}"
            # self._log_debug(f"Iteration tag: {iteration_tag}")
            
            # if iteration_tag in odb_file:
            base_name = os.path.splitext(os.path.basename(odb_file))[0]
            if self.main.forces:
                self._log_debug("Processing forces...")
                forces_summary = processor01.process_file(base_name, exp_width = 4.0, sim_width = 0.02, start_pct = 0.25, end_pct = 1.00)
            if self.main.chip:
                self._log_debug("Processing chip geometry...")
                chip_summary = processor03.process_file(base_name)
            self._log_debug("Calling ResultsManager.store_simulation_results...")
            ResultsManager.store_simulation_results(self, base_name, forces_summary, chip_summary)
        
        except Exception as e:
            print("❌ Error in SimulationResultHandler22:", e)
            err = f"❌ Error in _process_simulation_outputs: {e}\n{traceback.format_exc()}"
            self._log_debug(err)
            traceback.print_exc()
            logging.error("❌ Error in SimulationResultHandler22: %s", str(e))
            logging.error("🔍 Traceback:\n%s", traceback.format_exc())
            raise

    @staticmethod
    def _clean_directory() -> None:
        """
        Deletes temporary files from the working directory based on keywords.
        """
        key_words_to_delete = ["acis", "rpy", "pyc"]
        for file_name in os.listdir(os.getcwd()):
            file_path = os.path.join(os.getcwd(), file_name)
            if os.path.isfile(file_path) and any(keyword in file_name for keyword in key_words_to_delete):
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass