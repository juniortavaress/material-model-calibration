**Material Model Calibration** is a Python-based application designed for the inverse calibration of material models (e.g., Inconel 718) using Finite Element Analysis (FEA) simulations in Abaqus. The system automates the entire optimization cycle by orchestrating distributed execution across multiple computers and utilizing algorithms such as Particle Swarm Optimization (PSO) to identify the parameters that best describe real material behavior based on experimental data.

---

## Key Features
* **Project Management:** Centralized organization of parameters, cutting conditions, and material data.
* **Abaqus Automation:** Automatic editing of `.inp` files to systematically vary parameter sets.
* **Cloud Sync:** Integration with **Supabase Storage** for uploading and downloading original and modified simulation files.
* **Distributed Execution:** Parallel simulation orchestration across multiple computers using a database-driven command system.
* **Intelligent Optimization:** Built-in PSO algorithm to minimize the error between experimental results and simulation outputs.

---

## Project Structure

material-model-calibration/
│
├── frontend/                     # Graphical User Interface (PySide6)
│   ├── aux_files/                # UI callbacks and helper functions
│   └── interface/                # UI layout and design files
├── backend/                      # Simulation logic and .inp manipulation
│   ├── abaqus_results_extractor/ # Data extraction from simulation outputs
│   ├── abaqus_simulation_manager/# Manager for job queues and execution
│   ├── config/                   # System and configurations
│   └── optimization/             # PSO and objective function implementations
├── requirements.txt              # Python dependencies
├── main.py                       # Application entry point
└── README.md                     # Project documentation

---

## Install dependencies

pip install -r requirements.txt



