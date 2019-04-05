# #1数的全排列
# n=int(input())
# #盒子
# box=[0 for i in range(n+1)]
# #标记
# book=[0 for i in range(n+1)]
# sum=0
# def dfs(step):
#     #表示到了第n+1个盒子面前，代表前n个盒子放好了
#     if step==n+1:
#         global sum
#         sum+=1
#         print(box[1:])
#         return
#     for i in range(1,n+1):
#         if book[i]==0:
#             box[step]=i
#             book[i]=1
#             dfs(step+1)
#             book[i]=0
# dfs(1)
# print(sum)

#2求最短路径，并打印每条路径
# import copy
# import sys
# sys.setrecursionlimit(1000000) #例如这里设置为一百万
# mn_str=input().strip()
# mn=[int(item) for item in mn_str.split(' ')]
# print(mn)
# m=mn[0]
# n=mn[1]
# #标记
# book=[]
# for i in range(0,m+1):
#     tmp=[]
#     for j in range(0,n+1):
#         tmp.append(0)
#     book.append(tmp)
# #路径
# path=copy.deepcopy(book)
#
# #地图
# array=[]
# for i in range(0,m+1):
#     if i==0:
#         tmp=[]
#         for j in range(0,n+1):
#             tmp.append(0)
#         array.append(tmp)
#     else:
#         array_str=input().strip()
#         tmp=[int(item) for item in array_str.split(' ')]
#         tmp.insert(0,0)
#         array.append(tmp)
# start_str=input().strip()
# start=[int(item) for item in start_str.split(' ')]
# start_x=start[0]
# start_y=start[1]
# end_str=input().strip()
# end=[int(item) for item in end_str.split(' ')]
# end_x=end[0]
# end_y=end[1]
#
# def dfs(x,y,step):
#     if x==end_x and y==end_y:
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if path[i][j]>=1:
#                     print('('+str(i)+'-'+str(j)+'->'+str(path[i][j])+')',end=" ")
#         print(step)
#         return
#     next=[[1,0],[0,1],[-1,0],[0,-1]]
#     for item in next:
#         next_x=x+item[0]
#         next_y=y+item[1]
#         if next_x<1 or next_x>m or next_y<1 or next_y>n:
#             continue
#         if book[next_x][next_y]==0 and array[next_x][next_y]==0:
#             path[next_x][next_y]=1
#             book[next_x][next_y]=1
#             dfs(next_x,next_y,step+1)
#             book[next_x][next_y]=0
#             path[next_x][next_y]=0
#
#
# book[start_x][start_y]=1
# dfs(start_x,start_y,0)

#计数
# import sys
# import copy
# mn_str=input().strip()
# mn=[int(item) for item in mn_str.split(' ')]
# m=mn[0]
# n=mn[1]
# location_str=input().strip()
# location=[int(item) for item in location_str.split(' ')]
# location_x=location[0]
# location_y=location[1]
# array=[]#标记陆地和海洋
# for i in range(0,m+1):
#     if i==0:
#         tmp = []
#         for j in range(0,n+1):
#             tmp.append(0)
#         array.append(tmp)
#     else:
#         tmp_str=input().strip()
#         tmp=[int(item) for item in tmp_str.split()]
#         tmp.insert(0,0)
#         array.append(tmp)
#
# book=[]#标记是否走过
# for i in range(0,m+1):
#     tmp=[]
#     for j in range(0,n+1):
#         tmp.append(0)
#     book.append(tmp)
#
# path=copy.deepcopy(book)#标记路径
# sum=1
# def dfs(x,y,step):
#     next=[[1,0],[0,1],[-1,0],[0,-1]]
#     for item in next:
#         next_x=x+item[0]
#         next_y=y+item[1]
#         if next_x<1 or next_x>m or next_y<1 or next_y>n:
#             continue
#         if book[next_x][next_y]==0 and array[next_x][next_y]!=0:
#             path[next_x][next_y]=step
#             book[next_x][next_y]=1
#             global sum
#             sum+=1
#             dfs(next_x,next_y,step+1)
# book[location_x][location_y]=1
#
# dfs(location_x,location_y,1)
# print(sum)
# for i in range(0,m+1):
#     for j in range(0,n+1):
#         if path[i][j]!=0:
#             print('第'+str(path[i][j])+"步"+'-('+str(i)+','+str(j)+')')


#图的遍历
n=int(input())
book=[]#标记
for i in range(0,n+1):
    book.append(0)
array=[]#存放图的矩阵
for i in range(0,n+1):
    if i==0:
        tmp=[]
        for j in range(0,n+1):
            tmp.append(-1)
        array.append(tmp)
    else:
        tmp_str=input().strip()
        tmp=[int(item) for item in tmp_str.split()]
        tmp.insert(0,-1)
        array.append(tmp)
current=int(input())
book[current]=1
result=[]
result.append(current)
sum=1
def dfs(current):
    global sum
    if sum==n:
        global result
        print(result)
        return
    for j in range(1,n+1):
        if book[j]==0 and array[current][j]==1:
            sum+=1
            result.append(j)
            book[j]=1
            dfs(j)
dfs(current)





