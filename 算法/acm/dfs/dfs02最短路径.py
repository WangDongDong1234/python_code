#计算到目的地点最短的距离
#扩展  打印最短路径
import copy
import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万
mn_str=input("输入mn").strip()
mn=[int(item) for item in mn_str.split(" ")]
m=mn[0]
#print(m)
n=mn[1]
#print(n)
book=[]
for i in range(0,m+1):
    tmp=[]
    for j in range(0,n+1):
        tmp.append(0)
    book.append(tmp)
#print(book)
path=copy.deepcopy(book)
array=[]
for i in range(0,m+1):
    array_str = input().strip()
    tmp=[int(item) for item in array_str.split(" ")]
    array.append(tmp)

#print(array)
min=99999
start_str=input("输入起始位置").strip()
start=[int(item) for item in start_str.split(" ")]
start_x=start[0]
start_y=start[1]
#print(start_x,start_y)
end_str=input("输入终点位置").strip()
end=[int(item) for item in end_str.split(" ")]
end_x=end[0]
end_y=end[1]
#print(end_x,end_y)
def dfs(x,y,step):
    if x==end_x and y==end_y:
        for i in range(0,len(book)):
            for j in range(0,len(book[0])):
                if path[i][j]>=1:
                    print("(",i,"-",j,"-",path[i][j],")",end=" ")
        print(step)
        global min
        if step<min:
            min=step
        return

    next=[[0,1],[1,0],[0,-1],[-1,0]]  #按照右下左上的顺序
    for item in next:
        next_x=x+item[0]
        next_y=y+item[1]
        global m
        global n
        if next_x<1 or next_x>m or next_y<1 or next_y>n:
            continue
        if array[next_x][next_y]!=1 and book[next_x][next_y]==0:
            book[next_x][next_y]=1  #确保单次行走不原地打转
            path[next_x][next_y]=step+1
            dfs(next_x,next_y,step+1)
            book[next_x][next_y]=0
            #回退时清除当前步数,因为步数是一步一步累加的，置为0表示没有走到这
            path[next_x][next_y]=0
    #return
book[start_x][start_y]=1
dfs(start_x,start_y,0)
print("最短路径",min)
#测试数据
"""
5 4
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 1
1 1
4 3
"""