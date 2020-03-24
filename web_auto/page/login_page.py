from selenium.webdriver.common.by import By
from comment.base import Base
from selenium import webdriver

class Login(Base):
    lot1 = (By.ID, 'login-username')
    lot2 = (By.ID, 'login-passwd')
    def login(self,username='17872301006',pwd='123456'):
        self.driver.get('https://passport.bilibili.com/login')
        self.sendkeys(self.lot1, username)
        self.sendkeys(self.lot2, pwd)
        # self.find_lement(self.lot1).send_keys('17872301006')
        # self.find_element(self.lot2).send_keys('123456')
        # self.z_click()


if __name__ == '__main__':
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    dxlogin = Login(wd)
    dxlogin.login()