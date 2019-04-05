import re
#匹配负数
# ret=re.findall("-0\.\d+|[1-9]\d*(\.\d+)?","-1adsfas-200")
# # print(ret)#['', '']  这里是（）里的优先匹配因为括号里的没有匹配的上所以是空但是照样匹配了两个（带了（）只显示括号里的）
# # ret2=re.findall("www.baidu.com|www.oldboy.com","www.baidu.com")
# # print(ret2)#['www.baidu.com']
# # ret3=re.findall("www.(?:baidu|oldboy).com","www.baidu.com")
# # print(ret3)#baidu
# #
# # ret4=re.split("\d+","wdd26wn22we23")
# # print(ret4)#['wdd', 'wn', 'we', '']
# # ret5=re.split("(\d+)","wdd26wn22we23")
# # print(ret5)#['wdd', '26', 'wn', '22', 'we', '23', '']

ret=re.search("\d+(\.\d+)(\.\d+)(\.\d+)(\.\d+)?","1.2.3.4")
print(ret.group())#1.2.3.4
print(ret.group(0))#1.2.3.4
print(ret.group(1))#.2
print(ret.group(2))#.3
print(ret.group(3))#.4
print(ret.group(4))#None
