import time
# print(time.time())#1548760668.429915
# print(time.strftime('%Y-%m-%d %H:%M:%S'))#2019-01-29
# print(time.localtime())#time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, tm_hour=19, tm_min=20,
# # tm_sec=49, tm_wday=1, tm_yday=29, tm_isdst=0)
# time_obj=time.localtime()
# print(time_obj.tm_hour)
# #时间戳时间
# #15000000000
# #结构化时间
# t1=time.localtime(1500000000)
# print(t1)
# #格式化时间
# t2=time.strftime("%Y-%m-%d %H:%M:%S",t1)
# print(t2)
# #结构化时间
# t3=time.strptime(t2,"%Y-%m-%d %H:%M:%S")
# print(t3)
# #时间戳时间
# t4=time.mktime(t3)
# print(t4)
#计算本月一号的时间戳时间
t1=time.localtime()
t2=time.strftime("%Y-%m",t1)
t2+="-01"
t3=time.strptime(t2,"%Y-%m-%d")
print(t3)
t4=time.mktime(t3)
print(t4)


