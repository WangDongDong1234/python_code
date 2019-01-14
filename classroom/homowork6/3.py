n=int(input())
def mystring(str,n):
    if n==1:
        return str+'$'+str[::-1]
    return mystring(str,n-1)+'$'*n+mystring(str,n-1)[::-1]
ss=mystring("12345",20)
for i in range(n):
    num=int(input())
    print(ss[num-1])

