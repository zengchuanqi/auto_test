import unittest
from comment.HTMLTestRunner_cn import HTMLTestRunner


filepath = r'E:\hugewarts\web_auto\case'
rule = 'test_login_ddt.py'
report_path = 'report\\'+'result.html'
fp = open(report_path,'wb')
discorve = unittest.defaultTestLoader.discover(filepath, rule)
print(discorve)
runner = HTMLTestRunner(fp,title= '报告标题', description='报告描述')
runner.run(discorve)