from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/a1525/Desktop/Code/Python/Reptile/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")

search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

searchButton = driver.find_element_by_class_name("sc-e6ba31f5-3")
searchButton.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-d6aee74c-1"))
)

artictitle = driver.find_elements_by_class_name("sc-a230363e-3")
artic = open("../articleTitle.txt", "w", encoding="utf-8")
artic.truncate()

for title in artictitle:
    print(title.text, end="\n", file=artic)
artic.close()
print()

driver.close()
