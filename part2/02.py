class Person:
    """类体：两部分：变量部分，方法部分"""
    mind="有思想"      #静态变量，静态字段
    animal="高级动物"  #静态变量，静态字段
    faith="有信仰"     #静态变量，静态字段

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print(self)
        print("6666")

    def work(self):#self暂时看成位置参数
        print("人都会工作%s" %self.name)

    def shop(self):
        self.love="衣服"
        print("人类可以消费")
p1=Person("wdd",18,"man")
#---------------------------------------------
#对象的角度
#类名+（）  过程：实例化的过程   类名（）这个整体叫实例化对象  然后自动执行__init__方法
ret=Person("wdd",18,"man")#产生一个对象，将这个对象理解成一个空间或者是内存地址，然后将这个内存地址给self
print(ret)#ret和self相同
#通过__init__查看对象中的所有变量,同样以字典的形式给你
print(ret.__dict__)#{'name': 'wdd', 'age': 18, 'sex': 'man'}
print(ret.__dict__['name'])#wdd
print(ret.name)#wdd  查
ret.high=175 #增
ret.sex="woman"#改
print(ret.__dict__)#{'name': 'wdd', 'age': 18, 'sex': 'woman', 'high': 175}
del ret.high#删
print(ret.__dict__)#{'name': 'wdd', 'age': 18, 'sex': 'woman'}
ret.high=188
print(ret.__dict__)#{'name': 'wdd', 'age': 18, 'sex': 'woman', 'high': 188}
print(ret.mind)#有思想
ret.work()#人都会工作
ret.shop()
print(ret.__dict__)#{'name': 'wdd', 'age': 18, 'sex': 'woman', 'high': 188, 'love': '衣服'}
del ret.mind
print(ret.__dict__)