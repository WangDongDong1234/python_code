import re
# #取出整数
# # ret=re.findall("\d+","1-2*(60+(-40.35/5)-(-4*3))")
# # print(ret)#['1', '2', '60', '40', '35', '5', '4', '3']
# # ret1=re.findall("\d+(?:\.\d+)|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# # print(ret1)#['1', '2', '60', '', '5', '4', '3']
# re1=re.findall(">(\w+)<","<a>haha</a>")
# print(re1)#['haha']
# re2=re.findall("<(\w+)>","<a>haha</a>")
# print(re2)#['a']
#
# ret1=re.search("<(\w+)>(\w+)</(\w+)>","<a>haha</a>")
# print(ret1.group())#<a>haha<\a>
# print(ret1.group(1))#a
# print(ret1.group(2))#haha
# print(ret1.group(3))#a
# ret2=re.search(r"<(?P<name>\w+)>(?P<body>\w+)</(?P=name)>","<a>haha</a>")
# print(ret2.group("name"))
# print(ret2.group("body"))
# #
# string="\\n"
# print(string)
# pattern1=r"\\n"
# res=re.search(pattern1,string)
# print(res.group())
# pattern2="\\\\n"
# res2=re.search(pattern2,string)
# print(res2.group())


res=re.split("\d+(\w+)","1996wdd0203")
print(res)#['', 'wdd0203', '']  (优先显示)
list="1996wdd0206".split("1996wdd0206")
print(list)#['', '']