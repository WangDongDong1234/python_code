import math
n=int(input())
result=[]
for i in range(0,n):
    in_put=int(input())
    if in_put<9:
        result.append(0)
    else:
        total=0
        for i in range(9,in_put+1):
            tmp=int(math.sqrt(i))
            if tmp*tmp!=i:
                continue
            else:
                num=[]
                for j in range(1,tmp+1):
                    if i%j==0:
                        other=int(i/j)
                        if j not in num:
                            num.append(j)
                        if other not in num:
                            num.append(other)
                if len(num)==9:
                    total+=1
        result.append(total)
for item in result:
    print(item)