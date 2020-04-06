from selenium import webdriver
import  os
import  time

class Vendor():
    def test(self):
        driverLocation = "D:\\Python\\Files\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://dokan.ajaira.website/my-account/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        username=driver.find_element_by_xpath("//input[@id='username']").send_keys("vnabcd@gmail.com")
        password=driver.find_element_by_xpath("//input[@id='password']").send_keys("Vn!@34675634")
        rem=driver.find_element_by_xpath("//input[@id='rememberme']").click()
        log=driver.find_element_by_xpath("//button[@name='login']").click()
        driver.implicitly_wait(5)
        coupon=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/article/div/div/div[1]/div/ul/li[4]/a").click()
        add_new=driver.find_element_by_xpath("//a[@class='dokan-btn dokan-btn-theme dokan-right']").click()
        cname=driver.find_element_by_xpath("//input[@id='title']").send_keys("new coupon")
        amnt=driver.find_element_by_xpath("//input[@id='amount']").send_keys("100")
        prod=driver.find_element_by_xpath("//a[@class='dokan-btn dokan-btn-default dokan-btn-sm dokan-coupon-product-select-all']").click()
        chkbox=driver.find_element_by_xpath("//input[@id='checkboxes-3']").click()
        button=driver.find_element_by_xpath("//input[@name='coupon_creation']").click()
        driver.find_element_by_xpath("//a[contains(text(),'Howdy,')]").click()
        logout=driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']//a[contains(text(),'Log out')]").click()



        time.sleep(6)
object=Vendor()
object.test()
