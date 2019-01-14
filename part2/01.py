class Person:
    """类体：两部分：变量部分，方法部分"""
    mind="有思想"      #静态变量，静态字段
    animal="高级动物"  #静态变量，静态字段
    faith="有信仰"     #静态变量，静态字段

    def work(self):#self暂时看成位置参数
        print("人都会工作")

    def shop(self):
        print("人类可以消费")

    def fun(self):
        Person.love="wdd"



#类名的角度
      #类中的静态变量
print(Person.__dict__)#查询类中所有的内容，发现是一个字典
                    #{'__module__': '__main__', '__doc__': '类体：两部分：变量部分，方法部分', 'mind': '有思想', 'animal': '高级动物', 'faith': '有信仰', 'work': <function Person.work at 0x000000A7DF31A6A8>, 'shop': <function Person.shop at 0x000000A7DF31A9D8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
print(Person.__dict__["mind"])
      #万能的点
print(Person.mind)#查询类中的静态变量
Person.money="运用货币"#增加类中的静态变量
print(Person.__dict__)
Person.mind="有思想的高级动物"#更改类中的静态变量
print(Person.__dict__)
del Person.money#删除类中的静态变量
print(Person.__dict__)
     #操作类中的方法
Person.work(11)#11就是传进来的地址

