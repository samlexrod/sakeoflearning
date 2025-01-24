import subprocess
import os

def run_fastapi(port):
    """
    """
    # Command to activate the virtual environment and run the FastAPI server
    command = f"source fastapi-env/bin/activate && uvicorn main:app --reload --port {port}"
    
    # Run the command in the shell with Popen
    fastapi_process = subprocess.Popen(command, shell=True, executable="/bin/bash", preexec_fn=os.setsid)


def clean_tutorial():
    """
    """
    # Activate the environment, uninstall the kernel, list kernels, and remove main.py
    commands = [
        "source fastapi-env/bin/activate && jupyter kernelspec uninstall -y fastapi-env",
        "jupyter kernelspec list",
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