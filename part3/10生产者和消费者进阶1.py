from multiprocessing import Process
from multiprocessing import Queue
import time
def producer(q,name):
    for i in range(10):
        time.sleep(2)
        q.put(name+str(i))
        print("生产了"+name)
    q.put(None)
    q.put(None)
    q.put(None)


def consumer(q,name):
    while True:
        t=q.get()
        if t==None:
            break
        time.sleep(1)
        print(name,"消费了"+t)

if __name__=='__main__':
    q=Queue()
    p1=Process(target=producer,args=(q,"骨头"))
    p1.start()
    p2 = Process(target=producer, args=(q, "红烧肉"))
    p2.start()
    c1=Process(target=consumer,args=(q,"wdd"))
    c1.start()
    c2 = Process(target=consumer, args=(q,"wn"))
    c2.start()
    c3 = Process(target=consumer, args=(q,"wdh"))
    c3.start()