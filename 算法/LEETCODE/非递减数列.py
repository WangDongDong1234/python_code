"""
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:

输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。
"""
"""
  // 思路如下：
    // 如果出现 a[i] > a[i+1]   改变一个数 就面临两种选择
    // 1. 把a[i]变小
    // 2. 把a[i+1] 变大
    // 这两种选择其实是有依据的 需要比较a[i-1] 与 a[i+1]的值
    // eg.  ... 1 4 3 ...   只能选择把4变小   ... 3 4 1 ... 只能选择把1变大
    // 改变完之后，记录改变次数，再检测是否升序
    // 如果次数大于1，至少改了两次 返回false"""
array_str=input().strip().strip('[').strip(']')
array=[int(item) for item in array_str.split()]
#将峰值右边第一个的元素进行标记(统计出现单个点的情况)
book=[0 for i in range(len(array))]
result=True

for i in range(0,len(array)-1):
    if array[i+1]<array[i] and book[i]==0:
        book[i+1]=1
        #连续两个下降
    elif book[i]==1 and array[i+1]<array[i] :
        result=False
#峰值右边第一个点的隔宿
total=sum(book)
if total>1:
    result=False
print(result)


