"""
5
2 3 3 3
"""
k=int(input())
len_num_str=input().strip()
len_num=[int(item) for item in len_num_str.split(' ')]
result=[]#存放的是歌曲
for i in range(len_num[1]):
    result.append(len_num[0])
for i in range(len_num[3]):
    result.append(len_num[2])
total=0
length=len(result)
#表示当前在i结点  考虑要不要加i
def dfs(sum,i):
    global total
    if i==length:
        if sum==k:
            total+=1
        return
    dfs(sum+result[i],i+1)
    dfs(sum,i+1)
dfs(0,0)
print(total)
print("不推荐用01背包去求解，用组合数去解")
"""
5
2 3 3 3
"""
k=int(input())
length_total_str=input().strip()
length_total=[int(item) for item in length_total_str.split(' ')]
a=[length_total[0],length_total[1]]
b=[length_total[2],length_total[3]]

c=[]
for i in range(0,a[1]+b[1]+1):
    tmp=[]
    for j in range(0,a[1]+b[1]+1):
        tmp.append(0)
    c.append(tmp)
c[0][0]=1
for i in range(1,a[1]+b[1]+1):
    c[i][0]=1
    for j in range(1,a[1]+b[1]+1):
        c[i][j]=c[i-1][j-1]+c[i-1][j]
# for item in c:
#     print(item)
count=0
for i in range(0,(k//a[0])+1):
    if i<=a[1]:#小于a的个数
        if (k-i*a[0])%b[0]==0 and (k-i*a[0])/b[0]<=b[1]:
            #a是从x个中选i个  b是从y个中选(k-i*a)/b个
            count+=c[a[1]][i]*c[b[1]][int((k-i*a[0])/b[0])]
print(count%1000000007)




        





