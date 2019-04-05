from multiprocessing import Process,Semaphore
import time
import random
def fun(num,sem):
    sem.acquire()
    print("%s进入房间"%num)
    time.sleep(random.rand(1,10))
    sem.release()
    print("%s离开房间"%num)


if __name__=='__main__':
    sem=Semaphore(4)
    for i in range(10):
        Process(target=fun,args=(i,sem)).start()
int