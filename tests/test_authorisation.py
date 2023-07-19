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


from pages.login_page import Login_page


"""Тест Проверка входа уже существующего пользователя"""
# @pytest.mark.run(order=1)
@allure.description("Test Authorisation")
def test_authorisation_valid_data():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    login = Login_page(driver)
    login.authorisation_valid_data()


    print("Finish Test 1")
    driver.quit()


"""Тест Попытка регистрации в уже существующей учетной записи. Ожидаемый результат: невозможность регистрации, ошибка"""
# @pytest.mark.run(order=2)
@allure.description("Test Registering an existing user")
def test_registration():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    login = Login_page(driver)
    login.registration()


    print("Finish Test 1")
    driver.quit()



"""Тест Проверка входа уже существующего пользователя с неверными данными. Ожидание: ошибка"""
# @pytest.mark.run(order=3)
@allure.description("Test Authorisation Invalid Data")
def test_authorisation_invalid_data():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    login = Login_page(driver)
    login.authorisation_invalid_data()


    print("Finish Test 1")
    driver.quit()



