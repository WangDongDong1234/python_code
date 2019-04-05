#from multiprocessing import Event
# e=Event()#实例化一个事件  标志/交通信号
# e.wait()#刚实例化出来一个事件对象，默认的信号是阻塞信号/默认是红灯，执行到wait，要先看灯，绿灯
#         #行红灯停，如果在停的过程中灯绿了就变成非阻塞
# e.set()#将标志变成非阻塞/交通变绿灯
# e.clear()#将标志编程阻塞，交通变红灯
# e.is_set()#看事件是否阻塞，True就是绿灯，False是红灯
from multiprocessing import Process
from multiprocessing import Event
import time

def light(e):
    while True:
        if e.is_set():
            print('是绿灯')
            time.sleep(3)
            e.clear()
        else:
            print('是红灯')
            time.sleep(5)
            e.set()
def car(i,e):
    e.wait()
    print('%s车通过'%i)
if __name__=='__main__':
    e=Event()#红路灯(默认开启的是红灯)
    light_process=Process(target=light,args=(e,))
    light_process.start()
    for i in range(10):
        if i%3==0:
            time.sleep(2)
        car_process=Process(target=car,args=(i,e))
        car_process.start()
