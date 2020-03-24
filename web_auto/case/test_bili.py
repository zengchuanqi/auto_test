import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dirver = webdriver.Chrome()
        cls.dirver.implicitly_wait(20)
    def setUp(self) -> None:
        self.dirver.get('https://www.bilibili.com/')

    def test_login(self):
        '''登录'''
        self.dirver.find_element_by_css_selector('.logout-face').click()
    @ classmethod
    def tearDownClass(cls) -> None:
        cls.dirver.quit()