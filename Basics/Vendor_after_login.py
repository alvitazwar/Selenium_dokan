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
        driver.implicitly_wait(3)
        prod=driver.find_element_by_xpath("//li[@class='products']//a[contains(text(),'Products')]").click()
        addnew=driver.find_element_by_xpath("//a[@class='dokan-btn dokan-btn-theme dokan-add-new-product']").click()
        prname=driver.find_element_by_xpath("//input[@placeholder='Product name..']").send_keys("Selenium")
        driver.find_element_by_xpath("//*[@id='select2-product_cat-container']").click()
        cat=driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[2]").click()
        desc=driver.find_element_by_xpath("//textarea[@placeholder='Enter some short description about this product...']").send_keys("SELEniun course")
        createproduct=driver.find_element_by_xpath("//*[@id='dokan-create-new-product-btn']").click()
        #browseprp=driver.find_element_by_xpath("//a[@class='woocommerce-Button button']").click()




        time.sleep(6)
object=Vendor()
object.test()

