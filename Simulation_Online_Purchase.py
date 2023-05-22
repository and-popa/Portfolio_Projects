#1. Navigare pe https://www.saucedemo.com/
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ComandaProduse:
    def __init__(self):
        self.driver_service = Service(executable_path=r"C:\Users\andre\PycharmProjects\Tema_curs6\chromedriver.exe")
        self.driver = webdriver.Chrome(service= self.driver_service)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)

#2. Logare cu username si parola

    def logare_pe_pagina(self):
        username = self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
        username.click()
        username.send_keys("standard_user")
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password.click()
        password.send_keys("secret_sauce")
        time.sleep(2)

    def login_btn(self):
        buton_inregistrare = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        buton_inregistrare.click()
        time.sleep(2)


#3. Adaugam 6 produse in cosul de cumparaturi

    def adaugare_produse_in_cos(self):
        backpack_addtocart =  self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
        backpack_addtocart.click()
        time.sleep(1)

        bikelight_addtocart = self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
        bikelight_addtocart.click()
        time.sleep(1)

        tshirt_addtocart = self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
        tshirt_addtocart.click()
        time.sleep(1)

        hoodie_addtocart = self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        hoodie_addtocart.click()
        time.sleep(1)

        onesie_addtocart = self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-onesie"]')
        onesie_addtocart.click()
        time.sleep(1)

        redtshirt_addtocart = self.driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        redtshirt_addtocart.click()
        time.sleep(1)


#4. Click pe cosul de cumparaturi
    def bin_btn(self):
        cosul_de_cumparaturi = self.driver.find_element(By.XPATH,'//span[@class="shopping_cart_badge"]')
        cosul_de_cumparaturi.click()
        time.sleep(2)

#5. Stergere produs de 49,99$

    def stergere_produs(self):
        jacheta_de_sters = self.driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-fleece-jacket"]')
        jacheta_de_sters.click()
        time.sleep(2)


#6. Click checkout

    def check_out_btn(self):
        checkout_cumparaturi= self.driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
        checkout_cumparaturi.click()
        time.sleep(2)

#7. Introducem FirstName, LastName si Cod postal

    def completare_form(self):
        first_name = self.driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
        first_name.send_keys("Andreea")
        time.sleep(1)
        last_name = self.driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
        last_name.send_keys("Popa")
        time.sleep(1)
        cod_postal = self.driver.find_element(By.XPATH,'//input[@placeholder="Zip/Postal Code"]')
        cod_postal.send_keys(1223)
        time.sleep(1)

#8.Click pe Continue
    def continue_btn(self):
        continue_form = self.driver.find_element(By.XPATH, '//input[@data-test="continue"]')
        continue_form.click()
        time.sleep(2)

#9.Click pe Finish

    def finish_btn(self):
        buton_finish = self.driver.find_element(By.XPATH, '//button[@data-test="finish"]')
        buton_finish.click()
        time.sleep(2)

#10.Revenire la produse
    def backhome_btn(self):
        buton_backhome = self.driver.find_element(By.XPATH, '//button[@data-test="back-to-products"]')
        buton_backhome.click()
        time.sleep(1)

    def scroll_by_value(self, scroll_value):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_value});")
        time.sleep(2)



ins1 = ComandaProduse()
ins1.logare_pe_pagina()
ins1.login_btn()
ins1.scroll_by_value(200)
ins1.adaugare_produse_in_cos()
ins1.scroll_by_value(-200)
ins1.bin_btn()
ins1.scroll_by_value(400)
ins1.stergere_produs()
ins1.scroll_by_value(100)
ins1.check_out_btn()
ins1.completare_form()
ins1.continue_btn()
ins1.scroll_by_value(700)
ins1.finish_btn()
ins1.backhome_btn()







