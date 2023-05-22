import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class ChangeFrame(object):

    def switch_the_frame(self):
        driver_service = Service(executable_path=r"C:\Users\andre\PycharmProjects\testare_teme\chromedriver.exe")
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.dofactory.com/html/iframe#examples")
        time.sleep(3)

        iframe_wikipedia = driver.find_element(By.XPATH, '//iframe[@src="https://www.wikipedia.org/wiki/Vincent_van_Gogh"]')
        driver.switch_to.frame(iframe_wikipedia)
        time.sleep(3)

        btn_language = driver.find_element(By.XPATH,'//input[@aria-label="Go to an article in another language. Available in 202 languages"]')
        btn_language.click()
        time.sleep(3)

        search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search for a language"]')
        search_bar.send_keys("Espagnol")
        time.sleep(2)

        select_language = driver.find_element(By.XPATH, '//a[@class="autonym"]')
        select_language.click()
        time.sleep(2)

instanta1 = ChangeFrame()
instanta1.switch_the_frame()

