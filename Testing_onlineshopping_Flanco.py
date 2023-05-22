import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class PurchaseCart:

    def __init__(self):
        self.driver_service = Service(executable_path=r"C:\Users\andre\PycharmProjects\Tema_curs7\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()
        self.driver.get("https://www.flanco.ro/")
        time.sleep(3)

    def accept_cookies(self):
        cookies_btn = self.driver.find_element(By.XPATH, '//a[@class="x-agree"]')
        cookies_btn.click()
        time.sleep(2)

    def select_product(self):
        item_btn = self.driver.find_element(By.XPATH, '//button[@title="Toggling menu"]')
        item_btn.click()
        time.sleep(2)
        laptop_btn = self.driver.find_element(By.XPATH, '//figure[@aria-controls="category-node-3"]')
        laptop_btn.click()
        time.sleep(2)


    def notebook_memory(self):
        memory_btn = self.driver.find_element(By.XPATH, '//span[text() = "Memorii Notebook"]')
        memory_btn.click()
        time.sleep(1)
        price_btn = self.driver.find_element(By.XPATH, '//a[@href="https://www.flanco.ro/laptop-it-tablete/componente/memorii-notebook/filtre/price/200-300.html"]')
        price_btn.click()
        time.sleep(1)
        memory_type = self.driver.find_element(By.XPATH, '//a[@href="https://www.flanco.ro/laptop-it-tablete/componente/memorii-notebook/filtre/price/200-300/tip-memorie-pc-lap/ddr4.html"]')
        memory_type.click()
        time.sleep(2)

    def scroll_by_value(self, scroll_value):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_value});")
        time.sleep(2)


    def add_product(self):
        add_item_btn = self.driver.find_element(By.XPATH,'//form[@data-product-sku="177934"]')
        add_item_btn.click()
        time.sleep(3)


    def details_cart_products(self):
        cart_btn = self.driver.find_element(By.XPATH, '//div[@class="aj-product-controller__gocheckout checkoutPopupDesktop"]')
        cart_btn.click()
        time.sleep(2)

    def select_dropdown_value(self):
        multiple_values_webelem = self.driver.find_element(By.XPATH, '//select[@data-cart-item-id="177934"]')
        multiple_values_webelem.click()
        multiple_values_menu = Select(multiple_values_webelem)
        multiple_values_menu.select_by_value("4")
        time.sleep(5)


    def take_screenshot_by_time(self, screenshot_name, path_to_save_ss):
        screenshot_n = screenshot_name + ".png"
        destination_of_screenshot = path_to_save_ss + "\\" + screenshot_n
        self.driver.save_screenshot(destination_of_screenshot)
        time.sleep(3)

    def checkout_step(self):
        checkout_btn = self.driver.find_element(By.XPATH, '//button[@title="Pasul urmator"]')
        checkout_btn.click()
        time.sleep(1)



instanta1 = PurchaseCart()
instanta1.accept_cookies()
instanta1.select_product()
instanta1.notebook_memory()
instanta1.scroll_by_value(200)
instanta1.add_product()
instanta1.details_cart_products()
instanta1.select_dropdown_value()
instanta1.take_screenshot_by_time("Total price shopping cart from Flanco", r"C:\Users\andre\PycharmProjects\Tema_curs7")
instanta1.checkout_step()

