"""
递归函数中只递归一次，由于每次递归完都要递归到最后，所以用一个容器存取路径
递归函数中包含两次递归，每次递归都需要将存取路径copy一下
"""
import copy
n=int(input())
a_str=input().strip()
a=[int(item) for item in a_str.split(" ")]
k=int(input())
result=[]
#表示钱num个数的和为sun
def dfs(total,sum,re):
    if total==n:
        if sum==k:
            print(re)
        return
    re1=copy.deepcopy(re)
    dfs(total+1,sum,re1)
    re2 = copy.deepcopy(re)
    re2.append(a[total])
    dfs(total+1,sum+a[total],re2)
dfs(0,0,result)