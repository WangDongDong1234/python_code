n=int(input())
a_str=input().strip()
b_str=input().strip()
a=[int(item) for item in a_str.split(' ')]
b=[int(item) for item in b_str.split(' ')]

def fun(a,b):
    sum=0
    for i in range(len(a)):
        sum+=a[i]*b[i]
    return sum
book=[]
box=[]
for i in range(n):
    book.append(0)
    box.append(0)
min=fun(a,b)
def dfs(step):
    if step==n:
        global min
        tmp=fun(box,b)
        if tmp<min:
            min=tmp
        return
    for i in range(n):
        if book[i]==0:
            book[i]=1
            box[step]=a[i]
            dfs(step+1)
            book[i]=0
dfs(0)
print(min)
