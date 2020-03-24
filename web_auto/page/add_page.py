from selenium import webdriver
from selenium.webdriver.common.by import By

from comment.base import Base


class Search(Base):

    lot1 = (By.CSS_SELECTOR,'[title="秀人网200G高清美图下载+美图录图片下载器-福利吧"]')
    lot2 = (By.ID,'author')
    lot3 = (By.ID,'email')
    lot4 = (By.ID, 'url')
    def enter(self):
        self.driver.get('http://fulibus.net/')
        self.z_click(self.lot1)
        for handle in self.driver.window_handles:
            # 先切换到该窗口
            self.driver.switch_to.window(handle)
            # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
            if '人' in self.driver.title:
                # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
                break


    def add_comment(self):
        ele = self.find_element_new(self.lot2)
        print(ele.text)
        # self.sendkeys(self.lot1, username)

        self.sendkeys(self.lot2,'zengshuai')
        self.sendkeys(self.lot3,'1501327456@qq.com')
        self.sendkeys(self.lot4,'123456')

if __name__ == '__main__':
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    dxsearch = Search(wd)
    dxsearch.enter()
    dxsearch.add_comment()

