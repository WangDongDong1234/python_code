# print(hash('abc'))

#
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __eq__(self, other):
#         if self.name==other.name and self.age==other.age:
#             return True
#         return False
#
# a=A("wdd",18)
# aa=A("wdd",18)
# print(a==aa)#True


class Employee:
    def __init__(self,name,age,sex,part):
        self.name=name
        self.age=age
        self.sex=sex
        self.part=part

    def __hash__(self):
        return hash('%s%s'%(self.name,self.sex))

    def __eq__(self, other):
        if self.name==other.name and self.sex==other.sex:
            return True

emoloyees=[]
for i in range(200):
    emoloyees.append(Employee("wdd",i,"man","python"))

for i in range(200):
    emoloyees.append(Employee("wn",i,"woman","python"))
print(len(emoloyees))
print(set(emoloyees))
print(len(set(emoloyees)))