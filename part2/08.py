from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):  #抽象类接口类
    @abstractmethod
    def pay(self):
        pass

class Alipay(Payment):
    def __init__(self,money):
        self.money=money
    def pay(self):
        print("使用支付宝支付%s" %self.money)


a=Alipay(200)
a.pay()

class Str:
    def index(self):
        pass

class List:
    def index(self):
        pass

class Tuple:
    def index(self):
        pass