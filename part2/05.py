# class Animal:
#     breath="有呼吸"
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age=age
#
#     def eat(self):
#         print("进食")
#
# class Person(Animal):
#     pass


#继承的子类
#1 子类的类名可以访问父类的所有内容
# print(Person.breath)
# Person.eat(11)
#2 子类实例化的对象可以访问父类的所有内容
# p1=Person("wdd","man","25")
# print(p1.breath)
# p1.eat()
# print(p1.__dict__)


print("-------------------------------------------------------")
class Animal:
    breath="有呼吸"
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

    def eat(self):
        print("进食")

class Bird(Animal):
    def __init__(self,name,sex,age,wing):
        #Animal.__init__(self,name,sex,age)
        super().__init__(name,sex,age)
        self.wing=wing

b1=Bird("鹦鹉","公","23","会飞")
print(b1.__dict__)