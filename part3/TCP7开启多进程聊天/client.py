import socket
sk=socket.socket()
sk.connect(("127.0.0.1",8081))
sk.send(b'hello')