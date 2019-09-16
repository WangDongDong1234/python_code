"""
爬楼梯
n=1:1
n=2:2
n>2:f(n)=f(n-1)+f(n-2)
"""
def fun(n):
    dp=[]
    for i in range(0,n+1):
        dp.append(0)
    for i in range(1,n+1):
        if i==1:
            dp[i]=1
        elif i==2:
            dp[i]=2
        else:
            dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
class Solution:

    def climbStairs(self, n: int) -> int:

        return fun(n)