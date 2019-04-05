import socket
sk=socket.socket()  #买手机
sk.connect(('127.0.0.1',8080))  #拨号
while True:
    info=input("<<")
    sk.send(info.encode('utf-8'))
    ret=sk.recv(1024).decode('utf-8')
    print(ret)
    if ret=='bye':
        sk.send(b'bye')
        break
sk.close()

