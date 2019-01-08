"""
给定整数a1,a2,.....an判断是否可以从中选出若干数，使他们的和恰好为K
测试用例
4 1 2 4 7
13
yes  13=2+4+7
4 1 2 4 7
15
no
"""
import copy
a_str=input().strip()
list=[int(item) for item in a_str.split()]
n=list[0]
k=int(input())
book=[0 for item in range(0,n+1)]
#表示前i项的和，即将判断第i+1项是否要加上
def dfs(i,sum):
    if i==n:
        return sum==k
    if sum>k:
        return False
    #第list[i]不加

    if dfs(i+1,sum):
        return True
    #第list[i]


    if dfs(i+1,sum+list[i+1]):
        return True
    return False

print(dfs(0,0))

