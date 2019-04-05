from multiprocessing import Process,Lock
import json
import time
import random
def func(num,lock):
    lock.acquire()
    #查看票
    with open('ticket',mode="r",encoding="utf-8" )as f:
        ticket_num=json.load(f)['count']
        print(ticket_num)
        print("当前进程%s,查看票数%s"%(num,ticket_num))
    time.sleep(random.random())
    #取票
    if ticket_num>0:
        with open('ticket',mode='w',encoding='utf-8')as f:
            json.dump({'count':ticket_num-1},f)
            print("当前进程%s买到票了"%(num))
    else:
        print("当前进程%s没有买到票了" % (num))
    lock.release()

if __name__=='__main__':
    lock=Lock()
    for i in range(10):
        p=Process(target=func,args=(i,lock))
        p.start()