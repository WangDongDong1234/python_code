#client执行命令
import socket
import subprocess
sk=socket.socket()
sk.connect(("127.0.0.1",8080))
while True:
    cmd=sk.recv(1024).decode('utf-8')
    print(cmd)
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out=res.stdout.read()#从管道里读的话只能读一次
    std_err=res.stderr.read()
    sk.send(str(len(std_out)+len(std_err)).encode('utf-8'))
    statue=sk.recv(1024).decode('utf-8')
    sk.send(std_out)
    sk.send(std_err)
sk.close()