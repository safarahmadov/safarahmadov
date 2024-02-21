import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window
driver.get("https://turbo.az")

WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@class="footer__makes-i" and contains(@href, "/autos?q%5Bmake%5D%5B%5D=20")]')))
search_click = driver.find_element(By.XPATH, '//a[@class="footer__makes-i" and contains(@href, "/autos?q%5Bmake%5D%5B%5D=20")]')
search_click.click()


WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q[price_to]")))
filter_click_up=driver.find_element( By.NAME, "q[price_to]")
filter_click_up.send_keys("60000")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q[price_from]")))
filter_click_down=driver.find_element(By.NAME, "q[price_from]")
filter_click_down.send_keys("55000")


WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "commit")))
search=driver.find_element(By.NAME, "commit")
search.click()

link_list=[]
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="products-i__link"]')))
selected=driver.find_elements(By.XPATH, '//a[@class="products-i__link"]')
for select in selected:
   link_list.append(select.get_attribute('href'))

names = []
prices = []

for link in link_list:
    driver.get(link)
    time.sleep(2)
    try:
        name = driver.find_element(By.XPATH, '//h1[@class="product-title"]').text
        price_element = driver.find_element(By.XPATH, '//div[@class="product-price__i product-price__i--bold"]')
        price = price_element.text
    except:
        name = ""
        price = ""
    
    names.append(name)
    prices.append(price)

# Döngü bittiğinde tüm değerleri yazdır
for i in range(len(names)):
    print(f"Name: {names[i]}, Price: {prices[i]}")