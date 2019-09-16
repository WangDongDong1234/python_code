"""
这是求有几对有效括号
str=input().strip()
array=[]
count=0
for i in range(len(str)):
    try:
        t=array[len(array)-1]
    except IndexError:
        t=''
    array.append(str[i])
    if str[i]==")" and t=="(":
        count+=1
        array.pop()
        array.pop()
    else:
        continue
print(2*count)

"""
"""
动态规划
dp[i][j]表示从i到j的字符串是不是有效的
str[i]="(" and str[i]=")" if dp[i+1][j-1]=true  就是true  感觉解决不出来
"""
"""
超时
def check(str):
    array = []
    count = 0
    for i in range(len(str)):
        try:
            t = array[len(array) - 1]
        except IndexError:
            t = ''
        array.append(str[i])
        if str[i] == ")" and t == "(":
            count += 1
            array.pop()
            array.pop()
        else:
            continue
    if 2*count==len(str):
        return True
    else:
        return False


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length=len(s)
        max_length=0
        for i in range(length):
            for j in range(i+1,length):
                tmp_str=s[i:j+1]
                if check(tmp_str):
                    max_length=max(max_length,len(tmp_str))
        return max_length
str=input().strip()
s=Solution()
print(s.longestValidParentheses(str))
"""
"""

解题思路：
 
1.需有一个变量start记录有效括号子串的起始下标，max表示最长有效括号子串长度，初始值均为0
 
2.遍历给字符串中的所有字符
 
    2.1若当前字符s[index]为左括号'('，将当前字符下标index入栈（下标稍后有其他用处），处理下一字符
 
    2.2若当前字符s[index]为右括号')'，判断当前栈是否为空
 
        2.2.1若栈为空，则start = index + 1，处理下一字符（当前字符右括号下标不入栈）
 
        2.2.2若栈不为空，则出栈（由于仅左括号入栈，则出栈元素对应的字符一定为左括号，可与当前字符右括号配对），判断栈是否为空
 
            2.2.2.1若栈为空，则max = max(max, index-start+1)
 
            2.2.2.2若栈不为空，则max = max(max, index-栈顶元素值)

"""





class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:return 0
        array = []  # 左括号入
        start=0#记录有效括号子串的起始下标，初始值为0
        i = 0
        max_length = 0
        while i < len(s):
            if s[i] == "(":
                array.append(i)

            elif s[i] == ")":
                if len(array) == 0:
                    #更换有效括号子串的起始下标(移到i的后一位)
                    #）（）（）
                    start =i+ 1

                else:
                    tmp=array.pop()
                    if len(array)==0:
                        #解决这种情况（）（）（）
                        max_length = max(max_length, i - start + 1)
                    else:
                        #最开始时遇到的((这两个必定连续
                        #这里的技巧性严重注意
                        #解决（（）（）
                        max_length=max(max_length,i-array[-1])

            i+=1
        return max_length

str=input().strip()
s=Solution()
print(s.longestValidParentheses(str))










