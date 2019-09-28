from selenium import webdriver
import os
import time
class Webelement():
    def test_web(self):
        driverLocation="D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseurl ="https://www.techlistic.com/p/selenium-practice-form.html"
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        firstname= driver.find_element_by_css_selector("[name='firstname']")
        firstname.send_keys("Alvi")
        lastname= driver.find_element_by_css_selector("[name='lastname']")
        lastname.send_keys("Tazwar")
        gender =driver.find_element_by_css_selector("[id='sex-0']")
        gender.click()
        exp= driver.find_element_by_css_selector("[id='exp-0']")
        exp.click()
        date=driver.find_element_by_id("datepicker")
        date.send_keys("28/9/2019")
        automation =driver.find_element_by_id("profession-0")
        automation.click()
        manual = driver.find_element_by_id("profession-1")
        manual.click()
        time.sleep(10)


alvi=Webelement()
alvi.test_web()


