"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
分5中情况
1..
2.a
3..*
4..a
5.a*
"""
s=input().strip()#输入的字符串
p=input().strip()#正则表达式
def check(s,p):
    i=0#对应的是匹配在s的坐标
    j=0#对应的是匹配在p的坐标
    length_s=len(s)
    length_p=len(p)
    if i>=length_s or j>=length_p:
        return False
    while i<length_s and j<length_p:
        #a
        if p[j]!="*" and p[j]!=".":
            if p[j]==s[i]:
                if i==length_s-1 and j==length_p-1:
                    return True
                i+=1
                j+=1
                if i >=length_s or j >=length_p:
                    return False
            else:
                #处理c#的情况
                if j+1<length_p and p[j+1]=="*":
                    j+=1
                else:
                    return False
        #.
        elif p[j]==".":
            #.后面不带其他值
            if j==length_p-1:
                if i==length_s-1:
                    return True
                else:
                    return False
            #.后面带一个
            elif j<length_p-1:
                #带一个字母
                if p[j+1]!="*":
                    i+=1
                    j+=1
                    if i >=length_s or j >=length_p:
                        return False
                #带一个*
                else:
                    #正好最后的长度是2
                    if j==length_p-2:
                        return True
                    else:
                        if s[i]==p[j+2]:
                            i+=1
                            j+=3
                            if i >=length_s or j >=length_p:
                                return False
                        else:
                            while j+2<length_p  and i<length_s and s[i]!=p[j+2]:
                                i+=1
                            i+=1
                            j+=3
                            if i >=length_s or j >=length_p:
                                return False
        elif p[j]=="*":
            #*正好是最后一个
            if j==length_p-1:
                while i<length_s and  s[i]==p[j-1]:
                    i+=1
                if i==length_s:
                    return True
                else:
                    return False
            elif j+1<length_p and s[i]==p[j+1]:
                i+=1
                j+=2
                if i >=length_s or j >=length_p:
                    return False
            else:
                while i<length_s and  s[i]==p[j-1]:
                    i+=1
                if i<length_s:

                    j+=1
                    if i >=length_s or j >=length_p:
                        return False
                else:
                    return False
# if check(s,p):
#     print("true")
# else:
#     print("false")

#########################
"""
这道题分的情况的要复杂一些，需要用递归Recursion来解：

- 若p为空，且s也为空，返回true，反之返回false

- 若p的长度为1，且s长度也为1，且相同或是p为'.'则返回true，反之返回false

- 若p的第二个字符不为*，且此时s为空则返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配

- 若p的第二个字符为*，s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母

- 返回调用递归函数匹配s和去掉前两个字符的p的结果
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();
        if (p.size() == 1) {
            return (s.size() == 1 && (s[0] == p[0] || p[0] == '.'));
        }
        if (p[1] != '*') {
            if (s.empty()) return false;
            return (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1));
        }
        while (!s.empty() && (s[0] == p[0] || p[0] == '.')) {
            if (isMatch(s, p.substr(2))) return true;
            s = s.substr(1);
        }
        return isMatch(s, p.substr(2));
    }
};
"""
def check2(s,p):
    if len(p)==0:
        if len(s)==0:
            return True
        else:
            False
    if len(p)==1:
        if len(s)==1 and (s[0]==p[0] or p[0]=='.'):
            return True
        else:
            return False

    while len(s)>0 and (s[0]==p[0] or p[0]=="."):
        if check2(s,p[2:]):
            return True
        s=s[1:]
    return check2(s,p[2:])
print(check(s,p))
print(check2(s,p))
"""
class Solution(object):
    def isMatch(self, s, p):
        
        #:type s: str
        #:type p: str
        #:rtype: bool
        
        # 判断匹配规则是否为空
        if p == "":
            # p为空的时候，判断s是否为空，则知道返回True 或 False
            return s == ""
        # 判断匹配规则是否只有一个
        if len(p) == 1:
            # 判断匹配字符串长度是否为1，和两者的第一个元素是否相同，或匹配规则使用.
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        # 匹配规则的第二个字符串不为*，当匹配字符串不为空的时候
        # 返回 两者的第一个元素是否相同，或匹配规则使用. and 递归新的字符串(去掉第一个字符的匹配字符串 和 去掉第一个字符的匹配规则)
        if p[1] != "*":
            if s == "":
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        # 当匹配字符串不为空 and (两者的第一个元素是否相同 or 匹配规则使用.)
        while s and (s[0] == p[0] or p[0] == '.'):
            # 到了while循环，说明p[1]为*，所以递归调用匹配s和p[2:](*号之后的匹配规则)(这种情况*取0的时候)
            # 用于跳出函数，当s循环到和*不匹配的时候，则开始去匹配p[2:]之后的规则
            if self.isMatch(s, p[2:]):
                return True
            # 当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，循环
            s = s[1:]
        # 假如第一个字符和匹配规则不匹配，则去判断之后的是否匹配
        return self.isMatch(s, p[2:])


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "a"))  # false
    print(s.isMatch("aa", "aa"))  # true
    print(s.isMatch("aaa", "aa"))  # false
    print(s.isMatch("aa", "a*"))  # true
    print(s.isMatch("aa", ".*"))  # true
    print(s.isMatch("ab", ".*"))  # true
    print(s.isMatch("aab", "c*a*b"))  # true
    

"""



