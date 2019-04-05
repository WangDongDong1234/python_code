import socket

sk=socket.socket()#买手机
sk.bind(('127.0.0.1',8080))  #绑定手机卡
sk.listen()    #监听
conn,addr=sk.accept()   #接受别人电话
while True:
    ret=conn.recv(1024).decode('utf-8')
    print(ret)
    if ret=='bye':
        conn.send(b'bye')
        break
    info=input("<<<")
    conn.send(bytes(info.encode('utf-8')))
conn.close()
sk.close()
