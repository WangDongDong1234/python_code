class A:
    company_name="老男孩" #静态变量（静态字段)
    __iphone="13327790127"#私有静态变量（私有静态字段）

    def __init__(self,name,age):#普通方法(构造方法)
        self.name=name  #对象属性（普通字段）
        self.__age=age  #私有对象属性（私有普通字段）

    def func1(self): #普通方法
        pass

    def __func(self):#私有方法
        pass

    @classmethod
    def class_func(cls):#只能类名调用（对象调用，传给cls参数的也是该对象的所属类）
        """定义类方法，至少有一个cls参数"""
        print("类方法")

    @staticmethod
    def static_func():
        """定义静态方法，无默认参数"""
        print("静态方法")

    #属性
    @property
    def age(self):#让外部可以获得类中的私有静态属性
        return self.__age

    @age.setter
    def age(self,new_value):#在外部修改类中的私有静态属性
        self.__age=new_value

    @age.deleter#在外部删除类中私有静态属性
    def age(self):
        del self.__age

a1=A("wdd",25)
print(a1.age)#查看私有静态属性
a1.age=26#修改私有静态属性
print(a1.age)
print(a1.__dict__)
del a1.age#删除私有静态属性
print(a1.__dict__)