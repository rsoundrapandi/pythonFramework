import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Baseclass import Baseclass
from page_objects.home_page import HomePage


class Test_Suite(Baseclass):

    def test_e2e(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopitems()
        product_name = checkout_page.product()
        i = -1
        for product in product_name:
            i = i + 1
            print(i)
            pd_name = product.text
            log.info(pd_name)
            print(pd_name)
        if pd_name == getData["ProductName"]:
            self.scrolldown()
            checkout_page.Addcartbutton()[i].click()
            # self.expilicitwait("India")
            self.scrollup()
            assert pd_name == 'Blackberry'
        self.screenshot(getData["Screenshot"])

    @pytest.fixture(params=[{"ProductName": "Blackberry", "Screenshot": "Test2.png"}])
    def getData(self, request):
        return request.param
