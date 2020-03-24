from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self,driver):
        self.driver = driver
        # print('这是Base.driver%s' % self.driver)

    def find_Element(self, loctor):
        '''查找元素'''
        # try:
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loctor))
        return element
        # except:
        #     return False
    def sendkeys(self,loctor,text):
        '''发送数据'''
        self.find_Element(loctor).send_keys(text)

    def z_click(self,loctor):
        '''点击'''
        self.find_Element(loctor).click()

    def is_element_exit(self,loctor):
        '''查找元素是否存在'''
        try:
            self.find_Element(loctor)
            return True
        except:
            return False

    def is_title(self,title):
        '''查找页面标题是否符合期望值   返回布尔制'''
        result = WebDriverWait(self.driver,10).until(EC.title_is(title))
        return result

    def is_title_contains(self,title):
        '''查找页面标题是否包含期望值  返回布尔制'''
        try:
            result = WebDriverWait(self.driver,10).until(EC.title_is(title))
            return True

        except:
            return False

    def find_element_new(self,lot):
        '''查找元素对象'''
        ele =  WebDriverWait(self.driver,10).until(EC.presence_of_element_located(lot))
        return ele

    def get_text(self,lot):
        ele = self.find_element_new(lot)
        return ele

    def select_by_index(self,locatot,index=0):
        ele = self.find_element_new(locatot)
        Select(ele).select_by_index(index)


    def select_by_value(self,locatot,value):
        ele = self.find_element_new(locatot)
        Select(ele).select_by_value(value)

    def select_by_text(self, locatot, text):
        ele = self.find_element_new(locatot)
        Select(ele).select_by_visible_text(text)

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = self.find_element_new(locator)
        # self.driver.execute_script('arguments[0].removeAttribute(argument[1])', target)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # sleep(10)

    def js_scrool_end(self,x=0):
        '''滚动到底部'''         #document.body.scrollHeight
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)





if __name__ == "__main__":
    driver =webdriver.Chrome()
    driver.get('https://passport.bilibili.com/login')
    # driver.get('https://www.baidu.com')
    # res = EC.title_contains('百度一')(driver)
    # print(res)
    dx = Base(driver)
    locaor1 = (By.ID, 'login-username')
    ele = dx.find_element_new(locaor1)
    ele.send_keys('123')
    # locaor1 = (By.ID, 'login-username')
    # locaor2 = (By.ID, 'login-passwd')
    # locaor1 = (By.CSS_SELECTOR, '#login-username')
    # locaor2 = (By.XPATH, "//* [@id='login-passwd']")
    # dx.sendkeys(locaor1,'17872301006')
    # dx.sendkeys(locaor2,'123456')
