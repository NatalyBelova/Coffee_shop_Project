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
@pytest.mark.run(order=1)
@allure.description("Test Buy One Product")
def test_buy_product():
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
    scp.ordering_product()

    print("Finish Test 1")
    driver.quit()



"""Расширенное тестирование. Проверка покупки товара с использованием дополнительных фильтров"""
@pytest.mark.run(order=2)
@allure.description("Test Buy One Product with Filters")
def test_buy_product_wit_filters():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 2")

    mp = Main_page(driver)
    mp.select_menu()

    cp = Catalog_page(driver)
    cp.select_product_with_filters()

    print("Finish Test 2")
    driver.quit()




"""Расширенное тестирование. Проверка покупки нескольких товаров"""
@pytest.mark.run(order=3)
@allure.description("Test Buy Some Product")
def test_buy_some_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 3")

    mp = Main_page(driver)
    mp.select_menu()

    cp = Catalog_page(driver)
    cp.select_some_products()

    print("Finish Test 3")
    driver.quit()