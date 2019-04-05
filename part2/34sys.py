import sys #和python解释器打交道
# print(sys.path)#寻找模块的路径
# print(sys.modules)#存放了多少个模块路径
# print(sys.platform)#win32
# #sys.exit()
# print(sys.argv)
#列表
#第一元素  是执行这个文件的时候 写在python命令后的第一个值
arg0=sys.argv[1]
arg1=sys.argv[2]
if arg0=="wdd" and arg1=="123":
    print("success")
else:
    print("fail")
    exit()