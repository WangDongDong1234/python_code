import socket
import os
import json
import struct
sk=socket.socket()
sk.connect(('127.0.0.1',8080))

#报头
heads={'filepath':r'D:\搜狗高速下载',
       'filename':r'VID_20180901_153135.mp4',
       'filesize':None}
filesize=os.path.getsize(os.path.join(heads['filepath'],heads['filename']))
heads['filesize']=filesize
#将字典转成json字符串
heads_json=json.dumps(heads)
#将字符串转成字节
bytes_head=heads_json.encode("utf-8")
#使用struct将字节数转成4个字节
length=struct.pack("i",len(bytes_head))
sk.send(length)
sk.send(bytes_head)
file_path=os.path.join(heads['filepath'],heads['filename'])
buffer=1024
with open(file_path,mode='rb') as f:
       while filesize:
              print(filesize)
              if filesize>=buffer:
                     content=f.read(buffer)
                     sk.send(content)
                     filesize-=buffer
              else:
                     content=f.read(filesize)
                     sk.send(content)
                     break
sk.close()