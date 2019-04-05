import socket
import struct
import json
sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
coon,addr=sk.accept()
length=coon.recv(4)
#将4个字节转成长度
length=struct.unpack("i",length)[0]
bytes_head=coon.recv(length)
heads_json=bytes_head.decode("utf-8")
heads=json.loads(heads_json)
print(heads)
filesize=heads['filesize']
buffer=1024#用4096会出错

with open(heads['filename'],mode='wb') as f:
    while filesize:
        if filesize>=buffer:
            content=coon.recv(buffer)
            filesize-=buffer
            f.write(content)
        else:
            content=coon.recv(filesize)
            f.write(content)
            break
coon.close()
sk.close()
