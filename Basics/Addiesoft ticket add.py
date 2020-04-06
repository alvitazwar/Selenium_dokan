from selenium import webdriver
#import os
import time
class Webelement():
    def test_web(self):
        driverLocation="D:\\Python\\Files\\chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "http://addieapps.addiesoft.com/"
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        username = driver.find_element_by_xpath("//input[@name='Email']")
        username.send_keys("alvitazwar.addiesoft@gmail.com")
        password = driver.find_element_by_xpath("//input[@name='password']").send_keys("SQA052")
        login = driver.find_element_by_xpath("//button[@class='btn green uppercase']")
        login.click()
        ticket=driver.find_element_by_xpath("//div[1]/div[2]/div[1]/div/div[2]/div/ul/li[5]/a/span[1]").click()
        new_ticket=driver.find_element_by_xpath("//div[1]/div[2]/div[1]/div/div[2]/div/ul/li[5]/ul/li[1]/a/span").click()
        title=driver.find_element_by_xpath("//input[@name='Title']").send_keys("Update Solution")
        dept=driver.find_element_by_xpath("//*[@id='frm']//div[1]/div[1]/div/select/option[7]").click()
        cat=driver.find_element_by_xpath("//*[@id='frm']/div/div/div[2]/div[1]/div[2]/div/select/option[2]").click()
        pro=driver.find_element_by_xpath("//*[@id='frm']/div/div/div[2]/div[1]/div[3]/div/select/option[2]").click()
        date=driver.find_element_by_xpath("//*[@id='DueDate']").click()
        driver.find_element_by_xpath("//div[3]/div[1]/table/tbody/tr[3]/td[4]").click()
        des=driver.find_element_by_xpath("//*[@id='frm']//div/textarea").send_keys("ASC LGHSC")
        save=driver.find_element_by_xpath("//*[@id='frm']/div/div/div[4]/button[2]").click()
        time.sleep(40)
        driver.close()
alvi=Webelement()
alvi.test_web()