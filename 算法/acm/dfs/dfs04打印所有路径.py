"""
炸弹超人
5 4
1 1
4 3
0 0 1 0
0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 1
"""
mn_str=input("请输入mn").strip()
mn=[int(item) for item in mn_str.split(" ")]
m=mn[0]
n=mn[1]
print(m,n)
location_str=input("请输入降落地点").strip()
location=[int(item) for item in location_str.split()]
location_x=location[0]
location_y=location[1]
end_str=input("请输入终点").strip()
end=[int(item) for item in end_str.split(" ")]
end_x=end[0]
end_y=end[1]
#标记地图的数组
book=[]
for i in range(0,m+1):
    tmp=[]
    for j in range(0,n+1):
        tmp.append(0)
    book.append(tmp)
print(book)
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
print(array)

min=9999
path_array=[]
def dfs(x,y,step):
    if x==end_x and y==end_y:
        global min
        if step<min:
            min=step
        print(path_array)
        return
    next = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 按照右下左上的顺序
    for item in next:
        #这里老是忘了加x,y
        next_x=item[0]+x
        next_y=item[1]+y
        if next_x<1 or next_x>m or next_y<1 or next_y>n:
            continue
        if book[next_x][next_y]==0 and array[next_x][next_y]==0:
            book[next_x][next_y]=1
            path_array.append([next_x,next_y])
            dfs(next_x,next_y,step+1)
            book[next_x][next_y]=0
            path_array.pop()

book[location_x][location_y]=1
dfs(location_x,location_y,0)
