import socketserver#对server的一次封装，是他能同时支持多个客户端的请求
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #print(self.request.recv(1024).decode("utf-8"))#这里的self.request相当于coon
        while True:
            ret=self.request.recv(1024).decode("utf-8")
            if ret=='q':
                self.request.close()
                break
            print(ret)
            info=input("服务端<<<")
            self.request.send(info.encode("utf-8"))

if __name__=='__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)#执行了绑定，监听，接收
    #永久开启这个服务，接受多个客户端的请求
    server.serve_forever()