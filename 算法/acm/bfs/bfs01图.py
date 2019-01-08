"""
0 1 1 -1 1
1 0 -1 1 -1
1 -1 0 -1 1
-1 1 -1 0 -1
1 -1 1 -1 0
"""
import copy
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
current_n=int(input())
sum=1
result=copy.deepcopy(book)
i=1
j=2
result[i]=current_n
book[current_n]=1
while sum<n:
    for index in range(1,n+1):
        if book[index]==0 and array[result[i]][index]==1:
            book[index]=1
            result[j]=index
            sum+=1
            j+=1
    i+=1
print(result[1:])

