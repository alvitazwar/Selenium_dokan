from selenium import webdriver
import  os
import  time

class Customer():
    def test(self):
        driverLocation = "D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://dokan.ajaira.website/my-account/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        email = driver.find_element_by_xpath("//input[@id='reg_email']").send_keys("alvicustomer2@gmail.com")
        password = driver.find_element_by_xpath("//input[@id='reg_password']").send_keys("Vn!@34675634")
        customer = driver.find_element_by_xpath("//p[@class='form-row form-group user-role']//label[1]").click()
        register = driver.find_element_by_xpath("//button[@name='register']").click()

        time.sleep(6)
object=Customer()
object.test()