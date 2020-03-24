from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from comment.base import Base


class BaiDu(Base):
    # lot = (By.CSS_SELECTOR, '#u1 > a.lb')
    lot1=(By.CSS_SELECTOR,'#u1 .lb')
    lot2=(By.CLASS_NAME,'tang-pass-footerBarULogin')
    lot3=(By.ID,'TANGRAM__PSP_10__userName')
    lot4=(By.ID,'TANGRAM__PSP_10__password')
    lot5 = (By.ID, 'TANGRAM__PSP_10__submit')
    lot6 = (By.ID,'s_username_top')
    lot7 = (By.CLASS_NAME,'pass-fgtpwd')

    def login(self,username='17872301006',pwd='zct123580',expe='普罗米修斯zct'):
        self.driver.get('https://www.baidu.com/')
        # self.driver.get('https://passport.bilibili.com/login')
        self.z_click(self.lot1)
        self.z_click(self.lot2)
        sleep(1)
        self.sendkeys(self.lot3,username)
        sleep(3)
        self.sendkeys(self.lot4,pwd)
        sleep(3)
        self.z_click(self.lot5)
        ele = self.confirm()
        print('ele=%s' % ele)
        print('expe=%s' % expe)
        assert expe==ele
        # ele = self.get_text(self.lot6)
        # assert ele.text == '普罗米修斯zct'
        # self.z_click(self.lot)

    def get_url(self,url='https://www.baidu.com/'):
        self.driver.get(url)
        self.z_click(self.lot1)
        self.z_click(self.lot2)
        sleep(1)

    def input_username(self,name):
        self.sendkeys(self.lot3, name)
        sleep(3)

    def input_pwd(self,password):
        self.sendkeys(self.lot4,password)
        sleep(5)

    def click_submit(self):
        self.z_click(self.lot5)

    def forget_pwd(self):
        self.z_click(self.lot7)

    def confirm(self):
        try:
            ele = self.get_text(self.lot6)
            return ele.text
        except:
            return 'False'
            # assert ele.text == '普罗米修斯zct'
        # except:


if __name__ == '__main__':
    wd = webdriver.Chrome()
    baidu = BaiDu(wd)
    baidu.get_url()
    baidu.input_username('17872301006')
    baidu.input_pwd('zct123580')
    baidu.click_submit()