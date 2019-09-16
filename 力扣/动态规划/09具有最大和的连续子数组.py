"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        dp=[]#表示从
        for i in range(length):
            tmp=[]
            for j in range(length):
                if i==j:
                    tmp.append(nums[i])
                else:
                    tmp.append(0)
            dp.append(tmp)
        for i in range(length):
            for j in range(i+1,length):
                dp[i][j]=dp[i][j-1]+nums[j]
        max=-9999
        for i in range(length):
            for j in range(i,length):
                if max<dp[i][j]:
                    max=dp[i][j]
        return max

array_str=input().strip()
array=[int(item) for item in array_str.split(" ")]
s=Solution()
print(s.maxSubArray(array))#-2 1 -3 4 -1 2 1 -5 4

"""
"""
 /**
     * 定义状态：
     * dp[i] ： 表示以 nums[i] 结尾的连续子数组的最大和
     * <p>
     * 状态转移方程：
     * dp[i] = max{num[i],dp[i-1] + num[i]}
     *
     * @param nums
     * @return
     */
！
"""

from typing import List
import sys
def fun(nums):
    dp = []
    max_value = -sys.maxsize

    for e in nums:
        dp.append(int(e))

    for i in range(1, len(nums)):
        dp[i] = max(dp[i], dp[i - 1] + nums[i])

    for i in range(len(nums)):
        if max_value < dp[i]:
            max_value = dp[i]
    return max_value
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return fun(nums)

array_str=input().strip()
array=[int(item) for item in array_str.split(" ")]
s=Solution()
print(s.maxSubArray(array))
