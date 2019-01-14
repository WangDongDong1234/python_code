class H:
    def bar(self):
        print("H")
    pass

class G(H):
    # def bar(self):
    #     print("G")
    pass

class F(H):
    # def bar(self):
    #     print("F")
    pass

class E(G):
    # def bar(self):
    #     print("E")
    pass

class D(F):
    # def bar(self):
    #     print("D")
    pass

class C(E):
    # def bar(self):
    #     print("C")
    pass

class B(D):
    # def bar(self):
    #     print("B")
    pass

class A(B,C,D):
    # def bar(self):
    #     print("A")
    pass

a=A()
print(A.mro())