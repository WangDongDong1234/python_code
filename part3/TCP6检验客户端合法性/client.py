import socket
import os
import hmac

secret_key=b'wdd'
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
msg=sk.recv(1024)
h=hmac.new(secret_key,msg)
client_digest=h.digest()
sk.send(client_digest)