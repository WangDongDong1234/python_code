class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        book1=True#标记初试路径的 横路径上是否有障碍物
        book2=True#标记初始路径的 竖路径上是否有障碍物
        array=[]
        for i in range(m):
            tmp=[]
            for j in range(n):
                if i==0 or j==0:
                    #判断横路径上是否出现障碍物
                    if i==0 and obstacleGrid[i][j]==1:
                        book1=False
                    #判断竖路径上是否出现障碍物
                    if j==0 and obstacleGrid[i][j]==1:
                        book2=False

                    if (book1 and i==0) or (book2 and j==0):
                        tmp.append(1)
                    else:
                        tmp.append(0)
                else:
                    tmp.append(0)
            array.append(tmp)
        print(array)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    if obstacleGrid[i][j-1]!=1 and j-1>=0 :
                        array[i][j]+=array[i][j-1]
                    if obstacleGrid[i-1][j]!=1 and i-1>=0:
                        array[i][j]+=array[i-1][j]
                    if j-1>=0 and i-1>=0 and obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]==1:
                        array[i][j]=0
        return array[m-1][n-1]
array=[
  [0,1,0],
  [1,0,0],
  [0,0,0]
]
s=Solution()
print(s.uniquePathsWithObstacles(array))

