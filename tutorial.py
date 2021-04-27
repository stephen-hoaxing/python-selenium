from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
link = driver.find_element_by_link_text("Tutorials")
link.click()
driver.back()
driver.forward()

try:
    element = WebDriverWait(driver, 10000).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Machine Learning With Python"))
    )
    element.click()

    button = WebDriverWait(driver, 10000).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    button.click()
finally:
	print("OK")