import time
from logging import Logger

import allure
from selenium.webdriver.common.keys import Keys

from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


"""Страница авторизации"""
class Login_page(Base):

    url = 'https://shop.tastycoffee.ru/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    login_button = "//button[@class='greyLink enterOpen']"
    email = "//input[@id='email']"
    password = "//input[@id='password']"
    enter_button = "//input[@id='sign-in']"
    registration_button = "//div[@class='greyLink-wrap']"

    name_surname = "//input[@class='full_name suggestions-input']"
    email_registration = "//input[@placeholder='* E-Mail']"
    phone_number = "//input[@placeholder='* Телефон']"
    password_registration = "//input[@placeholder='* Пароль']"
    password_repeat_registration = "//input[@placeholder='* Повторите пароль']"
    create_account_button = "//a[@id='create_account']"



    """Getters"""

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))

    def get_name_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_surname)))

    def get_email_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_registration)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_password_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_registration)))

    def get_password_repeat_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_repeat_registration)))

    def get_create_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_account_button)))



    """Actions"""

    def click_login_button(self):
        self.get_login_button().click()
        print("CLick login button")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("CLick enter button")

    def click_registration_button(self):
        self.get_registration_button().click()
        print("CLick Registration button")

    def input_name_surname(self, name_surname):
        self.get_name_surname().send_keys(name_surname)
        print("Input Name and Surname")


    def input_email_registration(self, email_registration):
        self.get_email_registration().send_keys(email_registration)
        print("Input Email registration")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input Phone number")

    def input_password_registration(self, password_registration):
        self.get_password_registration().send_keys(password_registration)
        print("Input Password registration")

    def input_password_repeat_registration(self, password_repeat_registration):
        self.get_password_repeat_registration().send_keys(password_repeat_registration)
        print("Input Password Repeat registration")

    def click_create_account_button(self):
        self.get_create_account_button().click()
        print("CLick Create Account button")


    """Methods"""

    """Метод авторизации в существующей учетной записи"""
    def authorisation_valid_data(self):
        with allure.step("Authorisation Valid Data"):
            Logger.add_start_step(method='authorisation')
            self.driver.get(self.url) # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_button()
            self.input_email("test.qa@yandex.ru")
            self.input_password("000000")
            self.click_enter_button()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorisation')


    """Метод попытки регистрации в уже существующей учетной записи. Ожидаемый результат: невозможность регистрации, ошибка"""
    def registration(self):
        with allure.step("Registration"):
            Logger.add_start_step(method='registration')
            self.driver.get(self.url) # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.get_current_url()
            self.click_registration_button()
            self.input_name_surname("Иван Иванов")
            time.sleep(1)
            self.input_email_registration("test.qa@yandex.ru")
            self.input_phone_number("+7 (111) 222-3344")
            self.input_password_registration("000000")
            self.input_password_repeat_registration("000000")
            self.click_create_account_button()
            time.sleep(1)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='registration')



    """Метод авторизации в существующей учетной записи с неверными данными. Ожидание: ошибка"""
    def authorisation_invalid_data(self):
        with allure.step("Authorisation Invalid Data"):
            Logger.add_start_step(method='authorisation')
            self.driver.get(self.url) # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_button()
            self.input_email("test@yandex.ru")
            self.input_password("000000")
            self.click_enter_button()
            time.sleep(0.5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorisation')


