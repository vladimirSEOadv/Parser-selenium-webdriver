###Инициализация
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from fake_useragent import UserAgent ##https://pypi.org/project/fake-useragent/ - библиотека с юзерагентами

import pickle


#Опции

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
# options.add_argument("--proxy-server")


driver = webdriver.Chrome(executable_path=r"F:\Programirovanie\Python\Parser selenium webdriver\webdriver chrome 87.0.4280\chromedriver.exe", options=options)
url = "https://www.rambler.ru/"

def rambler_mail_reg():
    driver.get(url="https://www.rambler.ru/")
    time.sleep(2)
    element1 = driver.find_element_by_class_name("rui__2FTrL")
    element1.click()
    time.sleep(5)
    driver.find_element_by_class_name("footer-0-3-47").click()  ##Клик по "Зарегистрироватся"
    time.sleep(4)
    driver.find_element_by_name("login").send_keys()
    time.sleep(4)

## Рабочая область
try:
    rambler_mail_reg()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()