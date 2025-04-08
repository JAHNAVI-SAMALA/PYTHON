class A:
    def __init__(self,name,pin):
        self.__pin=pin
    def showpin(self):
        return self.__pin
obj = A("HI",1234)
print(obj.showpin())
#private access modifier
