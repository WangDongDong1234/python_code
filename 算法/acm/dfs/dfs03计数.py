#宝岛探险   用dfs产生一个问题我倒什么情况才不会继续走(解决，for循环在4个方向执行完了就退出)

import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万

mn_str=input("请输入mn").strip()
mn=[int(item) for item in mn_str.split(" ")]
m=mn[0]
n=mn[1]
location_str=input("请输入降落地点").strip()
location=[int(item) for item in location_str.split()]
location_x=location[0]
location_y=location[1]
#标记地图的数组
book=[]
for i in range(0,m+1):
    tmp=[]
    for j in range(0,n+1):
        tmp.append(0)
    book.append(tmp)
#存放地图的数组
array=[]
for i in range(0,m+1):
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
sum=1
def dfs(x,y):
    next=[[0,1],[1,0],[0,-1],[-1,0]]#右下左上
    for item in next:
        next_x=item[0]+x
        next_y=item[1]+y
        #想判断下一步是否越界
        if next_x<1 or next_x>m or next_y<1 or next_y>n:
            continue
        if book[next_x][next_y]==0 and array[next_x][next_y]>0:#如果下一步不是海洋或者没走过
             global sum
             sum+=1
             book[next_x][next_y]=1
             dfs(next_x,next_y)

    return
book[location_x][location_y]=1
dfs(location_x,location_y)
print(sum)