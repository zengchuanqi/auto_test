from comment.base import Base


class AddBug:
    def __init__(self,driver):
        self.driver = driver
        self.dx = Base(self.driver)


