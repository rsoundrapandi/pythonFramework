from selenium.webdriver.common.by import By

from page_objects.checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    Namelist = (By.XPATH, "div/h4/a")

    # product.find_element_by_xpath("div/h4/a").text

    # self.driver.find_element_by_link_text("Shop").click()

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page


