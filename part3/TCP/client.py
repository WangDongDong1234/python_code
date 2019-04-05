import socket

sk=socket.socket()   #买手机
sk.connect(('127.0.0.1',8080))#拨别人的号

sk.send(b'hello')#说话
ret=sk.recv(1024)
print(ret)

sk.send(bytes('中午吃什么'.encode('utf-8')))#继续说话中文
ret=sk.recv(1024)
print(ret.decode('utf-8'))
sk.close()
