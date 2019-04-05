"""

6 5
XBGBX
YBBYB
BGGXX
XYYBG
XYBGG
YYXYX
18
"""
m_n_str=input().strip()
m_n=[int(item) for item in m_n_str.split()]
n=m_n[0]#长
m=m_n[1]#宽
start_array=[]#最后样例
for i in range(n):
    tmp_str=input().strip()
    tmp=[]
    for item in tmp_str:
        tmp.append(item)
    start_array.append(tmp)
end_array=[]#空的画板
for i in range(n):
    tmp=[]
    for j in range(m):
        tmp.append("X")
    end_array.append(tmp)

def dfs_y(x,y,direct):
    if x<0 or x>=n or y<0 or y>=m or start_array[x][y]=="X" or start_array[x][y]=="B":#不能画的情况考虑清楚
        return
    if end_array[x][y]=="B":
        end_array[x][y]="G"
    if end_array[x][y]=="X":
        end_array[x][y]="Y"
    if direct==1:#向上递归
        dfs_y(x-1,y-1,1)
    if direct==-1:#向下递归
        dfs_y(x+1,y+1,-1)

def dfs_b(x,y,direct):
    if x<0 or x>=n or y<0 or y>=m or start_array[x][y]=="X" or start_array[x][y]=="Y":
        return
    if end_array[x][y]=="Y":
        end_array[x][y]="G"
    if end_array[x][y]=="X":
        end_array[x][y]="B"
    if direct==1:#向上递归
        dfs_b(x-1,y+1,1)
    if direct==-1:#向下递归
        dfs_b(x+1,y-1,-1)

total=0
for i in range(n):
    for j in range(m):
        #需要画Y
        #1.给的是Y当前是X
        #2.给的是G当前是X
        #3.给的是G当前是B
        if (start_array[i][j]=="Y" and end_array[i][j]=="X") or(start_array[i][j]=="G" and end_array[i][j]=="B") or(start_array[i][j]=="G" and end_array[i][j]=="X"):
            total+=1
            dfs_y(i,j,1)
            dfs_y(i,j,-1)
        #需要画B
        if (start_array[i][j]=="B" and end_array[i][j]=="X") or (start_array[i][j]=="G" and end_array[i][j]=="X")or (start_array[i][j]=="G" and end_array[i][j]=="Y"):
            total+=1
            dfs_b(i,j,1)
            dfs_b(i,j,-1)
        #需要画G
        if start_array[i][j]=="G" and end_array[i][j]=="X":
            total+=2
            #先画Y后画B
            dfs_y(i,j,1)
            dfs_y(i,j,-1)
            dfs_b(i,j,1)
            dfs_b(i,j,-1)
#print(end_array)
print(total)

