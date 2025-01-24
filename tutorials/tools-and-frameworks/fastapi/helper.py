import subprocess
import os

def run_fastapi(port):
    """
    This function runs the FastAPI server in a subprocess.

    Parameters:
    port (int): The port to run the FastAPI server on.

    Returns:
    subprocess.Popen: The FastAPI process
    """
    # Command to activate the virtual environment and run the FastAPI server
    command = f"source fastapi-env/bin/activate && uvicorn main:app --reload --port {port}"
    
    # Run the command in the shell with Popen
    fastapi_process = subprocess.Popen(command, shell=True, executable="/bin/bash", preexec_fn=os.setsid)

    return fastapi_process


def clean_tutorial():
    """
    This function cleans up the artifacts created during the tutorial.
    """
    # Activate the environment, uninstall the kernel, list kernels, and remove main.py
    commands = [
        "rm -f main.py"
    ]
    
    for command in commands:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"Command: {command}")
        print(f"Return Code: {process.returncode}")
        if process.stdout:
            print(f"Output:\n{process.stdout}")
        if process.stderr:
            print(f"Error:\n{process.stderr}")
        print("-" * 40)

def kernel_validation():
    user_input = input("Is the notebook running in `SilverAIWolf (FastAPI)? Type `yes` to continue: ")

    if user_input.lower() != "yes":
        msg = "The notebook must be running with `SilverAIWolf (FastAPI)` environment."
        raise Exception(msg)
        
    