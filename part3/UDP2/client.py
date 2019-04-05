import socket
import subprocess
sk=socket.socket(type=socket.SOCK_DGRAM)
ip_port=('127.0.0.1',8081)
sk.sendto('chilema'.encode('utf-8'),ip_port)

while True:
    ret, addr = sk.recvfrom(1024)
    cmd=ret.decode("utf-8")
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    sk.sendto(res.stdout.read(),ip_port)