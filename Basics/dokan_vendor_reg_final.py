from selenium import webdriver
import  os
import  time


class RegisterCustomer():
    def test(self):
        driverLocation = "D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://dokan.ajaira.website/my-account/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        email= driver.find_element_by_xpath("//input[@id='reg_email']").send_keys("vendor1@gmail.com")
        password=driver.find_element_by_xpath("//input[@id='reg_password']").send_keys("Vn!@34675634")
        vendor=driver.find_element_by_xpath("//label[2]").click()
        firstname=driver.find_element_by_xpath("//input[@id='first-name']").send_keys("vendor")
        lastname=driver.find_element_by_xpath("//input[@id='last-name']").send_keys("one")
        shopname=driver.find_element_by_xpath("//input[@id='company-name']").send_keys("ShopTest")
        shopUrl=driver.find_element_by_xpath("//input[@id='seller-url']").send_keys("shoptest")
        phonenumber=driver.find_element_by_xpath("//input[@id='shop-phone']").send_keys("01711111222")
        register=driver.find_element_by_xpath("//button[@name='register']").click()
        Letsgo=driver.find_element_by_xpath("//a[@class='button-primary button button-large button-next lets-go-btn dokan-btn-theme']")
        time.sleep(5)


###################
#city=driver.find_element_by_xpath("//input[@id='address[city]']").send_keys("democityone")
        #zip=driver.find_element_by_xpath("//input[@id='address[zip]']").send_keys("1205")
        #country=driver.find_element_by_xpath("//*[@id='address[country]']/optgroup/option[19]").click()
        #state=driver.find_element_by_xpath("//input[@id='//li[@id='select2-calc_shipping_state-result-xuas-BD-13']']").click()
        #checkbox=driver.find_element_by_xpath("//label[contains(text(),'Show email address in store')]").click()
        #cont=driver.find_element_by_xpath("//input[@name='save_step']").click()
###################

object=RegisterCustomer()
object.test()