# import os
# import time
# print(os.getpid())  #获取当前运行的python程序的进程id  process id
# print(os.getppid()) #parent process id 获取当前进程的父id

from multiprocessing import Process
import os
# def func(money):
#     print('取钱:%d'% money)
#     print(123)
#
# if __name__=='__main__':
#     p=Process(target=func,args=(1,))#创建一个进程，这个进程去执行目标函数
#     print('开始取钱',os.getppid())
#     p.start()#开始执行这个进程
#     p.join()
#     print('取完钱', os.getppid())
def fun(i):
    print('%d 子进程%s干的事情'%(i,os.getpid()))

if __name__=='__main__':
    p_lst=[]
    for i in range(10):
        p=Process(target=fun,args=(i,))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
    print('主进程')#这样的话所有进程都执行完才显示主进程