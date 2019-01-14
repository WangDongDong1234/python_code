n=int(input())

def fun(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return fun(n-2)+fun(n-1)
for i in range(n):
    test_n=int(input())
    print(fun(test_n))