"""
先升后降
Description
从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的，连续出现的数值不应该有相等的情况。
Input
输入时一个数组，数值通过空格隔开。
Output
输出筛选之后的数组，用空格隔开。如果有多种结果，则一行一种结果。
Sample Input 1
1 2 4 7 11 10 9 15 3 5 8 6
Sample Output 1
1 2 4 7 11 10 9 8 6
最长递增子序列的长度：
    若i = 0，则LIS[i] = 1；
    若i > 0，则LIS[i]的值和其[0, i - 1]前缀的最长递增子序列长度有关，用j遍历[0, i - 1]得到其最长递增子序列为LIS[j]，对每一个LIS[j]，如果序列array[j]  < array[i]并且LIS[j] + 1 > LIS[i]，则LIS[i]的值变成LIS[j] + 1。即：
    LIS[i] = max{1, LIS[j] + 1}，其中array[i] > array[j] 且 j = [0, i - 1]。
"""
array_str=input().strip()
array=[int(item) for item in array_str.split(" ")]
lis=[1 for i in range(len(array))]
def LIS(array,lis):
    for i in range(len(array)):
        for j in range(0,i):
            if array[i]>array[j] and lis[j]+1>lis[i]:
                lis[i]=lis[j]+1
LIS(array,lis)
lds=[1 for i in range(len(array))]
array.reverse()
LIS(array,lds)
lds.reverse()
print(lds)
max=0
for i in range(len(array)):
    if lis[i]+lds[i]>max:
        max=lis[i]+lds[i]
print(max-1)
lds2=[1 for i in range(len(array))]
def LDS(array,lds):
    for i in range(len(array)):
        for j in range(0,i):
            if array[i]<array[j] and lds[j]+1>lds[i]:
                lds[i]=lds[j]+1
LDS(array,lds2)
print(lds2)


