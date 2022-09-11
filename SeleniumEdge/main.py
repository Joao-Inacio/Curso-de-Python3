from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Edge(
    executable_path='C:\Curso-de-Python3\SeleniumEdge\edgedriver\msedgedriver.exe'
)
browser.get('https://google.com')
sleep(10)
browser.find_element(By.NAME, 'q').send_keys('Python')
sleep(10)
browser.find_element(By.NAME, 'btnK').click()
sleep(20)
browser.quit()
