class Manager:
    OPERATE_DIC=[("创建学生账号","create_student"),("创建课程","create_course"),("查看学生信息","check_student_info")]
    def __init__(self,name):
        self.name=name
    def create_student(self):
        print("创建学生账号")
    def create_course(self):
        print("创建课程")
    def check_student_info(self):
        print("查看学生信息")
class Student:
    OPERATE_DIC = [("查询课程", "check_course"),("选择课程", "chose_course"),("查看已选择课程", "choosed_course")]
    def __init__(self,name):
        self.name=name
    def check_course(self):
        print("查询课程")
    def chose_course(self):
        print("选择课程")
    def choosed_course(self):
        print("查看已选择课程")
def login():
    username=input("use")
    password=input("pas")
    with open("data.txt",mode="r",encoding="UTF_8") as f:
        for line in f:
            list=line.strip().split("|")
            if username==list[0] and password==list[1]:
                print("登陆成功")
                return list[0],list[2]
import sys
def main():
    username,id=login()
    print(username,id)
    myfile=sys.modules['__main__']
    cls=getattr(myfile,id)#根据id得到类对象
    obj=cls(username)#创建实例
    operation=getattr(obj,"OPERATE_DIC")
    while True:
        for index,item in enumerate(operation,1):
            print(index,item[0])
        select=int(input("请选择"))
        select_item=operation[select-1]
        getattr(obj,select_item[1])()

main()