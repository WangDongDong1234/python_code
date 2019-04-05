# import sys
# sys.path.append("D:\wdd\pycharm\python_code\模块的复杂导入\glance\db")
# import models
# models.fun()

# import sys
# print(__file__)
# ret=__file__.split("/")
# basepath="/".join(ret[:-2])
# print(basepath)
# sys.path.append(basepath)
# from db import models
# models.fun()
import sys
print(__file__)
ret=__file__.split("/")
basepath="/".join(ret[:-2])
print(basepath)
sys.path.append(basepath)