#
#
# fp = open('1.txt','r')
# a = fp.readline()
# print(a)
# fp.close()
#
#
# fp = open('1.txt','a') # a是追加
# fp.write('456')
# fp.close()

# with open('1.txt','r')as fp:
#     content = fp.read()
#     print(content)
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from comment.base import Base

wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('https://www.cnblogs.com/yoyoketang/')
sleep(5)
# wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# sleep(5)
# wd.execute_script('window.scrollTo(0,0)')

dx = Base(wd)
dx.js_scrool_end()
# print('*'*50)
# lot2 = (By.ID,'author')
# ele = dx.find_element_new(lot2)
# ele = wd.find_element_by_css_selector('body > section > div.content-wrap > div > div.pagination > ul > li:nth-child(3) > a')
# ele.send_keys('123')
# print(ele.text)