"""
子串要求连续
子序列不要求连续
abcd
becd
3  bcd
"""
import copy
s=input().strip()
t=input().strip()
s_n=len(s)
t_n=len(t)
array=[]


for i in range(0,s_n+1):
    tmp=[]
    for j in range(0,t_n+1):
        tmp.append(0)
    array.append(tmp)
direction=copy.deepcopy(array)#0表示斜方向划，1表示从上滑下来，2表示从左话过来，3表示两者都行
for i in range(1,s_n+1):
    for j in range(1,t_n+1):
        if s[i-1]==t[j-1]:
            array[i][j]=array[i-1][j-1]+1
            direction[i][j]=0
        else:#0表示斜方向划，1表示从上滑下来，2表示从左话过来，3表示两者都行
            if array[i-1][j]>array[i][j-1]:
                direction[i][j]=1
                array[i][j]=array[i-1][j]
            elif array[i-1][j]<array[i][j-1]:
                direction[i][j]=2
                array[i][j] = array[i][j-1]
            else:
                array[i][j]=array[i-1][j]
                direction[i][j] = 3

def path(x,y):
    if x==0 or y==0:
        print(s)
    if direction[x][y]==0:
        return path(x-1,y-1)+
