import socket
import struct

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
coon,addr=sk.accept()
while True:
    cmd=input("<<")
    if cmd=="q":
        coon.send('q')
        break
    coon.send(cmd.encode('utf-8'))
    num=coon.recv(4)
    num=struct.unpack('i',num)[0]
    print(num)
    res=coon.recv(int(num)).decode('gbk')
    print(res)