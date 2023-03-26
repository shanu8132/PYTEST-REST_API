import inspect
import logging

class CustLogger:
    def custLogger(loglevel=logging.DEBUG):
        # set class/method name from where it is called
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        print(f"logger_name : {logger_name}")
        logger.setLevel(loglevel)
        fh = logging.FileHandler("logs/REST-API.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
