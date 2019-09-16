"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
输入: "cbbd"
输出: "bb"

dp[i][j]的递推公式可以这么表述：

（1）首先对dp的对角线元素初始化为1，也就是当i==j时，dp[i][j]=1。

这很显然，每个单独的字符其实就是个长度为1的回文串。

（2）当j-i==1：

若s[i]==s[j]，则dp[i][j]=2；否则dp[i][j]=0。

解释：当j-i==1时，若s[i]==s[j]，则s[i]和s[j]可以组成一个长度为2的回文串。若s[i]！=s[j]，显然他们不可能组成回文串，dp[i][j]=0。

（3）当j-i>=2：

若s[i]==s[j]：若dp[i+1][j-1]>0，则dp[i][j]= dp[i + 1][j - 1] + 2;否则dp[i][j]= 0;

若s[i]！=s[j]：dp[i][j]=0。

解释：如果s[i]==s[j]，表明这个子串有可能是回文串。当去头去尾后它是回文串时，就可以在去头去尾的那个回文串长度基础上+2，得到它的长度。如果去头去尾后不是回文串，那这个子串一定不是回文串，回文串长度只能是0。

若s[i]！=s[j]，显然他们不可能组成回文串，dp[i][j]=0。

只需找到dp[i][j]的最大元素和它对应的i和j就可以得到结果“s中最长回文子串”。

"""
str=input().strip()
length=len(str)
#表示以i开始以j结尾的字符串中回文串的长度，只要j>=i的部分
array=[]
for i in range(length):
    tmp=[]
    for j in range(length):
        if i==j:
            tmp.append(1)
        else:
            tmp.append(0)
    array.append(tmp)
for i in range(length):
    for j in range(length):
        if j>i:
            if j-i==1:
                if str[i]==str[j]:
                    array[i][j]=2
                else:
                    array[i][j]=0
            if j-i>1:
                if str[i]==str[j] and array[i+1][j-1]>0:
                    array[i][j]=array[i+1][j-1]+2
                if str[i]!=str[j]:
                    array[i][j]=0

max=0
for i in range(length):
    for j in range(i,length):
        if array[i][j]>max:
            max=array[i][j]
# for i in range(length):
#     for j in range(i,length):
#         if array[i][j]==max:
#             print(str[i:j+1])
book=True
for i in range(length):
    for j in range(i,length):
        if array[i][j]==max and book:
            print(str[i:j+1])
            #book=False