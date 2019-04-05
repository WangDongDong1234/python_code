class A:
    def func(self):
        print("IN A")
    pass

class B(A):
    # def func(self):
    #     print("IN B")
    pass

class C(A):
    # def func(self):
    #     print("IN C")
    pass

class D(B):
    # def func(self):
    #     print("IN D")
    pass

class E(C):
    # def func(self):
    #     print("IN E")
    pass

class F(D,E):
    # def func(self):
    #     print("IN F")
    pass

f1=F()
print(F.mro())