from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url_cookie = 'https://orteil.dashnet.org/cookieclicker/'
timeout = time.time() + 60*5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)

driver.get(url=url_cookie)


consent = driver.find_element(By.CLASS_NAME, value='fc-button')
consent.click()
time.sleep(5)
language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()
time.sleep(10)




def made_cookies():
    cookie = driver.find_element(By.ID, value='bigCookie')
    
    start = time.time()
    end = 0
    buyout = []
    for x in range(1):
        while end - start < 5:
           
            end = time.time()
            cookie.click()
       
        affordable = driver.find_elements(By.CSS_SELECTOR, value='.unlocked ')

        try:
            upgrade = driver.find_element(By.XPATH, value='// *[ @ id = "upgrade0"]')
            print(upgrade)
            upgrade.click()

        except:
            pass
        money = int(driver.find_element(By.ID, value='cookies').text.split()[0].replace(',', ''))
        
        while True:
            buyout = [int(_.text.split('\n')[1].replace(',', '')) for _ in affordable]
            looking_for = max(buyout)
            looking_for = buyout.index(looking_for)
            if money < max(buyout):
                buyout.pop(looking_for)
                affordable.pop(looking_for)
            else:
                break

        
        affordable[looking_for].click()


while time.time() - timeout <= 0:
    made_cookies()


