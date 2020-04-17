from selenium import webdriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class Webelement():
     def webTest(self):
         driverLocation="D:\\Python\\Files\\chromedriver.exe"
         os.environ["webdriver.chrome.driver"] = driverLocation
         driver = webdriver.Chrome(driverLocation)
         baseurl="http://cgsd.oemsbd.com:2019"
         driver.get(baseurl)
         driver.maximize_window()
         driver.implicitly_wait(50)

         username= driver.find_element_by_xpath("//input[@name='Email']")
         username.send_keys("admin")
         password=driver.find_element_by_xpath("//input[@name='Password']")
         password.send_keys("hG41C440")
         login =driver.find_element_by_xpath("//button[@class='btn red btn-block uppercase']")
         login.click()
         # studentEntry=driver.find_element_by_xpath("//*[@id='accordion']/li[2]/div")
         #studentEntry.click()
         #quickaddstudent= driver.find_element_by_xpath("//*[@id='accordion']/li[2]/ul/li[1]/a/span")
         #quickaddstudent.click()
         inventory= driver.find_element_by_xpath("//ul[@id='pills-tab']//a[@href='/InventoryV/Dashboard']")
         inventory.click()
         setup= driver.find_element_by_xpath("//ul[@id='accordion']/li[2]/div/a[@href='#']/span[.='SetUp']")
         setup.click()
         unit= driver.find_element_by_xpath("//ul[@id='accordion']/li[2]/ul//a[@href='/InventoryV/UnitSetup']/span[.='Unit Setup']")
         unit.click()
         #addnew=driver.find_element_by_xpath("//button[@ng-click='resetForm()']")
         #addnew.click()
         try:
            WebDriverWait(driver, 20).until(
            ec.element_to_be_selected((By.CSS_SELECTOR('.btn-group-solid [data-target]s')))).click()
         finally:
             driver.quit()
         #unit_name= driver.find_element_by_xpath("//input[@name='CategoryName']")
         #unit_name.send_keys("newly added unit")
         #code=driver.find_element_by_xpath("//input[@name='code']")
         #code.send_keys("1234567")
         #save=driver.find_element_by_xpath("//button[@type='submit']")
         #save.click()
         time.sleep(5)
test= Webelement()
test.webTest()
"This is newly added line"