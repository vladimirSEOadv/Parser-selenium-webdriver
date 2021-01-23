###Инициализация
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #Библиотека для установки пауз между запросами
from fake_useragent import UserAgent ##https://pypi.org/project/fake-useragent/ - библиотека с юзерагентами
from My_input import vvod #тест подгрузки ввода из другого файла
import pickle


#Опции

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
# options.add_argument("--proxy-server")


driver = webdriver.Chrome(executable_path=r"F:\Programirovanie\Python\Parser selenium webdriver\webdriver chrome 87.0.4280\chromedriver.exe", options=options)
url = "https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html"


## Рабочая область
try:
    driver.get(url=url)
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()