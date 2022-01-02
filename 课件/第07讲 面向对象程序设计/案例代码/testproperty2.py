class Test:
    def __init__(self, value):
        self.__value = value	

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v

    value = property(__get, __set)

    def show(self):
        print(self.__value)
