"""
子矩阵问题（这里只要把0换成无穷小就能用下面的解）
Description
给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
Input
输入的每一行是用空格隔开的0或1。
Output
输出一个数值。
1 0 1 1
1 1 1 1
1 1 1 0   6
"""
array=[]
while 1:
    line_str=input().strip()
    if(len(line_str)==0):
        break
    line=[int(item) for item in line_str.split(" ")]
    array.append(line)

def maxsub(a):
    max=0
    b=0
    for i in range(len(a)):
        # if b>0:
        #     b+=a[i]
        # else:
        #     b=a[i]
        # if b>max:
        #     max=b
        b+=a[i]
        if b>max:
            max=b
        if b<0:
            max=0
    return max

"""
https://www.cnblogs.com/GodA/p/5237061.html

0 -2 -7 0　这样一个4*4的矩阵中，元素之和最大的子矩阵为   9 2　 ，它们之和为15。　

　　　　　　 9  2 -6 2　　　　　　　　　　　　　　　　　　　　　　　　-4 1
　　　　　　-4 1 -4 1　　　　　　　　　　　　　　　　　　　　　　　　 -1 8
　　　　　　-1 8 0 -2
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 2
思路：首先子矩阵肯定是连续的行和列
      首先是枚举出所有可能的行（比如1-1，1-2，1-3，1-4，2-2，2-3，2-4）等，
      然后再这些可能的行中找列
"""
maxsubrec=0
maxsubarry=0
for i in range(len(array)):
    array_list = [0 for i in range(len(array))]
    for j in range(i,len(array)):
        for k in range(len(array)):
            array_list[k]+=array[j][k]
        maxsubarry=maxsub(array_list)
        if maxsubarry>maxsubrec:
            maxsubrec=maxsubarry
print("最大子矩阵和",maxsubrec)