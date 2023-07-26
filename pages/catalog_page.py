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


"""Страница каталога продуктов"""
class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    add_to_cart_natti = "//span[@class='buyText buyText_780']"
    go_to_cart = "//a[@class='blackBtn']"
    bright_espresso = "//label[@for='filter1a']"
    balanced_espresso = "//label[@for='filter2a']"
    bright_filter = "//label[@for='filter3a']"
    balanced_filter = "//label[@for='filter4a']"
    capsules = "//label[@for='filter5a']"
    drip_packs = "//label[@for='filter6a']"
    coffee_in_jars = "//label[@for='filter7a']"
    filter_price = "//*[@id='form-catalog-left']/div[1]/div[1]/div/button/div/div"
    check_box_price_down = "//a[@id='bs-select-1-1']"
    degree_of_roast = "//*[@id='form-catalog-left']/div[1]/div[2]/div[2]/button/div"
    light_roast = "//a[@id='bs-select-2-0']"
    coffee_taste = "//*[@id='form-catalog-left']/div[1]/div[3]/div/button/div"
    fruits_berries_taste = "//a[@id='bs-select-3-2']"
    add_to_cart_ColombiaCherrySantuario = "//span[@class='buyText buyText_1340']"
    go_to_cart_1 = "//a[@class='blackBtn']"
    add_to_cart_peru = "//span[@class='buyText buyText_1386']"
    continue_shopping = "/html/body/div[7]/div/button"
    add_to_cart_candy = "//span[@class='buyText buyText_5']"
    continue_shopping_1 = "/html/body/div[7]/div/button"
    add_to_cart_barry = "//span[@class='buyText buyText_1125']"
    go_to_cart_2 = "//a[@class='blackBtn']"
    logo_button = "/html/body/div[1]/header/div[1]/div/div[7]/a/img"



    """Getters"""

    def get_add_to_cart_natti(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_natti)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_bright_espresso(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bright_espresso)))

    def get_balanced_espresso(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.balanced_espresso)))

    def get_bright_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bright_filter)))

    def get_drip_packs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drip_packs)))

    def get_balanced_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.balanced_filter)))

    def get_capsules(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.capsules)))

    def get_coffee_in_jars(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_in_jars)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_check_box_price_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_price_down)))

    def get_degree_of_roast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.degree_of_roast)))

    def get_light_roast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.light_roast)))

    def get_coffee_taste(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_taste)))

    def get_fruits_berries_taste(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fruits_berries_taste)))

    def get_add_to_cart_ColombiaCherrySantuario(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_ColombiaCherrySantuario)))

    def get_go_to_cart_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_1)))

    def get_add_to_cart_peru(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_peru)))

    def get_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping)))

    def get_add_to_cart_candy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_candy)))

    def get_continue_shopping_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping_1)))

    def get_add_to_cart_barry(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_barry)))

    def get_go_to_cart_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_2)))

    def get_logo_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_button)))




    """Actions"""

    def click_add_to_cart_natti(self):
        self.get_add_to_cart_natti().click()
        print("Click add_to_cart_natti")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click go_to_cart")

    def click_bright_espresso(self):
        self.get_bright_espresso().click()
        print("Click bright_espresso")

    def click_balanced_espresso(self):
        self.get_balanced_espresso().click()
        print("Click balanced_espresso")

    def click_bright_filter(self):
        self.get_bright_filter().click()
        print("Click bright_filter")

    def click_balanced_filter(self):
        self.get_balanced_filter().click()
        print("Click balanced_filter")

    def click_capsules(self):
        self.get_capsules().click()
        print("Click capsules")

    def click_drip_packs(self):
        self.get_drip_packs().click()
        print("Click Drip Packs")

    def click_coffee_in_jars(self):
        self.get_coffee_in_jars().click()
        print("Click coffee_in_jars")

    def click_filter_price(self):
        self.get_filter_price().click()
        print("Click filter_price")

    def click_check_box_price_down(self):
        self.get_check_box_price_down().click()
        print("Click check_box_price_down")

    def click_degree_of_roast(self):
        self.get_degree_of_roast().click()
        print("Click degree_of_roast")

    def click_light_roast(self):
        self.get_light_roast().click()
        print("Click light_roast")

    def click_coffee_taste(self):
        self.get_coffee_taste().click()
        print("Click coffee_taste")

    def click_fruits_berries_taste(self):
        self.get_fruits_berries_taste().click()
        print("Click fruits_berries_taste")

    def click_add_to_cart_ColombiaCherrySantuario(self):
        self.get_add_to_cart_ColombiaCherrySantuario().click()
        print("Click add_to_cart_ColombiaCherrySantuario")

    def click_go_to_cart_1(self):
        self.get_go_to_cart_1().click()
        print("Click go_to_cart_1")

    def click_add_to_cart_peru(self):
        self.get_add_to_cart_peru().click()
        print("Click add_to_cart_peru")

    def click_continue_shopping(self):
        self.get_continue_shopping().click()
        print("Click continue_shopping")

    def click_add_to_cart_candy(self):
        self.get_add_to_cart_candy().click()
        print("Click add_to_cart_candy")

    def click_continue_shopping_1(self):
        self.get_continue_shopping_1().click()
        print("Click continue_shopping_1")

    def click_add_to_cart_barry(self):
        self.get_add_to_cart_barry().click()
        print("Click add_to_cart_barry")

    def click_go_to_cart_2(self):
        self.get_go_to_cart_2().click()
        print("Click go_to_cart_2")

    def click_logo_button(self):
        self.get_logo_button().click()
        print("Click Logo button")




    """Methods"""

    """Выбор товара"""
    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            self.click_add_to_cart_natti()
            self.click_go_to_cart()
            self.driver.execute_script("window.scrollTo(0, 300)")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')


    """Выбор одного товара, используя фильтры"""
    def select_product_with_filters(self):
        with allure.step("Select product with filters"):
            Logger.add_start_step(method='select_product_with_filters')
            self.click_drip_packs()
            self.click_balanced_filter()
            self.click_filter_price()
            self.click_check_box_price_down()
            self.click_degree_of_roast()
            self.click_light_roast()
            self.click_coffee_taste()
            self.click_fruits_berries_taste()
            self.click_add_to_cart_ColombiaCherrySantuario()
            self.click_go_to_cart_1()
            self.driver.execute_script("window.scrollTo(0, 300)")
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_product_with_filters')


    """Выбор нескольких товаров"""
    def select_some_products(self):
        with allure.step("Select some product"):
            Logger.add_start_step(method='select_some_products')
            self.click_add_to_cart_peru()
            self.click_continue_shopping()
            self.click_add_to_cart_candy()
            self.click_continue_shopping_1()
            self.click_add_to_cart_barry()
            self.click_go_to_cart_2()
            self.driver.execute_script("window.scrollTo(0, 300)")
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_some_products')



    """Нажатие на логотип. Ожидание: переход на главную страницу"""
    def click_logo(self):
        with allure.step("Click Logo"):
            Logger.add_start_step(method='click_logo')
            self.click_logo_button()
            time.sleep(2)
            self.assert_url("https://shop.tastycoffee.ru/")
            Logger.add_end_step(url=self.driver.current_url, method='click_logo')
        
