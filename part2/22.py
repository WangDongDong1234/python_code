# class A:
#     pass
#
# a=A()
# print(type(a))#<class '__main__.A'>
# print(type(A))#<class 'type'>

# class Person:
#     role="huaman"
#     print(role)#这个会执行的
#     #print(Person.role)#不行的原因是，先申请的内存空间，然后将类里面的内容加载进去，最后贴上类标签
#     def __init__(self):
#         pass
#
#     def pay(self):
#         print("支付")
# print(Person.__dict__)
# p=Person()
# print(Person.pay)
# print(p.pay)


class A:
    def fun(self):
        print("A")

class B(A):
    def fun(self):
        super().fun()
        print("B")

class C(A):
    def fun(self):
        super().fun()
        print("C")

class D(B,C):
    def fun(self):
        super().fun()
        print("D")

d=D()
d.fun()#acbd

class Circle:
    def __init__(self,r):
        self.__r=r
        #self.area=3.14*self.r**2  #在这里初始化的话，area就被固定住了，以后改了r这里的面积不会改
    @property
    def area(self):#这个方法计算结果本身就是一个属性，但是这个属性会随着这个类/对象的一些基础变量而改变
        return 3.14*self.__r**2
    @area.setter
    def area(self,new_value):
        self.area=new_value


c=Circle(5)
print(c.area)