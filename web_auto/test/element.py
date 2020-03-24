from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from comment.base import Base

wd = webdriver.Chrome()
dx = Base(wd)
dx.driver.get('http://www.5nj.com/index.php?m=vod-list-id-1-pg-1-order--by-time-class--year--letter--area--lang-.html')
        # self.driver.get('https://passport.bilibili.com/login')
#lot1 = (By.CSS_SELECTOR,'#mainContent > div > div:nth-child(12) > div:nth-child(17) > a')
lot2 = (By.CSS_SELECTOR,'body > div.main.kongbai > div.page.mb.clearfix > a:nth-child(14)')
# ele = wd.find_element(By.ID,'kw')
# ele.send_keys('123')
# ele = wd.find_element(*lot)
# sleep(10)
dx.js_focus_element(lot2)
# sleep(10)
# dx.z_click(lot2)
# sleep(2)
# ele = dx.find_element_new(lot2)
# print(ele.text)
# sleep(1)
#ele = WebDriverWait(dx.driver,10).until(EC.element_to_be_clickable(lot2))
ele =dx.find_element_new(lot2)
print(ele.text)
ele.click()

# print('*'*50)