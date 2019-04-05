#client执行命令
import socket
import subprocess
sk=socket.socket()
sk.connect(("127.0.0.1",8080))
while True:
    cmd=sk.recv(1024).decode('gbk')
    print(cmd)
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    sk.send(res.stdout.read())
sk.close()