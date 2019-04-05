import pickle

# dic={1:(1,2,30),(111,2,3):"a"}
# pic_dic=pickle.dumps(dic)
# print(pic_dic)#b'\x80\x03}q\x00(K\x01K\x01K\x02K\x1e\x87q\x01KoK\x02K\x03\x87q\x02X\x01\x00\x00\x00aq\x03u.'
# new_dic=pickle.loads(pic_dic)
# print(new_dic)#{1: (1, 2, 30), (111, 2, 3): 'a'}
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student=Student('wdd',26)
#这里注意，pickle只能以字节的形式写入
with open('pickle_demo',mode='wb') as f:
    pickle.dump({'a':'a'},f)
    pickle.dump({'b':'b'}, f)
    pickle.dump({'c':'c'}, f)
    pickle.dump({'d':'d'}, f)

with open('pickle_demo',mode='rb') as f:
    #反序列化的时候必须确保这个类存在
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
