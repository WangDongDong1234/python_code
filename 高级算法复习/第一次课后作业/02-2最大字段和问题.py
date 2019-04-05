"""
https://www.cnblogs.com/aabbcc/p/6504605.html
分治法求解

       分治法思路如下：

    将序列a[1:n]分成长度相等的两段a[1:n/2]和a[n/2+1:n],分别求出这两段的最大字段和，则a[1:n]的最大子段和有三中情形：

    [1]、a[1:n]的最大子段和与a[1:n/2]的最大子段和相同；

       [2]、a[1:n]的最大子段和与a[n/2+1:n]的最大子段和相同；

    [3]、a[1:n]的最大字段和为，且1<=i<=n/2,n/2+1<=j<=n。

    可用递归方法求得情形[1],[2]。对于情形[3],可以看出a[n/2]与a[n/2+1]在最优子序列中。因此可以在a[1:n/2]中计算出，并在a[n/2+1:n]中计算出。则s1+s2即为出现情形[3]时的最优值。
    -2 11 -4 13 -5 -2   20
"""
array_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
print(array)
def maxSum(array,left,right):

    if left==right:
        return array[left]
    else:
        center=int((left+right)/2)
        sum_left=maxSum(array,left,center)
        sum_right=maxSum(array,center+1,right)
        sum_mind1=array[center]
        left_s1=array[center]#保留想左探索过程中的最大值
        for t in range(center-1,left-1,-1):
            left_s1+=array[t]
            if left_s1>sum_mind1:
                sum_mind1=left_s1
        sum_mind2=array[center]#这里中间的值加了两次
        right_s1=array[center]
        for t in range(center+1,right+1):
            right_s1+=array[t]
            if right_s1>sum_mind2:
                sum_mind2=right_s1
        sum_mind=sum_mind2+sum_mind1-array[center]
        return max(sum_mind,sum_left,sum_right)
print(maxSum(array,0,len(array)-1))
"""
https://www.cnblogs.com/fzl194/p/8677350.html
动态规划求：设dp[i]为以i结尾的最大子段和，那对于dp[i]而言只有两种情况，如果dp[i - 1] > 0, 那么dp[i] = dp[i - 1] + a[i];不然，dp[i] = a[i]，然后求出dp数组中的最大值即可。
dp[i] = max(dp[i], dp[i - 1] + a[i]);  即以i结尾的最大子段=array[i]+dp[i-1]?选择加还是不加
"""
dp=[]#初始化dp，以i结尾的最大字段初始只有他一个
for i in range(len(array)):
    dp.append(array[i])
for i in range(1,len(array)):
    dp[i]=max(array[i]+dp[i-1],array[i])
print(dp)
print(max(dp))
print("理解了，他是假设有负数有正数，确保最大值大于0，但是这样不正确，当值全是负数的时候错的")

def l(array):
    max=0
    this=0
    for i in range(len(array)):
        this+=array[i]
        if this>max:
            max=this
        if this<0:
            this=0
    return max
print(l(array))

