from selenium import webdriver
import os
class TT():
    def test(self):
        driverLocation="D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://www.google.com")


ab = TT()
ab.test()