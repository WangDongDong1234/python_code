import struct
import socket
import subprocess
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    cmd=sk.recv(1024).decode("utf-8")
    if cmd=="q":
        sk.send(b'q')
        break
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out=res.stdout.read()
    std_err=res.stderr.read()
    length=len(std_out)+len(std_err)
    print(length)
    num=struct.pack('i',length)
    sk.send(num)
    sk.send(std_out)
    sk.send(std_err)