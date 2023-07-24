import time
from telnetlib import EC

import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger




"""Страница каталога кофе"""
class Shopping_cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    name_surname = "//input[@class='full_name suggestions-input']"
    email = "//input[@class='emailHelper suggestions-input']"
    phone_number = "//input[@class='phone-mask phone']"
    delivery_method_by_courier = "//label[@class='shipTab__link shipTab__link-courier active']"
    street_house = "//input[@placeholder='Улица, дом']"
    apartment = "//input[@placeholder='Квартира/Офис']"
    payment_methods = "//label[@for='payment_cod']"



    """Getters"""

    def get_name_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_surname)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_delivery_method_by_courier(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_by_courier)))

    def get_street_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_house)))

    def get_apartment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apartment)))

    def get_payment_methods(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_methods)))




    """Actions"""

    def input_name_surname(self, name_surname):
        self.get_name_surname().send_keys(name_surname)
        print("Input Name and Surname")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input Phone Number")

    def click_delivery_method_by_courier(self):
        self.get_delivery_method_by_courier().click()
        print("Click Delivery method Courier")

    def input_street_house(self, street_house):
        self.get_street_house().send_keys(street_house)
        print("Input Street and House")

    def input_apartment(self, apartment):
        self.get_apartment().send_keys(apartment)
        print("Input Apartment")

    def click_payment_methods(self):
        self.get_payment_methods().click()
        print("Click Payment Methods")


    """Methods"""

    """Добавление данных о покупателе в заказ"""
    def buy_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            fake = Faker("ru_RU")
            self.input_name_surname(fake.name())
            time.sleep(1)
            self.get_name_surname().send_keys(Keys.RETURN)
            self.input_email(fake.ascii_free_email())
            self.input_phone_number(fake.phone_number())
            Logger.add_end_step(url=self.driver.current_url, method='select_product')




