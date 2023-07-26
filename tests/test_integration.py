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



"""Проверка верного перехода на 'Оптовый сайт'"""
@pytest.mark.run(order=1)
@allure.description("Test Click Logo")
def test_wholesale_site():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.go_to_wholesale_site()

    print("Finish Test 1")
    driver.quit()



"""Расширенное тестирование. Проверка перехода на мессенеджер Telegram"""
@pytest.mark.run(order=2)
@allure.description("Test messenger WhatsApp")
def test_messenger_whats_app():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 2")

    mp = Main_page(driver)
    mp.messenger_telegram()


    print("Finish Test 2")
    driver.quit()



"""Расширенное тестирование. Проверка перехода на мессенеджер YouTube"""
@pytest.mark.run(order=3)
@allure.description("Test messenger Telegram")
def test_messenger_telegram(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 3")

    mp = Main_page(driver)
    mp.messenger_youtube()

    print("Finish Test 3")
    driver.quit()


"""Расширенное тестирование. Проверка перехода на мессенеджер VK"""
@pytest.mark.run(order=4)
@allure.description("Test messenger VK")
def test_messenger_vk(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 4")

    mp = Main_page(driver)
    mp.messenger_vk()

    print("Finish Test 4")
    driver.quit()

