from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os
import time
class TT():
    def test(self):
        driverLocation="D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://login.yahoo.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        #cr=driver.find_element_by_xpath("//a[@id='createacc']")
        #driver.findElement(By.linktext("Create New Account")).click()
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/form/div[4]/p/a").click()

        time.sleep(5)



ab = TT()
ab.test()