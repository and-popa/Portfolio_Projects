import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CompleteHerokuHtmlForm:

    def __init__(self):
        self.driver_service = Service(executable_path=r'D:\Exercitii pycharm AU Testing\Basic_HTML_Form\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()
        self.driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
        time.sleep(3)

    def insert_username(self):
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys("Ionescu Andrei Bogdan")
        time.sleep(1)

    def insert_password(self):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("secretpassword123")
        time.sleep(1)

    def textarea_comment(self):
        textarea = self.driver.find_element(By.XPATH, "//textarea[@name = 'comments']")
        textarea.clear()
        time.sleep(1)
        textarea.send_keys("Am inserat un text")
        time.sleep(1)

    def insert_file(self):
        choose_file_btn = self.driver.find_element(By.XPATH, "//input[@name = 'filename']")
        choose_file_btn.send_keys(r"C:\Users\andre\OneDrive\Desktop\Python.png")
        time.sleep(1)

    def select_checkboxes(self):
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@name='checkboxes[]']")
        last_checkbox = checkboxes[-1]
        first_two_checkboxes = checkboxes[:2]
        for checkbox in first_two_checkboxes:
            checkbox.click()
            time.sleep(1)
        last_checkbox.click()

    def select_radiobtn(self):

        radiobuttons = self.driver.find_elements(By.XPATH, '//input[@name="radioval"]')
        second_radio_btn = radiobuttons[-2]
        first_radiobtn = radiobuttons[0]
        first_radiobtn.click()
        time.sleep(1)
        third_radiobtn = radiobuttons[2]
        third_radiobtn.click()
        time.sleep(1)
        second_radio_btn.click()

    def select_multiple_values(self):
        multiple_values_webelem = self.driver.find_element(By.XPATH, "//select[@name='multipleselect[]']")
        multiple_values_menu = Select(multiple_values_webelem)

        multiple_values_menu.select_by_value("ms1")
        time.sleep(2)

        # multiple_values_menu.select_by_index(2)
        # time.sleep(2)
        #
        # multiple_values_menu.select_by_visible_text("Selection Item 2")
        # time.sleep(2)

        multiple_values_menu.deselect_all()
        time.sleep(1)

    def select_dropdown_value(self):
        dropdown_webelem = self.driver.find_element(By.XPATH, "//select[@name='dropdown']")
        dropdown_menu = Select(dropdown_webelem)

        dropdown_menu.select_by_value("dd3")
        time.sleep(1)
        dropdown_menu.select_by_index(5)
        time.sleep(1)
        dropdown_menu.select_by_visible_text("Drop Down Item 2")
        time.sleep(1)

    def click_submit(self):
        submit_btn = self.driver.find_element(By.XPATH, "//input[@type = 'submit']")
        submit_btn.click()
        time.sleep(5)

    def scroll_by_value(self, scroll_value):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_value});")
        time.sleep(2)

    def complete_form(self):
        self.insert_username()
        self.insert_password()
        self.textarea_comment()
        self.insert_file()
        self.select_checkboxes()
        self.select_radiobtn()
        self.select_multiple_values()
        self.select_dropdown_value()
        self.click_submit()


inst1 = CompleteHerokuHtmlForm().complete_form()
