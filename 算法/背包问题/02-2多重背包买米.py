"""
急！灾区的食物依然短缺！
为了挽救灾区同胞的生命，心系灾区同胞的你准备自己采购一些粮食支援灾区，现在假设你一共有资金n元，而市场有m种大米，每种大米都是袋装产品，其价格不等，并且只能整袋购买。
请问：你用有限的资金最多能采购多少公斤粮食呢？
输入描述:
输入数据首先包含一个正整数C，表示有C组测试用例，每组测试用例的第一行是两个整数n和m(1<=n<=100, 1<=m<=100),分别表示经费的金额和大米的种类，然后是m行数据，每行包含3个数p，h和c(1<=p<=20,1<=h<=200,1<=c<=20)，分别表示每袋的价格、每袋的重量以及对应种类大米的袋数。
输出描述:
对于每组测试数据，请输出能够购买大米的最多重量，你可以假设经费买不光所有的大米，并且经费你可以不用完。每个实例的输出占一行。
示例1
输入

8 2
2 100 4
4 100 2
"""
money_kinds_str=input().strip()
money_kinds=[int(item) for item in money_kinds_str.split(' ')]
money=money_kinds[0]
kinds=money_kinds[1]
privce_weight_totals=[]
for i in range(kinds):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    privce_weight_totals.append(tmp)
privce_weight_totals.insert(0,[0,0,0])
dp=[]
for i in range(kinds+1):
    tmp=[]
    for j in range(money+1):
        tmp.append(0)
    dp.append(tmp)
#开始动态规划了
for i in range(1,kinds+1):#从第一个种米开始
    for j in range(money,0,-1):#从money=1开始
        for k in range(0,privce_weight_totals[i][2]+1):
            if j<privce_weight_totals[i][0]*k:
                break
            else:
                #多重背包也是自己和自己比较，k=0时是不加入和之前的比较
                dp[i][j]=max(dp[i][j],dp[i-1][j-k*privce_weight_totals[i][0]]+k*privce_weight_totals[i][1])
print(dp)
print(dp[kinds][money])

