class B:
    __money=10000
    pass

#私有静态字段
class A:
    name="alex"
    __age=25#内存中存放和静态变量的区别  _A__age
    def func(self):
        #print(self.__money)#不能
        print(self.__age)
        print(A.__age)
        print("func")


a=A()
#print(a.__age)#不能调用
#print(A.__age)#不能调用
# a.func()
print(A.__dict__)
