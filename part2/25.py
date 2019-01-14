class A:
    def __del__(self):#析构方法
        print("执行析构方法")

a=A()
del a#先执行__del__方法，最后执行del a  理由如果先执行的是del a的话，对象没了就没有东西传给__init__中的self
# print(a)


class Myfile:
    def __init__(self,filepath):
        self.f=open(filepath)

    def read(self):
        self.f.read()

    def __del__(self):#是去归还/释放一些在创建对象的时候借用的一些资源
        self.f.close()#什么时候触发这个方法，当你意识到要删除的时候，手动执行del
                      #或者在python解释器的垃圾回收机制回收这个对象所占得内存的时候