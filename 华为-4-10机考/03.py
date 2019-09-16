m_n_sr=input()
m_n=[int(item) for item in m_n_sr.split(" ")]
m=m_n[0]
n=m_n[1]
array=[]
for i in range(m):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(" ")]
    array.append(tmp)
book=[]
for i in range(m):
    tmp=[]
    for j in range(n):
        tmp.append(0)
    book.append(tmp)

start_end_str=input().strip()
start_end=[int(item) for item in start_end_str.split(" ")]
start_x=start_end[0]
start_y=start_end[1]
end_x=start_end[2]
end_y=start_end[3]

count=0
def dfs(x,y):
    global count
    if x==end_x and y==end_y:
        count+=1
        book[x][y]=0
        return
    #上右下左
    next=[[-1,0],[0,1],[1,0],[0,-1]]
    for item in next:
        next_x=x+item[0]
        next_y=y+item[1]
        if next_x<0 or next_x>=m or next_y<0 or next_y>=n:
            continue
        if array[next_x][next_y]>array[x][y] and book[next_x][next_y]==0:
            book[next_x][next_y]=1
            dfs(next_x,next_y)
book[start_x][start_y]=1
dfs(start_x,start_y)
print(count%1000000000)