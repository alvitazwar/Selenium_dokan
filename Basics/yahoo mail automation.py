from selenium import webdriver
#import os
import time

class Webelement():
    def test_web(self):
        driverLocation = "D:\\Python\\Files\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseurl = "http://sos.oemsbd.com:2019/"
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        username = driver.find_element_by_xpath("//input[@name='Email']")
        username.send_keys("admin")
        password = driver.find_element_by_xpath("//input[@name='Password']")
        password.send_keys("hG41C440")
        login = driver.find_element_by_xpath("//button[@class='btn red btn-block uppercase']")
        login.click()
        fees= driver.find_element_by_xpath("//ul[@id='pills-tab']//a[@href='/FeesV/Dashboard']")
        fees.click()
        Process=driver.find_element_by_xpath("//ul[@id='accordion']/li[4]/div")
        Process.click()
        process= driver.find_element_by_xpath("//ul[@id='accordion']/li[4]/ul//a[@href='/FeesV/FeesProcess']/span[.='Process']")
        process.click()
        select= driver.find_element_by_xpath("//*[@id=formProcessFeilds']/div[1]/div[1]/div/div/select/option[8]")
        select.click()

        time.sleep(6)



alvi = Webelement()
alvi.test_web()