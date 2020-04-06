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
        email= driver.find_element_by_xpath("//input[@id='reg_email']").send_keys("alvidip@gmail.com")
        password=driver.find_element_by_xpath("//input[@id='reg_password']").send_keys("Vn!@34675634")
        vendor=driver.find_element_by_xpath("//label[2]").click()
        firstname=driver.find_element_by_xpath("//input[@id='first-name']").send_keys("vendor")
        lastname=driver.find_element_by_xpath("//input[@id='last-name']").send_keys("one")
        shopname=driver.find_element_by_xpath("//input[@id='company-name']").send_keys("vnshop")
        shopUrl=driver.find_element_by_xpath("//input[@id='seller-url']").send_keys("vnshop")
        phonenumber=driver.find_element_by_xpath("//input[@id='shop-phone']").send_keys("01711111222")
        register=driver.find_element_by_xpath("//button[@name='register']").click()

        #Letsgo=driver.find_element_by_xpath("//a[@class='button-primary button button-large button-next lets-go-btn dokan-btn-theme']")
        letgo=driver.find_element_by_link_text("Let's Go!").click()
        driver.implicitly_wait(10)
        time.sleep(3)

        storeproduct=driver.find_element_by_xpath("//input[@id='store_ppp']").send_keys("5")
        staddress1=driver.find_element_by_xpath("//*[@id='address[street_1]']").send_keys("Streetone")
        staddress2=driver.find_element_by_xpath("//*[@id='address[street_2]']").send_keys("demoaddresstwo")
        city=driver.find_element_by_xpath("//input[@id='address[city]']").send_keys("DHAKA")
        zip = driver.find_element_by_xpath("//input[@id='address[zip]']").send_keys("1205")
        country = driver.find_element_by_xpath("//*[@id='address[country]']/optgroup/option[19]").click()
        driver.implicitly_wait(2)
        #state = driver.find_element_by_css_selector("#select2-calc_shipping_state-result-5fc7-BD-13").click()
        #state=driver.find_element_by_xpath("//*[@id='select2-calc_shipping_state-result-5fc7-BD-13']").click()
        checkbox = driver.find_element_by_xpath("//label[contains(text(),'Show email address in store')]").click()
        cont = driver.find_element_by_xpath("//input[@name='save_step']").click()
        driver.implicitly_wait(10)
        time.sleep(3)
        acname=driver.find_element_by_xpath(" //input[@placeholder='Your bank account name']").send_keys("demoacc")
        acnum=driver.find_element_by_xpath("//input[@placeholder='Your bank account number']").send_keys("112233445566")
        namebank=driver.find_element_by_xpath("//input[@placeholder='Your bank account number']").send_keys("janata")
        skip=driver.find_element_by_xpath("//a[@class='button button-large button-next payment-step-skip-btn dokan-btn-theme']").click()
        driver.implicitly_wait(3)
        time.sleep(2)
        Dashboard= driver.find_element_by_xpath("//a[@class='button button-primary dokan-btn-theme']").click()


        time.sleep(5)




object=RegisterCustomer()
object.test()