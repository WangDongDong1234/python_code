#基于tcp实现远程执行命令
#server端发送命名
import socket
sk=socket.socket()#买手机
sk.bind(('127.0.0.1',8080))#绑卡

sk.listen()#监听
coon,addr=sk.accept()#连接
while True:
    cmd=input()
    coon.send(cmd.encode('gbk'))
    ret=coon.recv(1024).decode('gbk')#操作系统是以gbk码表发过来的
    print(ret)
coon.close()
sk.close()