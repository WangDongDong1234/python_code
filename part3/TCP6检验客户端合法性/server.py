import socket
import os
import hmac
sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
coon,addr=sk.accept()
secret_key=b'wdd'#钥匙必须是字节

def check(coon):
    #随机生成一个32位的字节
    msg=os.urandom(32)
    coon.send(msg)
    h=hmac.new(secret_key,msg)#钥匙和信息合起来加密
    digest=h.digest()#加密之后的东西
    client_digest=coon.recv(1024)
    result=hmac.compare_digest(digest,client_digest)#判断客户端和服务器加密后的是否一样
    return result

if check(coon):
    print("合法的客户")