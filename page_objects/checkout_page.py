import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Baseclass import Baseclass
from page_objects.confirm_Page import ConfirmPage


class CheckoutPage(Baseclass):

    def __init__(self, driver):
        self.driver = driver

    div_products = (By.CSS_SELECTOR, ".card-title a")
    btn_cart_button = (By.CSS_SELECTOR, ".card-footer button")
    btn_checkout = (By.CSS_SELECTOR, "[class='nav-link btn btn-primary']")
    btn_success = (By.CSS_SELECTOR, "button.btn-success")

    def product(self):
        product_name = self.driver.find_elements(*CheckoutPage.div_products)
        return product_name

    def Addcartbutton(self):
        cart = self.driver.find_elements(*CheckoutPage.btn_cart_button)
        return cart

    def checkout(self):
        return self.driver.find_element(*CheckoutPage.btn_checkout).click()

    def success(self):
        self.driver.find_element(*CheckoutPage.btn_success).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
