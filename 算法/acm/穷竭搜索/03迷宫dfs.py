"""
# . # # # # # # . #
. . . . . . # . . #
. # . # # . # # . #
. # . . . . . . . .
# # . # # . # # # #
. . . . # . . . . #
. # # # # # # # . #
. . . . # . . . . .
. # # # # . # # # .
. . . . # . . . . #
"""
mn_str=input().strip()
mn=[int(item) for item in mn_str.split(" ")]
m=mn[0]
n=mn[1]
start_str=input().strip()
start=[int(item) for item in start_str.split(" ")]
# start_x=start[0]
# start_y=start[1]
end_str=input().strip()
end=[int(item) for item in end_str.split(" ")]
end_x=end[0]
end_y=end[1]
book=[]
for i in range(0,m+1):
    tmp=[]
    for j in range(0,n+1):
        tmp.append(0)
    book.append(tmp)

array=[]
for i in range(0,m+1):
    tmp=[]
    if i==0:
        for j in range(0,n+1):
            tmp.append('#')
    else:
        in_str=input().strip()
        list=[str(item) for item in in_str.split(" ")]
        tmp.extend(list)
        tmp.insert(0,'#')
    array.append(tmp)
for item in array:
    print(item)
restult=[]
restult.append([start[0],start[1]])
min=99999
def dfs(start_x,start_y,step):
    if start_x==end_x and start_y==end_y:
        print(restult)
        global min
        if step<min:
            min=step
        return
    next = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 按照右下左上的顺序
    for item in next:
        next_x=start_x+item[0]
        next_y=start_y+item[1]
        if next_x<1 or next_x>m or next_y<1 or next_y>n:
            continue
        if book[next_x][next_y]==0 and array[next_x][next_y]=='.':
            book[next_x][next_y]=1
            restult.append([next_x,next_y])
            dfs(next_x,next_y,step+1)
            book[next_x][next_y]=0
            restult.pop()

dfs(start[0],start[1],0)
print(min)

