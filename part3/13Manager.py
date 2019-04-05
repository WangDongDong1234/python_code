#Manager是一个类，就提供了可以进行IPC（进程之间通信）通信
#提供了很多数据类型dict,list
from multiprocessing import Manager
from multiprocessing import Process

def work(d):
    #print(d)
    d['count']-=1

if __name__=='__main__':
    m=Manager()
    d=m.dict()#共享的数据
    d['count']=100
    l=[]
    for i in range(100):
        p=Process(target=work,args=(d,))
        p.start()
        l.append(p)
    [p.join() for p in l]#这是异步执行，知道所有的子进程都结束
    print(d)
