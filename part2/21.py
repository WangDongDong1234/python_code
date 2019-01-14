# l=["a","b","c"]
# #it=iter(l)
# it=l.__iter__()
# #next=next(it)
# next=it.__next__()
# print(next)

# class Mylist:
#     def __init__(self):
#         self.list=[1,2,3]
#
#     def __len__(self):
#         return len(self.list)
#
# l=Mylist()
# print(len(l))

# class Single:
#     __ISINCTANCE=None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__ISINCTANCE:
#             cls.__ISINCTANCE=object.__new__(cls)
#             print("在new方法里",cls.__ISINCTANCE)
#         return cls.__ISINCTANCE
#
#     def __init__(self):
#         print("在initial方法里",self)
#
# s1=Single()
# print("创建第二个对象")
# s2=Single()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        print("执行__str__方法")
        return "学生的名字是%s,年龄是%s" %(self.name,self.age)

s1=Student("wdd",25)
print("学生：%s" %s1)