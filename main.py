from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webTest = webdriver.Chrome()

webTest.get("https://exe.ua/")
print("Page is open")

item_list = ["123", "FBSS", "привет маша", "№№", "fn66AS}="]

for item in item_list:
    try:
        search = webTest.find_element(By.XPATH, "//*[@id='search_query']")
        search.clear()
        search.send_keys(item)
        search.send_keys(Keys.ENTER)
        print(f"Поиск по запросу: {item}")
        time.sleep(0.5)  # Пауза между поисками, чтобы страница успевала подгружаться
    except Exception as e:
        print(f"Ошибка при поиске {item}: {e}")

time.sleep(2)
print("Page is close")

webTest.quit()
