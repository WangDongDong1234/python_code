from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self,arg1,arg2,arg3):
        super().__init__()
        self.arg1=arg1
        self.arg2=arg2
        self.arg3=arg3

    def run(self):
        print('子进程',os.getpid(),self.arg1,self.arg2,self.arg3)

if __name__=='__main__':
    p=MyProcess(3,2,1)
    p.start()#会调用run方法
    print('主进程',os.getpid())