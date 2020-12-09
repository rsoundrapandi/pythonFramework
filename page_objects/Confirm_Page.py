from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    txt_country = (By.ID,"country")
    link_text=(By.LINK_TEXT,"India")
    chx_terms=(By.CSS_SELECTOR,"[class='checkbox checkbox-primary']")
    btn_submit =(By.CSS_SELECTOR,"input.btn-lg")
    alert_success = (By.CSS_SELECTOR, ".alert-success")

    def searchcountry(self):

        self.driver.find_element(*ConfirmPage.txt_country).send_keys("ind")

        self.driver.find_element(*ConfirmPage.link_text).click()

    def success(self):
        self.driver.find_element(*ConfirmPage.chx_terms).click()
        self.driver.find_element(*ConfirmPage.btn_submit).click()
        self.driver.find_element(*ConfirmPage.alert_success).click()



