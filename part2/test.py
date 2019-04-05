# class A:
#     name="中国"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def fun(self):
#         self.name="美国"
#         print(self.name)
#
# a=A("wdd",18)
# a.fun()
# print(A.name)

# list=[1,2,3]
# list.pop(1)
# print(list)
import time
print(time.time())
print(time.localtime())
print(time.strftime("%y-%m-%d",time.localtime()))
t=time.strftime("%y-%m-%d  %H:%M:%S",time.localtime())
m=time.strptime(t,"%y-%m-%d  %H:%M:%S")
print(m)

