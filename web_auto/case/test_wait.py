from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# def find_element(wd, loctor):
#     element = WebDriverWait(wd, 10).until(lambda x: x.find_element(*loctor))
#     return element

wd = webdriver.Chrome()
wd.get('https://passport.bilibili.com/login')
locaor1 = (By.ID,'login-username')
locaor2 = (By.ID,'login-passwd')


ele = WebDriverWait(wd,10).until(EC.presence_of_element_located(locaor1))
ele.send_keys('17872301006')
wd.find_element(By.ID, 'login-passwd').send_keys('123456')
# find_element(wd,locaor1).send_keys('17872301006')
# find_element(wd,locaor2).send_keys('123456')
# start_time = time.time()
# wd.implicitly_wait(5)
# wd.get('https://passport.bilibili.com/login')
# find_element(wd,'login-username')
element = wd.find_element_by_id('login-username')
print(element.is_displayed())
# element.send_keys('17872301006')
#
# element = WebDriverWait(wd,10).until(lambda x:x.find_element(By.id'login-passwd'))
# # id 为 1 的元素 就是第一个搜索结果
# element = wd.find_element_by_id('login-passwd')
# element.send_keys('123456')
# print(element.text)
# end_time = time.time()
# # 打印出 第一个搜索结果的文本字符串
# print (end_time-start_time)
