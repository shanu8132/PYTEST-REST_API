import time

import pytest
import subprocess
import os


@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    print(f"Starting the Json Server...")
    get_pid = subprocess.Popen('cmd /c "cd C://Users//Salim && json-server --watch db.json" ')
    time.sleep(5)
    print(f"Json Server started and the process id is : {get_pid}")
    yield
    server_pid = int(get_pid.pid)
    print(f"Server PID :{server_pid}")
    print(f"Please Close the Server, Stopping the server automatically is pending...")
    os.system(f"""taskkill /f /im cmd.exe""")
    os.system("""taskkill /f /im conhost.exe""")

