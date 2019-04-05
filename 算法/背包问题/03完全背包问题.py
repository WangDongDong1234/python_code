"""
多重背包问题
v w c

4 5 3
3 4 2
7
"""
values_str=input().strip()
values=[int(item) for item in values_str.split(' ')]
values.insert(0,0)
weights_str=input().strip()
weights=[int(item) for item in weights_str.split(' ')]
weights.insert(0,0)
c=int(input())
print("解法一")
dp=[]
#长是0-C 宽是0-n
for i in range(len(values)):#这里len(values)=n+1
    tmp=[]
    for j in range(c+1):
        tmp.append(0)
    dp.append(tmp)
for i in range(1,len(values)):
    for j in range(1,c+1):
        #到底取多少件
        for k in range(0,(j//weights[i])+1):#这里不要忘了加1
            #严重注意这里的比较  不是和i-1比较了是和自己比较  只不过每次比较后k就会增加1（比01背包多了个循环）
            #多重背包里面有加0-k个（加0的话就是不和前面比较了）
            dp[i][j]=max(dp[i][j],dp[i-1][j-k*weights[i]]+values[i]*k)
print(dp)
print(dp[len(values)-1][c])
print("解法二")
f=[0 for i in range(c+1)]
for i in range(1,len(values)):
    #j在增大的过程中是否可以在重复加（虽然和01有相似）
    for j in range(weights[i],c+1):
        #这里也是自己和自己比较（起点是从可以加一个情况下和不加的情况比较）
        f[j]=max(f[j],f[j-weights[i]]+values[i])
print(f)
print(f[c])

