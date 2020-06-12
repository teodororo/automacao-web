import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


class SaucedemoAutomationTest(unittest.TestCase):
    BROWSER = ''

    def setUp(self):
        # Instanciação do Webdriver
        # self.driver = webdriver.Chrome('./drivers/chromedriver')
        if self.BROWSER == 'chrome':
            self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
        elif self.BROWSER == 'firefox':
            self.driver = webdriver.Firefox('./drivers/geckodriver.exe')
        elif self.BROWSER == 'edge':
            self.driver = webdriver.Edge('./drivers/msedgedriver.exe')
        else:
            return 'Argumento inválido'
        self.baseUrl = "https://www.saucedemo.com/"

    def test_invalidLogin(self):
        self.driver.get(self.baseUrl)
        name_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_btn = self.driver.find_element_by_class_name("btn_action")
        name_field.send_keys("admin")
        password_field.send_keys("admin")
        login_btn.click()
        self.assertTrue(
            "Username and password do not match any user in this service" in self.driver.page_source)

    def test_validLogin(self):
        self.driver.get(self.baseUrl)
        name_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_btn = self.driver.find_element_by_class_name("btn_action")
        name_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_btn.click()
        self.assertTrue("Products" in self.driver.page_source)

    def test_addCart(self):
        self.driver.get(self.baseUrl + "inventory.html")
        btn_inventory = self.driver.find_element_by_xpath(
            "//div[@class='pricebar']//button[1]")
        shopping_cart = self.driver.find_element_by_id(
            "shopping_cart_container")
        btn_inventory.click()
        shopping_cart.click()
        item = self.driver.find_element_by_xpath("//button[text()='REMOVE']")
        self.assertTrue(item.is_displayed())

    def test_rmCart(self):
        self.driver.get(self.baseUrl + "inventory.html")
        btn_inventory = self.driver.find_element_by_xpath(
            "//div[@class='pricebar']//button[1]")
        shopping_cart = self.driver.find_element_by_id(
            "shopping_cart_container")
        btn_inventory.click()
        btn_inventory.click()
        shopping_cart.click()
        try:
            # if it raises an error, then the button isn't displayed
            item = self.driver.find_element_by_xpath(
                "//button[text()='REMOVE']")
        except:
            self.assertTrue

    def test_invalidCheckout(self):
        self.driver.get(self.baseUrl + "checkout-step-one.html")
        bnt_checkout = self.driver.find_element_by_xpath(
            "//div[@class='checkout_buttons']//input[1]")
        bnt_checkout.click()
        self.assertTrue(
            "Error: First Name is required" in self.driver.page_source)

    def test_validCheckout(self):
        self.driver.get(self.baseUrl + "checkout-step-one.html")
        bnt_checkout = self.driver.find_element_by_xpath(
            "//div[@class='checkout_buttons']//input[1]")
        name_field = self.driver.find_element_by_id("first-name")
        lastname_field = self.driver.find_element_by_id("last-name")
        postalcode_field = self.driver.find_element_by_id("postal-code")
        name_field.send_keys("Aurea")
        lastname_field.send_keys("Melo")
        postalcode_field.send_keys("69000000")
        bnt_checkout.click()
        self.assertTrue("Payment Information" in self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        SaucedemoAutomationTest.BROWSER = sys.argv.pop()
    unittest.main()
