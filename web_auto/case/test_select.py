from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from comment.base import Base

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
dx = Base(driver)
locator1 = (By.LINK_TEXT,'设置')
element = dx.find_Element(locator1)
'''
move_to_element讲鼠标移动到元素
ActionChains首字母大写，说明是个类，ActionChains(driver)实例化类
move_to_element 移动到要查找的元素对象
perform 执行
'''
ActionChains(driver).move_to_element(element).perform()
locator2 = (By.LINK_TEXT,'搜索设置')
# dx.click(locator2)
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator2))
# dx.find_element(locator2).click()
element.click()
print('*'*50)
locator3 = (By.NAME,'NR')
ele = dx.find_element_new(locator3)
# ele = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator3),(driver))
# ele = dx.find_element(locator3)
'''
Select是一个选择类，ele是元素对象，
'''
Select(ele).select_by_visible_text("每页显示50条")
# Select(ele).select_by_index(2)
res= ele.is_selected()
print(res)
'''
radio选择框
'''
driver.get('http://cdn1.python3.vip/files/selenium/test2.html')
#ele = driver.find_element(By.ID,'s_radio')
# lot4 = (By.CSS_SELECTOR,'#s_radio > input[type=radio]:nth-child(1)')
ele = driver.find_element(By.CSS_SELECTOR,'#s_radio > input[type=radio]:nth-child(1)')
# dx.find_element(lot4).click()
# ele = driver.find_element_by_css_selector('#s_radio > input[type=radio]:nth-child(1)')
ele.click()
# print(ele.text)


'''
checkbox框
'''
ele = driver.find_elements(By.CSS_SELECTOR, '#s_checkbox [checked="checked"]')
for i in ele:
    i.click()
# CheckBox多选
ele = driver.find_element(By.CSS_SELECTOR,'#s_checkbox [value="小雷老师"]')
# print(ele)
ele.click()
'''
查看ele是否被选中
'''
print(ele.is_selected())
driver.find_element(By.CSS_SELECTOR,'#s_checkbox [value="小江老师"]').click()

'''
select多选框
'''
# print(ele.text)
select = Select(driver.find_element_by_id("ss_multi"))

# 清除所有 已经选中 的选项
select.deselect_all()

# 选择小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
