from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")

driver.maximize_window()
input = driver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")
searchButton=driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(5)
firstResult= driver.find_element(By.XPATH,"/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
firstResult.click()
courses=driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlamaio sitesinde şu an {len(courses)} tane kurs var.")
#sleep(2)
while True:
   continue


#HTML LOCATORS


#web scraping ya da data scraping sitelerden veri kazıma olarak bilinir.


