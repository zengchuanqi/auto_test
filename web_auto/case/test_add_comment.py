from selenium import webdriver

from comment.base import Base
import unittest

from page.baidu_page import BaiDu
from page.login_page import Login
from page.add_page import Search


class Test_Add_Comment(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.dx_login = Login(cls.driver)
        cls.dx_add = Search(cls.driver)
        # cls.dx_login.login()
        cls.bd = BaiDu(cls.driver)
    def test_add_comment(self):
        self.dx_add.enter()
        self.dx_add.add_comment()
    def test_bd(self):
        self.bd.login()
