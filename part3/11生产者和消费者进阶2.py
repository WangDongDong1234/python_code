from multiprocessing import JoinableQueue
#put  q.join 等待生产者的所有数据都被消费者执行task_done,我才停住
#get 后 处理数据  然后task_done告诉生产者消费完了 接着和q通信
from multiprocessing import Process
import time
def producer(q,name):
    for i in range(10):
        time.sleep(2)
        q.put(name+str(i))
        print("生产了"+name)
    q.join()#q是一个队列，我生产完了没有结束在等待消费者发送task_done(所有的数据都接收了task_done)
def consumer(q,name):
    while True:
        t=q.get()
        if t==None:break
        time.sleep(1)
        print(name,"消费了"+t)
        q.task_done()
if __name__=='__main__':
    q=JoinableQueue()
    p1=Process(target=producer,args=(q,"骨头"))
    p1.start()
    p2 = Process(target=producer, args=(q, "红烧肉"))
    p2.start()
    c1=Process(target=consumer,args=(q,"wdd"))
    c1.daemon=True#设置成守护进程
    c1.start()
    c2 = Process(target=consumer, args=(q,"wn"))
    c2.daemon = True
    c2.start()
    c3 = Process(target=consumer, args=(q,"wdh"))
    c3.daemon = True
    c3.start()
    p1.join()#等待p1执行完毕
    p2.join()#等待p2执行完毕