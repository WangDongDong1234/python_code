#struct模块
#什么事固定长度的byte
#为什么要转成固定长度的bytes(struct将一个int（i int integer 4）转成4个字节，我接受这4个字节然后转成对应的数)
import struct
ret=struct.pack('i',4096000)#b'\x00\x80>\x00'
print(ret)#b'\x00\x10\x00\x00'
num=struct.unpack('i',ret)
print(num)#(4096,)


head={'filename':'test','filesize':409600,'filetype':'txt','filepath':r'\user\bin'}
#client               server
#先发送报头的长度        #先接收4个字节
#send(head)#报头     #根据这四个字节获取报头
#send(file)#报文     #从报头中回去filesize,然后根据filesize接受文件


#sk.sendall("hello world")

# buffer="hello world\n"
# while buffer:
#     bytes=sk.send(buffer)
#     buffer=[bytes:]
