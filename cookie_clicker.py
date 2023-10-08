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

# consent = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/')
consent = driver.find_element(By.CLASS_NAME, value='fc-button')
consent.click()
time.sleep(5)
language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()
time.sleep(10)

# print(cookies)=


def made_cookies():
    cookie = driver.find_element(By.ID, value='bigCookie')
    # cookies = int(driver.find_element(By.ID, value='cookies').text.split()[0])
    # price0 = int(driver.find_element(By.ID, value='productPrice0').text)
    # price1 = int(driver.find_element(By.ID, value='productPrice0').text)
    # price2 = int(driver.find_element(By.ID, value='productPrice0').text)
    # price3 = int(driver.find_element(By.ID, value='productPrice0').text)
    # price4 = int(driver.find_element(By.ID, value='productPrice0').text)
    # price = min(price4, price3, price2, price1, price0)
    start = time.time()
    end = 0
    buyout = []
    for x in range(1):
        while end - start < 5:
            # print(price, cookies)
            end = time.time()
            cookie.click()
        # money = int(driver.find_element(By.ID, value='cookies').text.split()[0].replace(',', ''))
        affordable = driver.find_elements(By.CSS_SELECTOR, value='.unlocked ')

        try:
            upgrade = driver.find_element(By.XPATH, value='// *[ @ id = "upgrade0"]')
            print(upgrade)
            upgrade.click()

        except:
            pass
        money = int(driver.find_element(By.ID, value='cookies').text.split()[0].replace(',', ''))
        # for _ in affordable:
        #   buyout.append(int(_.text.split('\n')[1]))
        while True:
            buyout = [int(_.text.split('\n')[1].replace(',', '')) for _ in affordable]
            looking_for = max(buyout)
            looking_for = buyout.index(looking_for)
            if money < max(buyout):
                buyout.pop(looking_for)
                affordable.pop(looking_for)
            else:
                break

        # try:
        #     print(upgrade[0].text)
        #     upgrading = [int(_.text.split('\n')[1].replace(',', '')) for _ in upgrade]
        #     looking_for_up = min(upgrading)
        #     looking_for_up = upgrading.index(looking_for_up)
        #     if min(buyout) < min(upgrading):
        #         affordable[looking_for].click()
        #     else:
        # upgrade[looking_for_up].click()
        #       except IndexError:
        #     print('Error')
        affordable[looking_for].click()


while time.time() - timeout <= 0:
    made_cookies()


