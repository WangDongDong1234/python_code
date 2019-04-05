.import copy
n=int(input())
array=[]
for i in range(0,n+1):
    if i==0:
        tmp=[]
        for j in range(0,n+1):
            tmp.append(-1)
        array.append(tmp)
    else:
        tmp_str=input().strip()
        tmp=[int(item) for item in tmp_str.split(' ')]
        tmp.insert(0,-1)
        array.append(tmp)
print(array)
current=int(input())
book=[]
for i in range(n+1):
    book.append(0)
print(book[1:])
last_result=[]
last_result.append(current)
book[current]=1

def dfs(current,result):
    if len(result)==n:
        print(result)
        return
    for j in range(1,n+1):
        if book[j]==0 and array[current][j]==1:
            book[j]=1
            new_result=copy.deepcopy(result)
            new_result.append(j)
            dfs(j,new_result)
            book[j]=0
dfs(current,last_result)

"""
5
0 1 1 1 -1
1 0 -1 -1 1
1 -1 0 -1 -1
1 -1 -1 0 1
-1 1 -1 1 0"""
