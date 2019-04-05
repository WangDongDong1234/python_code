import socket
import os
from multiprocessing import Process


def talk(coon):
    msg=coon.recv(1024)
    print(msg,os.getpid())
    coon.send(b'wdd')


if __name__=='__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8081))
    sk.listen()
    while True:
        coon,addr=sk.accept()
        #让子进程去聊天
        p=Process(target=talk,args=(coon,))
        p.start()

