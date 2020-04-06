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
        username=driver.find_element_by_xpath("//input[@id='username']").send_keys("alvicustomer@gmail.com")
        password=driver.find_element_by_xpath("//input[@id='password']").send_keys("Vn!@34675634")
        rem=driver.find_element_by_xpath("//input[@id='rememberme']").click()
        log=driver.find_element_by_xpath("//button[@name='login']").click()
        driver.implicitly_wait(3)
        order=driver.find_element_by_xpath("//*[@id='post-12']/div/div/nav/ul/li[2]/a").click()
        browseprp = driver.find_element_by_xpath("//a[@class='woocommerce-Button button']").click()
        demoprodu=driver.find_element_by_xpath("//*[@id='main']/ul/li[2]/a/h2").click()
        addcart=driver.find_element_by_xpath("//button[@name='add-to-cart']").click()
        vwcart=driver.find_element_by_xpath("//*[@id='main']/div[1]/div/a").click()
        apply=driver.find_element_by_xpath("//input[@id='coupon_code']").send_keys("DEMO_COUPON")
        btn=driver.find_element_by_xpath("//button[@name='apply_coupon']").click()
        checkout=driver.find_element_by_xpath("//a[@class='checkout-button button alt wc-forward']").click()

        fname=driver.find_element_by_xpath("//input[@id='billing_first_name']").send_keys("alvi")
        lname=driver.find_element_by_xpath("//input[@id='billing_last_name']").send_keys("tazwar")
        selectcntry=driver.find_element_by_xpath("//*[@id='select2-billing_country-container']").click()
        bd=driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[19]").click()
        #billadd=driver.find_element_by_xpath("//input[@id='billing_address_1']").send_keys("azimpur")
        #city=driver.find_element_by_xpath("//input[@id='billing_city']").send_keys("dhaka")
        driver.find_element_by_xpath("//span[@class='select2-selection__placeholder']").click()
        billstate=driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[13]").click()
        postcode=driver.find_element_by_xpath("//input[@id='billing_postcode']").send_keys("1205")
        #placeorder=driver.find_element_by_xpath("//button[@id='place_order']").click()









        time.sleep(20)
object=Customer()
object.test()
