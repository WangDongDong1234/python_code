import socket
sk=socket.socket()         #买手机
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#避免服务重启的时候报address already in use
sk.bind(('127.0.0.1',8080))#绑定手机卡,接受元组（ip,port）
sk.listen()                #监听
conn,addr=sk.accept()      #接受别人电话，conn是连接connection,addr地址是对面的电话号码

ret=conn.recv(1024)            #听被人说话（接受1024的整数倍）
print(ret)                     #答应别人说的话
conn.send(b'hi')            #我和别人说话（这里必须传一个byte类型）

ret=conn.recv(1024)         #继续接收
print(ret.decode('utf-8'))  #这里是中文
conn.send(bytes("大碗面".encode('utf-8')))
conn.close()               #挂电话
sk.close()                 #关手机
