class A:
    pass

class B(A):
    pass

b=B()
print(type(b) )#<class '__main__.B'>
print(type(b) is B)#True
print(isinstance(b,B))#True
print(isinstance(b,A))#True

print(issubclass(B,A))#True
print(issubclass(A,B))#False