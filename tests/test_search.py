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

from pages.main_page import Main_page



"""Проверка верной работы строки поиска по слову 'Шоколад'"""
@pytest.mark.run(order=1)
@allure.description("Test Search 1")
def test_search_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.search_chocolate()

    print("Finish Test 1")
    driver.quit()


"""Проверка верной работы строки поиска по слову 'Подарочный сертификат'"""
@pytest.mark.run(order=2)
@allure.description("Test Search 2")
def test_search_2():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 2")

    mp = Main_page(driver)
    mp.search_gift_certificate()

    print("Finish Test 2")
    driver.quit()


"""Проверка верной работы строки поиска по слову 'Бразилиа можиана'"""
@pytest.mark.run(order=3)
@allure.description("Test Search 3")
def test_search_3():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 3")

    mp = Main_page(driver)
    mp.search_brazil_mogiana()

    print("Finish Test 3")
    driver.quit()


