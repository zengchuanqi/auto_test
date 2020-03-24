import os


curpath = os.path.realpath(__file__)
uppath = os.path.dirname(os.path.realpath(__file__))

print(curpath)
print(uppath)
uppath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(uppath)
filepath = os.path.join(uppath,'comment','sheel.xls')
print(filepath)
