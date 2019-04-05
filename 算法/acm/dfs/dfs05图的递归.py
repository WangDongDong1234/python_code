"""
-1表示无穷
0 1 1 -1 1
1 0 -1 1 -1
1 -1 0 -1 1
-1 1 -1 0 -1
1 -1 1 -1 0
"""
n=int(input())
#标记地图的数组
book=[]
for i in range(0,n+1):
    book.append(0)
#存放地图的数组
array=[]
for i in range(0,n+1):
    tmp=[]
    if i==0:
        for j in range(0,n+1):
            tmp.append(0)
    else:
        tmp_str=input().strip()
        tmp_list=[int(item) for item in tmp_str.split()]
        for item in tmp_list:
            tmp.append(item)
        tmp.insert(0,0)
    array.append(tmp)
print(array)
#从那个节点开始
current_n=int(input())
sum=1
result=[]
#已经遍历到n结束
def dfs(location):
    global sum
    if sum==n:
        print(result)
        return
    for j in range(1,n+1):
        if array[location][j]==1 and book[j]==0:
            sum+=1
            book[j]=1
            result.append(j)
            dfs(j)#这里的回退是指这所有的都执行完了，在执行上一个循环没有执行完成的


book[current_n]=1
result.append(current_n)
dfs(current_n)

