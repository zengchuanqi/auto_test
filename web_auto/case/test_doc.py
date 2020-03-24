import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        print('用例执行前')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('用例执行后')
    def setUp(self):
        print('action')
    def tearDown(self) -> None:
        print('end')
        self.driver.delete_all_cookies() #删除cookie
    def is_alter_exit(self):
        try:
            alter = self.driver.switch_to.alert
            text = alter.text
            alter.accept()
            return text
        except:
            return 'NO'

    def testAdd(self):  # test method names begin with 'test'
        '''add'''
        self.assertEqual((1 + 2), 3)
        print('add')
        # self.a ='123'
        # self.b = '1234'
        # self.assertEqual(self.a,self.b)
        # self.assertNotIn(self.a,self.b)
        self.assertEqual(0 + 1, 1)
        text = self.is_alter_exit()
        print(text)
        assert 1==2

    def testMultiply(self):
        '''mul'''
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
        print('mul')





