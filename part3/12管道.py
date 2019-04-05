from multiprocessing import Pipe
from multiprocessing import Process
from multiprocessing import Lock
import time

#用管道实现生产者和消费者
def producer(p,l):
    parent, son=p
    son.close()
    for i in range(10):
        parent.send('hello'+str(i))
    parent.close()
def consumer(p,l,name):
    parent, son = p
    parent.close()
    while True:
        try:
            l.acquire()
            print(son.recv()+str(name))
            l.release()
            time.sleep(name)
        except EOFError:
            l.release()#报错后要释放锁
            son.close()
            break
if __name__=='__main__':
    parent,son=Pipe()
    l=Lock()
    p_p=Process(target=producer,args=((parent,son),l))
    p_p.start()
    c1=Process(target=consumer,args=((parent,son),l,1))
    c1.start()
    c2 = Process(target=consumer, args=((parent, son), l,2))
    c2.start()
    parent.close()
    son.close()

