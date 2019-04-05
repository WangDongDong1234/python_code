class Person:
    __mind="有思想"
    animal="高级动物"
    faith="有信仰"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def work(self):
        print("人都会工作")



p=Person("wdd",18)
print(getattr(p,"name"))
import sys
print(sys.modules)