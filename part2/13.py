class A:
    def fun1(self):
        print(self)

    @classmethod
    def fun2(cls):
        print(cls)

a1=A()
a1.fun1()#对象实例化的地址  <__main__.A object at 0x0000007F1457C048>
A.fun1(a1)#和10行效果等价<__main__.A object at 0x0000007F1457C048>
A.fun2()#通过类名调用的方法，类方法中的第一个参数是cls,python自动将类空间传给cls
        #<class '__main__.A'>
a1.fun2()#对象调用类方法，cls得到的是类本身
         #<class '__main__.A'>这是类本身