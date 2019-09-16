"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
有几条须注意掌握：
1、基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
2、不能把基本数字V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
3、V 和X 左边的小数字只能用Ⅰ。
4、L 和C 左边的小数字只能用X。
5、D 和M 左边的小数字只能用C。
注意IXC，单个连用的话不超过3个，放在大数左边的只有一个
"""
luoma=input()
dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
i=0
sum=0
while i<len(luoma)-1:
    if i<len(luoma)-1 and dict.get(luoma[i])>=dict.get(luoma[i+1]):
        sum+=dict.get(luoma[i])
        i+=1
    if i<len(luoma)-1 and dict.get(luoma[i])<dict.get(luoma[i+1]):
        sum=sum+dict.get(luoma[i+1])-dict.get(luoma[i])
        i+=2
if i<len(luoma):
    sum+=dict.get(luoma[i])
print(sum)


