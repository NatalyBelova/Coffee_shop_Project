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



"""Проверка смены города"""
@pytest.mark.run(order=1)
@allure.description("Test Change City_1")
def test_change_city_omsk():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.change_city_omsk()

    print("Finish Test 1")
    driver.quit()


@pytest.mark.run(order=2)
@allure.description("Test Change City_2")
def test_change_city_kazan():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 2")

    mp = Main_page(driver)
    mp.change_city_kazan()


    print("Finish Test 2")
    driver.quit()

@pytest.mark.run(order=3)
@allure.description("Test Change City_3")
def test_change_city_yekaterinburg():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 3")

    mp = Main_page(driver)
    mp.change_city_yekaterinburg()

    print("Finish Test 3")
    driver.quit()







