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
class Products_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver


    """Locators"""

    filter_size = "/html/body/main/div[2]/div/aside/div[2]/div[4]/a/div"



    """Getters"""

    def get_filter_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size)))




    """Actions"""

    def click_filter_size(self):
        self.get_filter_size().click()
        print("Click Filter Size")


    """Methods"""

    """Используем фильтры для выбора нужного товара"""
    def select_products(self):
        with allure.step("Select products"):
            Logger.add_start_step(method='select_products')


            Logger.add_end_step(url=self.driver.current_url, method='select_products')

