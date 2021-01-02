from selenium import webdriver
from pynput.keyboard import Key, Controller
import time

MY_CHROME_DRIVER_PATH = 'C:\Program Files\chromedriver.exe'
driverPath = input(
    'Enter your Chrome driver PATH. Leave empty if its: C:\Program Files\chromedriver.exe')

if driverPath == '':
    path = MY_CHROME_DRIVER_PATH
else:
    path = driverPath

keyboard = Controller()
driver = webdriver.Chrome(path)
driver.get('https://monkeytype.com/')

words = driver.find_elements_by_class_name("word")

print(f'length of words: {len(words)}')
print('starting!')


for word in words:

    for i in range(len(word.text)):
        startTime = time.time()
        letter = word.text[i]
        keyboard.type(letter)
        endTime = time.time()
        print(f'Loop took {endTime - startTime}')

    keyboard.press(Key.space)
    keyboard.release(Key.space) 


print('done!')