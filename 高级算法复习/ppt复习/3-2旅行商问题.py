"""
4
0 2 5 7
2 0 8 3
5 8 0 1
7 3 1 0
0
"""
import copy
n=int(input())
array=[]
for i in range(n):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    array.append(tmp)
path=[0 for i in range(n)]#记录路径
book=[0 for i in range(n)]#标记路径
start=int(input())
def dfs(index,step):
    if index==start and book[start]==1:
        print(path)
    for i in range(n):
        if book[i]==0 and array[index][i]!=0:
            book[i]=1
            path[i]=step
            dfs(i,step+1)
            book[i]=0
            path[i]=0

dfs(start,1)




