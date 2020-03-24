# EC是 expected_conditions的别名
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
res = EC.title_is('百度一下，你就知道')(driver)
assert res == True
res = EC.title_contains('百度一')(driver)
print(res)
