import urllib.request
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class ConstClass:
    def __init__(self):
        const_keys = ['chrome_driver_path', 'chrome_home', 'search_input', 'search_button', 'div_vector', 'title', 'explane']
        const_file = open('./const.txt', 'r', encoding='UTF-8')
        const_list = const_file.readlines()
        for const in const_list:
            const_key_val = const.split('=')
            if len(const_key_val) != 2:
                raise ValueError('定数ファイル定義エラー')
                exit()
            key = const.split('=')[0]
            val = const.split('=')[1]
            if key in const_keys:
                setattr(self, key, val)
            else:
                raise ValueError('定数ファイル定義エラー')
                exit()

class CommonConstClass:
    CHROME_DRIVER_PATH = './chromedriver_win32/chromedriver.exe'
    CHROME_HOME = 'https://www.google.com/'
    def get_driver (self):
        return self.CHROME_DRIVER_PATH
    
    def get_chrome_home (self):
        return self.CHROME_HOME

class GoogleHomeTagConst: 
    SEARCH_INPUT = 'gLFyf.gsfi'
    SEARCH_BUTTON = 'gNO89b'

    def get_search_input (self):
        return self.SEARCH_INPUT
    
    def get_search_button (self):
        return self.SEARCH_BUTTON

class GoogleSearchListTagConst:
    SEARCH_RESULT_AREA = 'jtfYYd'
    TITLE = 'yuRUbf'

print('引数チェック')
args = sys.argv
if len(args) == 1:
    print('引数不正')
    exit()
else:
    print(args[1])
print('引数チェック終了')

const = CommonConstClass()
chrome_driver = const.get_driver()
chrome_home = const.get_chrome_home()
print(chrome_driver)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

word = args[1]
chrome_service = Service(executable_path=chrome_driver)
chrome = webdriver.Chrome(service=chrome_service, options=options)
chrome.get(chrome_home)

chrome.find_element(by=By.CLASS_NAME, value="gLFyf.gsfi").send_keys(word)
chrome.find_element(by=By.CLASS_NAME, value="gNO89b").submit()

time.sleep(5)

div_vector = chrome.find_elements(by=By.CLASS_NAME, value="jtfYYd")
file = open('./result.csv', 'w', encoding='UTF-8')
file.write("タイトル,URL,説明\n")
for num,_ in enumerate(div_vector):
    href = div_vector[num].find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    title = div_vector[num].find_element(by=By.CLASS_NAME, value="LC20lb.MBeuO.DKV0Md").text
    explane = div_vector[num].find_element(by=By.CLASS_NAME, value="VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf").text
    file.write(title + "," + href + "," + explane + "\n")
file.close()
chrome.close()
exit()

