import time
import pytest
import subprocess
import os
import logging
logging.basicConfig(level=logging.INFO, filename="logs\REST-API.log", filemode="a")


@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    logging.info(f"Starting the Json Server...")
    get_pid = subprocess.Popen('cmd /c "cd C://Users//Salim && json-server --watch db.json" ')
    time.sleep(5)
    logging.info(f"Json Server started and the process id is : {get_pid}")
    yield
    server_pid = int(get_pid.pid)
    logging.info(f"Server PID :{server_pid}")
    logging.info(f"Please Close the Server, Stopping the server automatically is pending...")
    time.sleep(2)
    os.system(f"""taskkill /f /im cmd.exe""")
    time.sleep(2)
    os.system("""taskkill /f /im conhost.exe""")

