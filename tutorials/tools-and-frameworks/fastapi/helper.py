import subprocess
import os

def run_fastapi(port):
    # Command to activate the virtual environment and run the FastAPI server
    command = f"source fastapi-env/bin/activate && uvicorn main:app --reload --port {port}"
    
    # Run the command in the shell with Popen
    fastapi_process = subprocess.Popen(command, shell=True, executable="/bin/bash", preexec_fn=os.setsid)