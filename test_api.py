from utilities.customLogger import CustLogger
import logging

# Creating this test file to check the customLogger is working fine or not with multiple files with different log level

class Test_API_New:
    logger = CustLogger.custLogger(loglevel=logging.DEBUG)

    def test_api_new(self):
        self.logger.info("Log from another python file")
        self.logger.debug("Debug Log")