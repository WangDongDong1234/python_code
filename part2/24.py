a=5
b=2
print(a+b)
print(a.__add__(b))

class Myadd:
    def __init__(self,s):
        self.s=s

    def __add__(self, other):
        return self.s.count("*")+other.s.count("*")

obj1=Myadd("**22211**999**")
obj2=Myadd("**")
print(obj1+obj2)