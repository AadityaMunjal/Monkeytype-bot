from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import random

CHROME_DRIVER_PATH = 'C:\Program Files\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('https://monkeytype.com/')

words = driver.find_elements_by_class_name("word")

print(f'length of words: {len(words)}')
print('starting!')


for word in words:

    for i in range(len(word.text)):
        startTime = time.time()
        letter = word.text[i]
        # waiting for random secs so that it dosent know that its a BOT ;)
        # time.sleep(random.randint(1, 2) / 100)
        # pyautogui.press(letter)
        pyautogui.write(letter)
        endTime = time.time()
        print(f'Loop took {endTime - startTime}')

    pyautogui.press('space')


print('done!')


time.sleep(5)
driver.quit()
