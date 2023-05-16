from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


s=Service('C:/Users/dycen/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)

scroll_vаlue = -5000
scroll_vаlue_2 = 2500
scroll_vаlue_3 = 300
scroll_by = f'window.scrollBy(0, {scroll_vаlue});'
scroll_by_2 = f'window.scrollBy(0, {scroll_vаlue_2});'
scroll_by_3 = f'window.scrollBy(0, {scroll_vаlue_3});'

driver.get("https://qahacking.guru/")
print("Сайт открыт")
driver.set_window_size(1920, 982)
time.sleep(2)
print("Проверка на наличие табов:")
tabButton_1 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[1]/a')
tabButton_2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[2]/a')
tabButton_3 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a')
tabButton_4 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[4]/a')
tabButton_5 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[5]/a')
tabButton_6 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[6]/a')

if tabButton_1 is None:
  print("Кнопка 'О нас' не найдена")
else:
 print("Кнопка 'О нас' имеется")

if tabButton_2 is None:
  print("Кнопка 'Блог Джесси' не найдена")
else:
 print("Кнопка 'Блог Джесси' имеется")

if tabButton_3 is None:
  print("Кнопка 'Магазин' не найдена")
else:
 print("Кнопка 'Магазин' имеется")

if tabButton_4 is None:
  print("Кнопка 'Советы' не найдена")
else:
 print("Кнопка 'Советы' имеется")

if tabButton_5 is None:
  print("Кнопка 'Статьи' не найдена")
else:
 print("Кнопка 'Статьи' имеется")

if tabButton_6 is None:
  print("Кнопка 'Проверь свой уровень' не найдена")
else:
 print("Кнопка 'Проверь свой уровень' имеется")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").send_keys("dycenkoviktor@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".el-button").click()
print("Осуществлена подписка на рассылку")
time.sleep(2)
driver.find_element(By.ID, "mod-rscontact-full-name-91").click()
driver.find_element(By.ID, "mod-rscontact-full-name-91").send_keys("Виктор Дыченко")
driver.find_element(By.ID, "mod-rscontact-email-91").click()
driver.find_element(By.ID, "mod-rscontact-email-91").send_keys("dycenkoviktor@gmail.com")
driver.find_element(By.ID, "mod-rscontact-mobile-phone-91").click()
driver.find_element(By.ID, "mod-rscontact-mobile-phone-91").send_keys("89255746357")
driver.find_element(By.ID, "mod-rscontact-subject-91").click()
driver.find_element(By.ID, "mod-rscontact-subject-91").send_keys("Moscow")
driver.find_element(By.ID, "mod-rscontact-submit-btn-91").click()
driver.find_element(By.ID, "mod-rscontact-submit-btn-91")
print("Форма обратной связи заполнена и отправлена")
time.sleep(2)
driver.execute_script(scroll_by)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(1) > a").click()
print("Открыта страница 'О нас'")
driver.execute_script(scroll_by_2)
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "firstName").send_keys("Виктор")
driver.find_element(By.ID, "lastName").click()
driver.find_element(By.ID, "lastName").send_keys("Дыченко")
driver.find_element(By.ID, "userEmail").click()
driver.find_element(By.ID, "userEmail").send_keys("dycenkoviktor@mail.com")
driver.find_element(By.ID, "sex-1").click()
driver.find_element(By.ID, "date").click()
driver.find_element(By.CSS_SELECTOR, ".uk-width-2-3\\@s").click()
driver.find_element(By.ID, "date").send_keys("18.10.2023")
driver.find_element(By.ID, "hobbies-checkbox-2").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
driver.execute_script(scroll_by_3)
print("Форма бронирования заполнена")
time.sleep(2)
driver.find_element(By.ID, "submit").click()
print("Форма бронирования отправлена")
time.sleep(2)
driver.close()
print("Сайт закрыт")
  
