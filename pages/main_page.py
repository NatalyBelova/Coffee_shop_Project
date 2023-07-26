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
    search = "//div[@id='openSearch_h']"
    enter_in_search = "//input[@id='search_h']"
    change_city_button = "//button[@id='city_open']"
    city_Omsk = "//a[@data-id='23']"
    city_Kazan = "//a[@data-id='30']"
    city_Yekaterinburg = "//a[@data-id='22']"


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

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_enter_in_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_in_search)))

    def get_change_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_city_button)))

    def get_city_Omsk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Omsk)))

    def get_city_Kazan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Kazan)))

    def get_city_Yekaterinburg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Yekaterinburg)))




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

    def click_search(self):
        self.get_search().click()
        print("Click Search")

    def input_enter_in_search(self, product):
        self.get_enter_in_search().send_keys(product)
        print("Input in search")

    def click_change_city_button(self):
        self.get_change_city_button().click()
        print("Click Change City button")

    def click_city_Omsk(self):
        self.get_city_Omsk().click()
        print("Click City Omsk")

    def click_city_Kazan(self):
        self.get_city_Kazan().click()
        print("Click city Kazan")

    def click_city_Yekaterinburg(self):
        self.get_city_Yekaterinburg().click()
        print("Click city Yekaterinburg")




    """Methods"""

    """Выбор кнопки "Купить", переод в каталог товаров"""
    def select_menu(self):
        with allure.step("Select Menu"):
            Logger.add_start_step(method='select_menu')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_buy_button()
            self.click_coffee()
            self.assert_url("https://shop.tastycoffee.ru/coffee")
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')


    """Переход на Оптовый сайт"""
    def go_to_wholesale_site(self):
        with allure.step("Select Wholesale Site"):
            Logger.add_start_step(method='select_wholesale_site')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_wholesale_site()
            time.sleep(7)
            Logger.add_end_step(url=self.driver.current_url, method='select_wholesale_site')


    """Переход в мессенджер Telegram"""
    def messenger_telegram(self):
        with allure.step("Messenger Telegram"):
            Logger.add_start_step(method='messenger_telegram')
            self.driver.get(self.url)
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
            self.driver.get(self.url)
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
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(0, 7000)")
            time.sleep(2)
            self.click_vk_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='messenger_vk')


    """Метод проверки строки поиска по слову 'Шоколад'"""
    def search_chocolate(self):
        with allure.step("Search Chocolate"):
            Logger.add_start_step(method='search_chocolate')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_enter_in_search("Шоколад")
            self.get_enter_in_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_chocolate')



    """Метод проверки строки поиска по слову 'Подарочный сертификат'"""
    def search_gift_certificate(self):
        with allure.step("Search Gift certificate"):
            Logger.add_start_step(method='gift_certificate')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_enter_in_search("Подарочный сертификат")
            self.get_enter_in_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='gift_certificate')



    """Метод проверки строки поиска по слову 'Бразилия можиана'"""
    def search_brazil_mogiana(self):
        with allure.step("Search Brazil Mogiana"):
            Logger.add_start_step(method='brazil_mogiana')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_enter_in_search("Бразилия можиана")
            self.get_enter_in_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='brazil_mogiana')


    """Смена города на Омск"""
    def change_city_omsk(self):
        with allure.step("Change city Omsk"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city_button()
            self.click_city_Omsk()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')


    """Смена города на Казань"""
    def change_city_kazan(self):
        with allure.step("Change city Kazan"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city_button()
            self.click_city_Kazan()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')


    """Смена города на Екатеринбург"""
    def change_city_yekaterinburg(self):
        with allure.step("Change city Yekaterinburg"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city_button()
            self.click_city_Yekaterinburg()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')
