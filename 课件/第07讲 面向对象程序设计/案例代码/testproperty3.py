class Test:
    def __init__(self, value):
        self.__value = value

    def __getValue(self):
        return self.__value

    def __setValue(self, v):
        self.__value = v

    def __delValue(self):
        del self.__value

    value = property(__getValue, __setValue, __delValue)

    def show(self):
        print(self.__value)
