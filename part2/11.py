class Parent:
    def __func(self):
        print("in parent func")

    def __init__(self):
        self.__func()


class Son(Parent):
    def __func(self):
        print("in son func")

s=Son()#in parent func