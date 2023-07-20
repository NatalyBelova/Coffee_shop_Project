import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Главная страница"""
class Main_page(Base):

    url = 'https://shop.tastycoffee.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    buy_button = "//a[@class='m-no-link menu__link-h menuAc openMob ']"
    coffee = "/html/body/div[1]/header/div[1]/div/div[8]/div[1]/ul/li[1]/a"
    change_city_button = "//span[@class='city_header_name']"
    city_moscow = "//a[@data-id='5']"


    """Getters"""

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_coffee(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee)))



    """Actions"""

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click Buy Button")

    def click_coffee(self):
        self.get_coffee().click()
        print("Click Coffee")



    """Methods"""

    """Выбор кнопки "Купить", переод в каталог товаров"""
    def select_menu(self):
        with allure.step("Select Menu"):
            Logger.add_start_step(method='select_menu')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.get_current_url()
            self.click_buy_button()
            self.click_coffee()
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')

