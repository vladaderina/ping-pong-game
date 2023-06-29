import content as content
from selenium import webdriver  # импорт библиотек
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.remote.webelement import WebElement

url = "https://tutorialsninja.com/demo/index.php?route=common/home"  # записываем адрес сайта который будем запускать
service = Service(executable_path="C:\\Users\\vlada\\Desktop\\chromedriver.exe")  # тут ваш путь до chromedriver
browser = webdriver.Chrome(service=service)

fieldName = "search"
testNameValue = "Samsung SyncMaster 941BW"

buttonSend = '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]'
buttonSend2 = 'shopping cart'

try:
    browser.get(url)  # браузер открывает ссылку
    fin = browser.find_element(By.NAME, fieldName)  # ищем элемент по имени
    fin.send_keys(testNameValue)
    time.sleep(1)
    fin.send_keys(Keys.RETURN)
    time.sleep(1)
    button = browser.find_element(By.XPATH, buttonSend)  # ищем элемент по имени
    button.click()
    time.sleep(1)
    button2 = browser.find_element(By.LINK_TEXT, buttonSend2)  # ищем элемент по имени
    button2.click()
    print("Успешный успех!")
    time.sleep(10)
    browser.quit()  # браузер завершает свою работу
except Exception as ex:
    print(ex)  # в случае ошибки ошибка выводится в консоль
    browser.quit()
