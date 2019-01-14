# class Goods:
#     __discount=0.8
#     def __init__(self,price):
#         self.__price=price
#
#     @property#注意用了这个price必须设置为私有
#     def price(self):
#         return self.__price*Goods.__discount
#     @classmethod
#     def change_discount(cls,new_discount):
#         #self.__discount=new_discount#这个是单个更改
#         cls.__discount=new_discount#这样子的是整体更改
#
# apple=Goods(10)
# banna=Goods(15)
# print(apple.price,banna.price)
# apple.change_discount(1)
# print(apple.price,banna.price)

class Person:
    @staticmethod
    def login():
        pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Manager(Person):
    pass