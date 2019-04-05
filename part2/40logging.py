lst=['登陆','注册','取消']
for i in enumerate(lst,1):
    print(i[0],i[1])


# try:
# #     num = int(input())
# #     print(lst[num - 1])
# # except ValueError:
# #     print("请输入一个数字")
# # except IndexError:
# #     print("请输入1-3")
# try:
#     num = int(input())#输入5
#     print(lst[num - 1])#产生于一个异常将这个异常对象给e
# except Exception as e:
#     print(type(e),e,e.__traceback__.tb_lineno)

# try:
#     num = int(input())
#     print(lst[num - 1])
# # except ValueError:print("请输入一个数字")
# # except IndexError:print("请输入1-3")
# except (IndexError,ValueError) as e:#用元组取代上面的分支语句
#     print(e)

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass  #只要没有异常产生就会执行else
# finally:#异常没有被处理会报错终止程序运行，用了finally会继续（适合做资源归还工作）
#     pass#无论无何都会执行finally

#主动抛异常
# try:
#     num=int(input('>>'))
# except ValueError:
#     print("在出现了异常之后做点什么，再让它抛异常")
#     raise #原封不动的抛出try语句中出现的异常

# class MyException(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#
# raise MyException("这是我自己定制的异常")

assert True#是True就往下走
assert False#是False就报异常