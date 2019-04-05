class Manager:
    OPERATION=[("创建学生账号","create_student"),("创建课程","create_course"),("查看学生信息","check_info")]
    def __init__(self,name):
        self.name=name

    def create_student(self):
        print("成功创建学生账号")

    def create_course(self):
        print("成功创建课程")

    def check_info(self):
        print("成功查看学生信息")

class Student:
    OPERATION=[("查询课程","check_course"),("选择课程","select_course"),("查询已选择课程","choosed_course")]
    def __init__(self,name):
        self.name=name

    def check_course(self):
        print("成功查看课程")
    def select_course(self):
        print("成功选择课程")
    def choosed_course(self):
        print("成功查询已选择课程")

def login():
    username=input().strip()
    password=input().strip()
    with open("data",mode="r",encoding="UTF_8") as f:
        for line in f:
            lst=line.strip().split(",")
            if username==lst[0] and password==lst[1]:
                return lst[0],lst[2]
import sys
def main():
    username,kind=login()
    print(username,kind)
    myfile=sys.modules["__main__"]
    cls=getattr(myfile,kind)
    obj=cls(username)
    operations=getattr(cls,"OPERATION")
    while 1:
        for index, item in enumerate(operations, 1):
            print(index, item)
        num=int(input("请选择"))
        getattr(obj,operations[num-1][1])()


main()