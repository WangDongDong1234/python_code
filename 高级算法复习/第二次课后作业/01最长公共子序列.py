"""
最长公共子序列
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
Input
输入为两行，一行一个字符串
Output
输出如果有多个则分为多行，先后顺序不影响判断。
Sample Input 1
1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1
23G456K
23G45JK


abcbdab
bdcaba      “BDAB”、“BCAB”、“BCBA”。
"""
import copy
str_a=input().strip()
str_b=input().strip()
dp=[]#i=0或j=0的直接初始为0  字符串的下表从1开始
for i in range(len(str_b)+1):
    tmp=[]
    for j in range(len(str_a)+1):
        tmp.append(0)
    dp.append(tmp)
for i in range(1,len(str_b)+1):
    for j in range(1,len(str_a)+1):
        if str_a[j-1]==str_b[i-1]:#对应字符串的位置
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
totalstr=[]
def traceback(i,j,str):
    while i>0 and j>0:
        if str_b[i-1]==str_a[j-1]:
            str.append(str_a[j-1])
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            elif dp[i-1][j]<dp[i][j-1]:
                j-=1
            else:
                str_tmp=copy.deepcopy(str)

                traceback(i-1,j,str_tmp)
                traceback(i,j-1,str_tmp)
                return
    #totalstr.append(str)
    if str not in totalstr:
        totalstr.append(str)
str=[]
traceback(len(str_b),len(str_a),str)
for item in dp:
    print(item)
for item in totalstr:
    print(item[::-1])
