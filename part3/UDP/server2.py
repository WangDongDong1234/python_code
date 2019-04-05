import socket
sk=socket.socket(type=socket.SOCK_DGRAM)#采用udp协议
sk.bind(('127.0.0.1',8080))
while True:
    ret,addr=sk.recvfrom(1024)
    print(ret.decode('utf-8'),addr)
    info=input("<<")
    sk.sendto(info.encode('utf-8'),addr)

sk.close()