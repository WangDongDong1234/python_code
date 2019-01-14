#用户知道类里面有个role，我想通过输入role,来拿到类里面的role

#类  静态属性，类方法，静态方法
class Student:
    ROLE="STUDENT"
    def __init__(self,name):
        self.name=name

    @classmethod
    def check_source(cls):
        print("查看课程")

    @staticmethod
    def login():
        print("登陆了")


#反射调用静态属性
print(Student.ROLE)
print(getattr(Student,"ROLE"))
#反射调用方法
print(getattr(Student,"check_source"))#<bound method Student.check_source of <class '__main__.Student'>>
getattr(Student,"check_source")()#执行了这个类方法
#反射调用静态方法
print(getattr(Student,"login"))

num=input(">>>")
if hasattr(Student,num):
    getattr(Student,num)()

#对象
#方法  对象属性
student=Student("wdd")
print(student.name)
print(getattr(student,"name"))
getattr(student,"login")()

#模块
import os
#os.rename("test.py","Test.py")
getattr(os,"rename")("Test.py","test.py")

#反射自己模块里的内容,找到自己当前当前文件所在的类名空间
def wahaha():
    print("哇哈哈")

def qqxin():
    print("qqxin")

import sys
print(sys.modules)
#import 相当于导入了一个模块
#模块那个导入了，那个没导入，在我的python解释器里应该记录了下来
#import sys是一个模块，这个模块的所有方法都是和python解释器相关的
#sys.modules这个方法，表示所有在当前这个python程序中导入的模块
#'__main__': <module '__main__' from 'D:/wdd/pycharm/python_code/part2/18.py'>
myfile=sys.modules['__main__']
myfile.wahaha()
getattr(myfile,"wahaha")()
