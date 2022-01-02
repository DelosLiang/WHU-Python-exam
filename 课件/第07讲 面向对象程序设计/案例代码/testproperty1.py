class Test:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):    #只读，无法修改和删除
        return self.__value
