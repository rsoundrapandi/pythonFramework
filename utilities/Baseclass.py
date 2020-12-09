import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def expilicitwait(self,text):

        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def scrolldown(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scrollup(self):
        return self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    def screenshot(self,screenshot):
        return self.driver.save_screenshot(screenshot)