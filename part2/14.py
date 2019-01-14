class A:
    name="中国"
    count=1
    #为了得到类中静态变量
    def fu(self):
        return A.name+str(A.count)

    #使用静态方法得到类中的静态变量
    @classmethod
    def fun(cls):
        return cls.name+str(cls.count) #return A.name+str(A.count)万一类名改了的话，
                                       # 这里也要改，推荐用cls,cls等于
print(A.fu(11))#里面要传一个地址
print(A.fun())#采用类方法，不用传地址，它自动把类的地址传给self