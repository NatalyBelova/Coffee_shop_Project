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



"""Проверка правильного перехода на все доступные пункты страницы"""
@pytest.mark.run(order=1)
@allure.description("Test Navigation")
def test_navigation():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.navigation_buy()
    mp.navigation_reviews()
    mp.navigation_community()
    mp.navigation_read()
    mp.navigation_working_conditions()

    print("Finish Test 1")
    driver.quit()



