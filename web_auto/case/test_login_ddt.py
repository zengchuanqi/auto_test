from selenium import webdriver

from comment.base import Base
import unittest

from page.baidu_page import BaiDu
import ddt
from comment.test_excel import Read_Ex

r = Read_Ex()
filepath = r"E:\hugewarts\web_auto\comment\sheel.xls"
date=r.read_excel(filepath)
print(date)

# date = [
#         {'username':'17872301006','password':'zct12358','expe':False},
#         {'username':'17872301006','password':'zct123580','expe':'普罗米修斯zct'},
#         {'username':'17872301006','password':'zct1','expe':False}
#         ]
@ddt.ddt
class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('cls开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('cls结束')


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.bd = BaiDu(self.driver)
        print('setup开始')

    def tearDown(self) -> None:

        print('self结束')
        self.driver.quit()

    def test_01(self):
        print('test_01')
        self.bd.get_url()
        self.bd.input_username('17872301006')
        self.bd.input_pwd('zct123580')
        self.bd.click_submit()
        result = self.bd.confirm()
        assert result=='普罗米修斯zct'

    def test_02(self):
        print('test_02')
        self.bd.get_url()
        self.bd.input_username('17872301006')
        self.bd.input_pwd('zct12358')
        self.bd.click_submit()
        result = self.bd.confirm()
        self.assertTrue(result=='False')

    @ddt.data(*date)
    def test_03(self,data):
        self.bd.login(data['username'],data['password'],data['expe'])
