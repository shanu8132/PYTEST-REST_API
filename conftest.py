import time
import pytest
import subprocess
import os
from utilities.customLogger import CustLogger
logger = CustLogger.custLogger()
#logging.basicConfig(level=logging.INFO, filename="logs\REST-API.log", filemode="a", format='%(asctime)s - %(levelname)s - %(module)s : %(message)s')


@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    logger.info(f"Starting the Json Server...")
    get_pid = subprocess.Popen('cmd /c "cd C://Users//Salim && json-server --watch db.json" ')
    time.sleep(5)
    logger.info(f"Json Server started and the process id is : {get_pid}")
    yield
    server_pid = int(get_pid.pid)
    logger.info(f"Server PID :{server_pid}")
    logger.info(f"Closing the Json API Server...")
    time.sleep(2)
    os.system(f"""taskkill /f /im cmd.exe""")
    time.sleep(2)
    os.system("""taskkill /f /im conhost.exe""")
    time.sleep(2)
    logger.info("Server closed successfully.")

