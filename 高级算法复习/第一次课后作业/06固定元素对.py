"""
Description

输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。


Input

输入第一行是数组，每一个数用空格隔开；第二行是数字和。


Output

输出这样两个数有几对。
1 2 4 7 11 0 9 15
11                       3
"""
array_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
sum=int(input())
total=0
for item in array:
    if sum-item in array:
        total+=1
print(total/2)