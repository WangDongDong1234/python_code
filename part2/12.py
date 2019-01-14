class Person:
    def __init__(self,name):
        self.name=name


    #属性
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new):
        if type(new) is int:
            self.__age=new
        else:
            print("age")

    @age.deleter
    def age(self):
        del self.__age
p1=Person("wdd")
p1.age=30
print(p1.__dict__)
