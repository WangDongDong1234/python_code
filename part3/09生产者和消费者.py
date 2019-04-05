from multiprocessing import Queue
from multiprocessing import Process
import time

def producer(q):
    for i in range(50):
        q.put("做包子%s"%i)
        print("做包子%s"%i)


def consumer(q):
    for i in range(50):
        print(q.get().replace('做','吃'))

if __name__=='__main__':
    q=Queue(10)
    p=Process(target=producer,args=(q,))
    p.start()
    c=Process(target=consumer,args=(q,))
    c.start()