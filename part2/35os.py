import os
"""
os.getcwd()  #获取当前工作目录，即当前Python脚本工作的目录路径（在那个地方执行这个文件，getcwd的结果就是那个路径）
             #__file__才是模块的位置
os.chdir()   #改变当前脚本的工作目录，相当于shell下cd(即修改getcwd的位置，不推荐用)
os.curdir    #返回当前路径.(暂时没用)
os.pardir    #获取当前目录的父目录字符串名..

os.makedirs('dirname1/dirname2'，exist_ok=True)#可生成多层递归目录，exist_ok默认是false(如果目录存在的话就报已存在)
os.removedirs('dirname1') #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依次类推
os.mkdir()    #每次只能创建单级目录（单级目录的上一层必须存在）（目录必须创建，存在就报错）
os.rmdir()  #删除目录之前，必须删除文件（使用os.remove()删除文件）
os.mkdir()   
os.listdir() #列出当前文件目录
os.remove()  #删除文件
os.rename()  #文件重命名

os.stat()   #查看文件的信息
os.sep   #当前你所在的操作系统的目录分隔符 \  /
         os.sep.join(base_path,s)
         if os.name=='nt':
         '\\'.join(base_path,s)
         else:
         "/".join(base_path,s)
os.linesep  #输出当前平台使用的行终止符，win下为"\t\n",linux下位"\n"
            #print([os.linesep])#['\r\n']要放到[]中查看
os.pathsep  #输出用于分割文件路径的字符串（环境变量里）win下位;,linux下为:
os.name     #输出字符串致死当前使用的平台。win->"nt",linux->"posix"
os.system() #执行操作系统命令（删除某个文件，copy一个文件，不关心结果）
os.popen()  #执行操作系统命令，将结果读到内存中（和system的区别就像exec和eval的区别  关心结果）
os.environ  #系统的环境变量
"""

def print_path(path,n):
    files=os.listdir(path)
    for item in files:
        newfile = os.path.join(path, item)
        if os.path.isdir(newfile):
            print_path(newfile,n+1)
        else:
            print("-"*n,item)
print_path("D:\wdd",0)

