from core.user import User
import os

def login(msg):
    print(msg)

def register(msg):
    print(msg)
    #username password
    #创建一个属于这个用户的家目录，把用户名的密码写在userinfo
    #记录用户的初试磁盘配额，记录文件大小，记录用户当前所在的目录
    user_obj=User(msg['name'])#记录用户的信息
    os.mkdir(user_obj.home)#创建一个家目录
def upload(msg):
    print(msg)

def download(msg):
    print(msg)