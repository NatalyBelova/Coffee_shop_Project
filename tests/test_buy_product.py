import time
import allure
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.shopping_cart_page import Shopping_cart_page


"""Smoke test. Проверка покупки товара без использования дополнительных фильтров"""
# @pytest.mark.run(order=2)
@allure.description("Test Registering an existing user")
def test_registration():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_menu()

    cp = Catalog_page(driver)
    cp.select_product()

    scp = Shopping_cart_page(driver)



    print("Finish Test 1")
    driver.quit()



"""Расширенное тестирование. Проверка покупки товара с использованием дополнительных фильтров"""

# @pytest.mark.run(order=2)
@allure.description("Test Registering an existing user")
def test_registration():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe',
                      chrome_options=options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_menu()

    print("Finish Test 1")
    driver.quit()