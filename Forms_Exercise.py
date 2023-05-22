import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class CompleteOnlineForm:

    def __init__(self):
        self.driver_service = Service(executable_path=r"C:\Users\andre\PycharmProjects\Tema_Curs5_Forms\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()
        self.driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        time.sleep(3)

    def insert_firstname(self):
        username_field = self.driver.find_element(By.ID, "RESULT_TextField-1")
        username_field.send_keys("Andreea")
        time.sleep(2)


    def insert_lastname(self):
        lastname_field = self.driver.find_element(By.ID, "RESULT_TextField-2")
        lastname_field.send_keys("Popa")
        time.sleep(2)


    def phone_number(self):
        phone_nr = self.driver.find_element(By.XPATH, '//input[@name="RESULT_TextField-3"]')
        phone_nr.send_keys(1234567890)
        time.sleep(2)

    def country_field(self):
        by_country = self.driver.find_element(By.ID, "RESULT_TextField-4")
        by_country.send_keys("Romania")
        time.sleep(2)

    def city_field(self):
        by_city =  self.driver.find_element(By.XPATH, '//input[@name="RESULT_TextField-5"]')
        by_city.send_keys("Bucuresti")
        time.sleep(2)

    def email_adress(self):
        e_mail = self.driver.find_element(By.XPATH, '//input[@name="RESULT_TextField-6"]')
        e_mail.send_keys("andreeapopa629@gmail.com")
        time.sleep(2)


    def gender_chosen(self):
        gender_radiobtn = self.driver.find_element(By.XPATH, '//label[@for="RESULT_RadioButton-7_1"]')
        gender_radiobtn.click()
        time.sleep(1)

    def free_days(self):
        sunday_checkbox = self.driver.find_element(By.XPATH, '//label[@for="RESULT_CheckBox-8_0"]')
        sunday_checkbox.click()
        time.sleep(1)
        saturday_checkbox = self.driver.find_element(By.XPATH, '//label[@for="RESULT_CheckBox-8_6"]')
        saturday_checkbox.click()
        time.sleep(1)


    def select_dropdown_value(self):
        dropdown_webelement = self.driver.find_element(By.ID, "RESULT_RadioButton-9")
        dropdown_menu = Select(dropdown_webelement)
        dropdown_menu.select_by_visible_text("Evening")
        time.sleep(1)

    def choose_file(self):
        choose_img = self.driver.find_element(By.XPATH, '//input[@class="file_upload"]')
        choose_img.send_keys(r"C:\Users\andre\PycharmProjects\Tema_Curs5_Forms\Netflix_Logo.png")
        time.sleep(1)

    def submit_btn(self):
        button_submit = self.driver.find_element(By.ID, 'FSsubmit')
        button_submit.click()
        time.sleep(1)

    def scroll_by_value(self, scroll_value):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_value});")
        time.sleep(2)


    def complete_form(self):
        self.insert_firstname()
        self.insert_lastname()
        self.phone_number()
        self.country_field()
        self.city_field()
        self.email_adress()
        self.gender_chosen()
        self.free_days()
        self.select_dropdown_value()
        self.choose_file()
        self.submit_btn()



inst1 = CompleteOnlineForm().complete_form()







