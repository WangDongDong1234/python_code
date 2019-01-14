class A:
    def __call__(self, *args, **kwargs):
        print("执行了__call__方法")

a=A()
a()#相当于调用了__call__方法
A()()#相当于调用__calll__方法

class B:
    def __init__(self,cls):
        print("在实例化A之前做一些事")
        self.a=cls()
        self.a()
        print("在实例化A之后做一些事")

B(A)#B实例化的时候传入一个A  self.a就相当于实例化了一个对象，self.a()就相当于执行了__call__方法