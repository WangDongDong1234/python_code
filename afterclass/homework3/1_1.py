def LCS(x,y):
    if len(x)==0 or len(y)==0:
        return 0
    x_last=x[len(x)-1]
    y_last = y[len(y) - 1]
    if x_last==y_last:
        return LCS(x[:len(x)-1],y[:len(y)-1])+1
    else:
        return max(LCS(x[:len(x)-1],y),LCS(x,y[:len(y)-1]))

x=input().strip()
y=input().strip()
n=LCS(x,y)
print(n)