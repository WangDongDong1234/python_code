import time
from multiprocessing import Process

# def cal_time():
#     while True:
#         #这个进程一旦执行就结束不了
#         time.sleep(1)
#         print('过去了一秒')
#
# if __name__=='__main__':
#     p=Process(target=cal_time)
#     #将这个进程设置为守护进程,一定要在开启线程之前
#     p.daemon=True
#     p.start()
#     for i in range(100):
#         time.sleep(0.1)
#         print(i*'*')
#     #判断进程是否活着，True代表活着，false代表不在了
#     p.is_alive()
#     #结束一个进程
#     p.terminate()
class MyProcess(Process):
    def run(self):
        print(self.pid,self.name)
if __name__=='__main__':
    p=MyProcess()
    p.start()
    print(p.pid)