import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from page.baidu_page import BaiDu


class UpDown(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('cls开始')

    @classmethod
    def tearDownClass(cls) -> None:

        print('cls结束')
        # cls.driver.quit()

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.bd = BaiDu(self.driver)
        self.driver.get('https://www.baidu.com/')
        print('self开始')

    def tearDown(self) -> None:
        print('self结束')
        self.driver.quit()

    def test_01(self):
        print('test_01开始')
        sleep(3)
        # self.bd.input_username('17872301006')
        # self.bd.input_pwd('zct123580')
        # self.bd.click_submit()
        # self.bd.confirm()


    def test_02(self):
        print('test_02开始')
        lot = (By.ID,'kw')
        self.bd.sendkeys(lot,'123')
        sleep(3)