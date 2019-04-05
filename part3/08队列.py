#from multiprocessing import Queue
#进程之间的同信通过multiprocessing的Queue模块
#队列有两种创建方式，第一种不传参数，这个队列没有长度限制，传参数，创建一个有最大长度的队列
#提供两个重要方法:put get
#对于不定长的队列，put不会阻塞，对于定长的队列会阻塞
#qsize不一定准确
#主线程和子线程通信
from multiprocessing import Queue
from multiprocessing import Process
def put(q):
    q.put("hello")

def get(q):
    t=q.get()
    print(t)

if __name__=='__main__':
    q=Queue()
    p1=Process(target=put,args=(q,))#开启一个子进程向队列中放数据
    p1.start()
    p2 = Process(target=get, args=(q,))  # 开启一个子进程从队列中取数据
    p2.start()

