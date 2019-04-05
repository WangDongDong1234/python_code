import re
# #第一个参数pattern表示正则表达式，string表示待匹配字符串
# ret=re.findall('\d',"111882211")
# print(ret)#参数  返回值类型:列表  返回值个数:1  返回值内容:所有匹配上的项
# ret2=re.search("\d+","111efsa 22")
# print(ret2)#<re.Match object; span=(0, 3), match='111'>
# print(type(ret2))#返回值类型:正则匹配结果的对象  返回值个数:1 如果匹配上了就返回对象
# print(ret2.group())#返回的对象通过group来匹配到第一个结果（只能取第一个）
# ret3=re.search("\s","sdaf111")
# print(ret3)#没有匹配上就返回为none

# ret4=re.search("\d+","%1996wdd0102")#不需要从头开始
# print(ret4)
# ret5=re.match("\d+","1996wdd0102")#match是从头开始匹配只要在search中的正则表达式前面加一个^效果就和match一样
# print(ret5)
# print(ret5.group())

# ret6="1996wdd0206wdd1314wdd1314".replace("1314","520")
# print(ret6)#print(ret6)替换之前需要知道替换的内容
# ret7=re.subn("\d+","520","1996wdd0206wdd1314wdd1314")
# print(ret7)#('520wdd520wdd520wdd520', 4)
# ret8="1996wdd0206wdd1314wdd1314".replace("1314","520",1)
# print(ret8)#print(ret6)替换之前需要知道替换的内容
# ret9=re.subn("\d+","520","1996wdd0206wdd1314wdd1314",2)
# print(ret9)#('520wdd520wdd1314wdd1314', 2)

# ret=re.split("\d+","alex80asdf50taibai90")
# print(ret)#['alex', 'asdf', 'taibai', '']

r=re.finditer("\d+","da111af452faf 187af af1222")
print(r)#<callable_iterator object at 0x00000049A0476B00>
for e in r:
    print(e.group())