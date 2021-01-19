from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://google.com.br")

print(driver.current_url)
print(driver.title)

element = driver.find_element_by_name("q")
element.click()
element.send_keys("hello world")
element.submit()
sleep(3)

assert driver.title == "hello world - Pesquisa Google"

driver.close()