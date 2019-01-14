class Parent:
    def func(self):
        print("in Pratent func")

    def __init__(self):
        self.func()

class Son(Parent):
    def func(self):
        print("in Son func")

s1=Son()#in Son func


class A:
    name=[]

p1=A()
p2=A()
p1.name.append(1)
print(p1.name)#[1]
print(p2.name)#[1]
print(A.name)#[1]