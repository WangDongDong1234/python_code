import math
def num(n):
    count=2
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            if i==int(math.sqrt(n)):
                count+=1
            else:
                count+=2

    return count

n=int(input())
result=[]
for i in range(0,n):
    in_put=int(input())
    if in_put<9:
        result.append(0)
    else:
        total=0
        for i in range(9,in_put+1):
            r=num(i)
            if r==9:
                total+=1
        result.append(total)
for item in result:
    print(item)