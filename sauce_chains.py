from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class Test_Sauce:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
       
    
    def test_invalid_login(self):
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"1")
        actions.send_keys_to_element(passwordInput,"1")
        actions.perform()
        # usernameInput.send_keys("1")
        # passwordInput.send_keys("1")
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"test sonucu1:{testResult}")
   
    def test_null_userName(self):
        self.driver.get("https://www.saucedemo.com/")
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        #passwordInput.send_keys()
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult1=errorMessage.text=="Epic sadface: Username is required"
        print(f"test sonucu2:{testResult1}")
    
    def test_null_password(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.perform()
        #usernameInput.send_keys()
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult2=errorMessage.text=="Epic sadface: Password is required"
        print(f"test sonucu3:{testResult2}")
    
    def test_locked_user(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"locked_out_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # usernameInput.send_keys("locked_out_user")
        # passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult4=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"test sonucu4:{testResult4}")
    
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        baslık=self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")
        testResult5=baslık.text=="Swag Labs"
        print(f"test sonucu5:{testResult5}")
    
    def test_add_Product(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        addToCart=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        addToCart.click()
        check=self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a/span")
        testResult6=check.text=="1"
        print(f"test sonucu6:{testResult6}")
    
    def test_remove_Product(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(2)
        remove=self.driver.find_element(By.ID,"remove-sauce-labs-onesie")
        remove.click()
        check1=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        testResult7=check1.text=="Add to cart"
        print(f"test sonucu7:{testResult7}")


testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_null_userName()
testClass.test_null_password()
testClass.test_locked_user()
testClass.test_valid_login()
testClass.test_add_Product()
testClass.test_remove_Product()



    