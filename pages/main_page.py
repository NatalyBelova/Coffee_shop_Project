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
    email = "//input[@title='Введите ваш e-mail']"
    checkbox_consent = "/html/body/div[3]/div[7]/div/div/div/div[1]/form/div[2]/label/span[1]"
    subscription_email = "//input[@class='btnRn']"

    reviews = "//span[@class='reviewsCount']"
    community = "/html/body/div[1]/header/div[1]/div/div[8]/div[3]/a"
    read = "/html/body/div[1]/header/div[1]/div/div[8]/div[4]/a"
    coffee_magazine = "/html/body/div[1]/header/div[1]/div/div[8]/div[4]/ul/li[1]"
    working_conditions = "/html/body/div[1]/header/div[1]/div/div[8]/div[5]/a"
    discount_system = "/html/body/div[1]/header/div[1]/div/div[8]/div[5]/ul/li[2]"



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

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_checkbox_consent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_consent)))

    def get_subscription_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subscription_email)))

    def get_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reviews)))

    def get_community(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.community)))

    def get_read(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.read)))

    def get_working_conditions(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.working_conditions)))

    def get_coffee_magazine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_magazine)))

    def get_discount_system(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount_system)))




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

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")

    def click_checkbox_consent(self):
        self.get_checkbox_consent().click()
        print("Click Checkbox Consent")

    def click_subscription_email(self):
        self.get_subscription_email().click()
        print("Click Subscription Email")

    def click_reviews(self):
        self.get_reviews().click()
        print("Click Reviews")

    def click_community(self):
        self.get_community().click()
        print("Click Community")

    def click_read(self):
        self.get_read().click()
        print("Click Read")

    def click_working_conditions(self):
        self.get_working_conditions().click()
        print("Click Working Conditions")

    def click_coffee_magazine(self):
        self.get_coffee_magazine().click()
        print("Click Coffee Magazine")

    def click_discount_systems(self):
        self.get_discount_system().click()
        print("Click Discount system")






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


    """Оформление подписки на новости"""
    def subscription_news(self):
        with allure.step("Subscription news"):
            Logger.add_start_step(method='subscription_news')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.input_email("test.qa@yandex.ru")
            self.click_checkbox_consent()
            self.click_subscription_email()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='subscription_news')


    """Переход на страницe Купить"""
    def navigation_buy(self):
        with allure.step("Navigation Buy"):
            Logger.add_start_step(method='navigation_buy')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_buy_button()
            self.click_coffee()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='navigation_buy')


    """Переход на страницу Отзывы"""
    def navigation_reviews(self):
        with allure.step("Navigation Reviews"):
            Logger.add_start_step(method='navigation_reviews')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_reviews()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='navigation_reviews')


    """Переход на страницу Сообщество"""
    def navigation_community(self):
        with allure.step("Navigation Community"):
            Logger.add_start_step(method='navigation_community')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_community()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='navigation_community')


    """Переход на страницу Читать"""
    def navigation_read(self):
        with allure.step("Navigation Read"):
            Logger.add_start_step(method='navigation_read')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_read()
            self.click_coffee_magazine()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='navigation_read')


    """Переход на страницу Условия работы"""
    def navigation_working_conditions(self):
        with allure.step("Navigation Working Conditions"):
            Logger.add_start_step(method='navigation_working_conditions')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_working_conditions()
            self.click_discount_systems()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='navigation_working_conditions')



