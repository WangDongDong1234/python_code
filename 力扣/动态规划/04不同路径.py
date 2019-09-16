"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
思路：动态规划

1 只能向下或者向右走。所以当在i=0 或者 j = 0时  等于1

2 dp[i] [j] = dp[i-1][j] + dp[i][j-1];
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array=[]
        for i in range(m):
            tmp=[]
            for j in range(n):
                if i==0 or j==0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            array.append(tmp)
        for i in range(1,m):
            for j in range(1,n):
                array[i][j]=array[i-1][j]+array[i][j-1]
        return array[m-1][n-1]

m_n_str=input().strip()
m_n=[int(item) for item in m_n_str.split(' ')]
m=m_n[0]
n=m_n[1]
array=[]
for i in range(m):
    tmp=[]
    for j in range(n):
        tmp.append(0)
    array.append(tmp)

count=0
def dfs(x,y):
    global count
    global m
    global n
    if x==m-1 and y==n-1:
        count+=1
        return
    next=[[1,0],[0,1]]
    for item in next:
        next_x=x+item[0]
        next_y=y+item[1]
        if next_x<m and next_y<n:
            dfs(next_x,next_y)
print("标准答案",Solution().uniquePaths(m,n))
dfs(0,0)
print(count)
