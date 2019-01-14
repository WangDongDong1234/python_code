class A:
    name = "中国"
    age=12

    @classmethod
    def fun(cls):
        cls.age
        print(cls.age)#这里答应的是13，因为cls是接受的B的类内存空间地址

    def gun(self):#这里self是B实例化的对象，仍然可以子类空间的任意值
        print(self)

    @staticmethod
    def fu():
        print("静态方法")

class B(A):
    age=13
    pass

b1=B()
b1.fu()

