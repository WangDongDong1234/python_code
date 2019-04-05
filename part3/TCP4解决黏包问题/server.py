#基于tcp实现远程执行命令
#server端发送命名
import socket
sk=socket.socket()#买手机
sk.bind(('127.0.0.1',8080))#绑卡

sk.listen()#监听
coon,addr=sk.accept()#连接
while True:
    cmd=input()
    coon.send(cmd.encode('utf-8'))
    num=coon.recv(1024).decode('utf-8')#收到要接受字节的长度

    coon.send('ok'.encode('utf-8'))
    ret=coon.recv(int(num)).decode('gbk')#操作系统是以gbk码表发过来的
    print(ret)
coon.close()
sk.close()