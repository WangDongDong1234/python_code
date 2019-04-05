import socket
sk=socket.socket()
sk.connect(("127.0.0.1",8080))
while True:
    info=input("我是客户端1")
    sk.send(info.encode('utf-8'))
    ret=sk.recv(1024).decode('utf-8')
    if ret=='q':
        sk.send(b'q')
        break
    print(ret)