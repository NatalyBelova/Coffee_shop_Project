import time
from telnetlib import EC

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


"""Страница каталога кофе"""
class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    add_to_cart_natti = '//*[@id="catalog-products"]/div[1]/div[1]/form/div[6]/div/div[3]/a'
    go_to_cart = "//a[@class='blackBtn']"


    """Getters"""

    def get_add_to_cart_natti(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_natti)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))




    """Actions"""

    def click_add_to_cart_natti(self):
        self.get_add_to_cart_natti().click()
        print("Click Add to Cart Natti")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click Go to cart")



    """Methods"""

    """Выбор товара"""
    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            self.click_add_to_cart_natti()
            self.click_go_to_cart()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')
        

