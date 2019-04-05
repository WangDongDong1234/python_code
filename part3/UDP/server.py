import socket
sk=socket.socket(type=socket.SOCK_DGRAM)#如果用udp需要带这个参数type=socket.SOCK_DGRAM
                                     #DGRAM datagram数据报
sk.bind(('127.0.0.1',8080))

#不需要监听，直接连接
msg,addr=sk.recvfrom(1024)
print(msg.decode('utf-8'),addr)
sk.sendto(b'bye',addr)
sk.close()

