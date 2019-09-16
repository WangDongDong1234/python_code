from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[]
        for i in range(len(grid)):
            tmp=[]
            for j in range(len(grid[0])):
                tmp.append(0)
            dp.append(tmp)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0 and j>=1:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0 and i>=1:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i][j-1]+grid[i][j],dp[i-1][j]+grid[i][j])
        print(dp)
        return dp[len(grid)-1][len(grid[0])-1]


array=[[1,3,1],[1,5,1],[4,2,1]]
s=Solution()
print(s.minPathSum(array))
