"""
m[ i ][ j ] 表示 在面对第 i 件物品，且背包容量为  j 时所能获得的最大价值:v,w,c
8 10 6 3 7 2
4 6 2 2 5 1
12
"""
"""
所有有用的下表从1开始  价值和重量的有效值从1开始
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
for i in range(len(values)):#物品的范围是0到n（这里的len(values)=n+1）
    tmp=[]
    for j in range(0,c+1):#背包的范围是1-c
        tmp.append(0)
    dp.append(tmp)
#开始动态规划（物品和背包的有效值从1开始）
#m[ i ][ j ] 表示 在面对第 i 件物品（放不放还不知道），且背包容量为  j 时所能获得的最大价值
for i in range(1,len(values)):
    #for j in range(1,c+1):#正过来和到过来都可以，正过来自己理解的透
    for j in range(c,0,-1):
        if j<weights[i]:
            dp[i][j]=dp[i-1][j]#第i个物品不能放则最大价值等于在面向第i-1件物品时
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])#可以放的话，则最大价值要么是放，要么是不放
print("输出的结果是0-c,0-n")
for item in dp:
    print(item)
"""
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8]
[0, 0, 0, 0, 8, 8, 10, 10, 10, 10, 18, 18, 18]
[0, 0, 6, 6, 8, 8, 14, 14, 16, 16, 18, 18, 24]
[0, 0, 6, 6, 9, 9, 14, 14, 17, 17, 19, 19, 24]
[0, 0, 6, 6, 9, 9, 14, 14, 17, 17, 19, 21, 24]
[0, 2, 6, 8, 9, 11, 14, 16, 17, 19, 19, 21, 24]"""
print("解法二")
print("和解法一的区别是，第i+1层对第i层不断进行更新")
"""
设 f[j]表示重量不超过 j公斤的最大价值 可得出状态转移方程
"""
f=[0 for i in range(c+1)]
for i in range(1,len(values)):
    #初试状态是j为最大值且要大于i的重量
    for j in range(c,weights[i]-1,-1):
        if f[j-weights[i]]+values[i]>f[j]:
            f[j]=f[j-weights[i]]+values[i]
print(f)
print(f[c])