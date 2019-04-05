"""
给定数组arr和整数num， 共返回有多少个子数组满足如下情况：
max(arr[i..j]) - min(arr[i..j]) <= num
max(arr[i..j])表示子数组arr[i..j]中的最大值， min(arr[i..j])表示子数组arr[i.中的最小值。
【要求】
如果数组长度为N， 请实现时间复杂度为O(N)的解法
解法一：暴力O(n^3)
解法二:
①、如果一个子数组从L->R中，arr[max] - arr[min] <= num，那么在L->R范围内的子数组都符合要求

②、如果一个子数组从L->R中，arr[max] - arr[min] > num，那么以L->R为基础向外扩的子数组都不符合要求

做两个双端队列，一个是窗口内最大值，另外一个是窗口内最小值

1）、开始时L在数组最左端 0 位置，R从最左端开始向右扩，直到再扩充一个值就不符合要求时，R停止，设此时为 x 位置

则以0位置开始的子数组有 x + 1个（0,0~1,……0~x）  这些子数组是以0为起始位置符合要求的所有子数组个数

2）、L向右边移动一个位置，更新两个窗口内的结构，然后R试着继续向右扩，重复上面的，然后就能得到以1为起始位置符合要求的所有子数组个数

L每次向右移动一个位置，R就开始向右扩
"""
array_str=input().strip();
num=int(input())
array=[int(item) for item in array_str.split()]
print("这是解法一")
total1=0
for i in range(len(array)):
    for j in range(i,len(array)):
        max=array[i]
        min=array[i]
        for t in range(i+1,j+1):
            if array[t]>max:
                max=array[t]
            if array[t]<min:
                min=array[t]
        if max-min<=num:
            total1+=1
print("解法一",total1)
print("这是解法二")
total2=0
i=0
j=0
while i<len(array):
    t = i
    max = array[t]
    min = array[t]
    while j<len(array):
        for tmp in range(i,j+1):
            if array[tmp]>max:
                max=array[tmp]
            if array[tmp]<min:
                min=array[tmp]
        if max-min>num:
            break
        j+=1
    total2+=j-1-i+1  #这里注意跳到j是不满足的情况
    i+=1
print("解法二",total2)



