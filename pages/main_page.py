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
    wholesale_site = "/html/body/div[1]/header/div[1]/div/div[4]/ul/li[2]/a"

    telegram_button = "//a[@class='socBtn tg']"
    youtube_button = "//a[@class='socBtn yt']"
    vk_button = "//a[@class='socBtn vk']"


    """Getters"""

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_coffee(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee)))

    def get_wholesale_site(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wholesale_site)))

    def get_telegram_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram_button)))

    def get_youtube_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.youtube_button)))

    def get_vk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vk_button)))




    """Actions"""

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click Buy Button")

    def click_coffee(self):
        self.get_coffee().click()
        print("Click Coffee")

    def click_wholesale_site(self):
        self.get_wholesale_site().click()
        print("Click Wholesale Site")

    def click_telegram_button(self):
        self.get_telegram_button().click()
        print("Click Telegram Button")

    def click_youtube_button(self):
        self.get_youtube_button().click()
        print("Click YouTube Button")

    def click_vk_button(self):
        self.get_vk_button().click()
        print("Click VK Button")



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
            self.assert_url("https://shop.tastycoffee.ru/coffee")
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')


    """Переход на Оптовый сайт"""
    def go_to_wholesale_site(self):
        with allure.step("Select Menu"):
            Logger.add_start_step(method='select_menu')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.click_wholesale_site()
            time.sleep(7)
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')


    """Переход в мессенджер Telegram"""
    def messenger_telegram(self):
        with allure.step("Messenger Telegram"):
            Logger.add_start_step(method='messenger_telegram')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(0, 7000)")
            time.sleep(2)
            self.click_telegram_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='messenger_telegram')


    """Переход в мессенджер WhatsApp"""
    def messenger_youtube(self):
        with allure.step("Messenger YouTube"):
            Logger.add_start_step(method='messenger_youtube')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(0, 7000)")
            time.sleep(2)
            self.click_youtube_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='messenger_youtube')


    """Переход в мессенджер Vk"""
    def messenger_vk(self):
        with allure.step("Messenger VK"):
            Logger.add_start_step(method='messenger_vk')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(0, 7000)")
            time.sleep(2)
            self.click_vk_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='messenger_vk')

