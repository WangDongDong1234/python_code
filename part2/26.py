# class B:
#     def __getitem__(self, item):
#         print("执行我了",item)
#         return "bbb"
#
#     def __setitem__(self, key, value):
#         print(key,value)
#
# b=B()
# r=b["a"]
# print(r)
# b["b"]="B"


# class C:
#     def __getitem__(self, item):
#         return getattr(self,item)
#
#     def __setitem__(self, key, value):
#         setattr(self,key,value)
#
#     def __delitem__(self, key):
#         delattr(self,key)
#
# c=C()
# c['wdd']='王冬冬'
# print(c['wdd'])
# print(c.wdd)#体现了反射，使用反射技术实现了
# del c['wdd']


class D:
    def __init__(self,lst):
        self.lst=lst

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key]=value

    def __delitem__(self, key):
        self.lst.pop(key)

d=D([11,22,"aa","cc"])
print(d[0])
d[3]="王者"
del d[2]
print(d.lst)#[11, 22, '王者']