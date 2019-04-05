import sys
print(sys.modules)
def fun():
    print("hello")

myfile=sys.modules[__name__]#深坑所以以后用__name__取代__main____main__是执行的那个文件的地址

getattr(myfile,"fun")()