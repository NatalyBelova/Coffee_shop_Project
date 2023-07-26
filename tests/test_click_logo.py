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



"""Проверка: при нажатии на логотип, осуществляется переход на главную страницу"""
@pytest.mark.run(order=1)
@allure.description("Test Click Logo")
def test_click_logo():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.select_menu()

    cp = Catalog_page(driver)
    cp.click_logo()

    print("Finish Test 1")
    driver.quit()



