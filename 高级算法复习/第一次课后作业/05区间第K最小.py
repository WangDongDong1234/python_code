"""
Description

找到给定数组的给定区间内的倒数第K小的数值。


Input

输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。


Output

1 2 3 4 5 6 7
3 5
2                  4
"""
array_str=input().strip()
mn_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
mn=[int(item) for item in mn_str.split(' ')]
m=mn[0]
n=mn[1]
k=int(input())

tmp=array[m-1:n]

tmp.sort()
print(tmp[k-1])