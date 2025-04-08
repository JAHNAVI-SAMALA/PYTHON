class A:
    _var = 2
    def __init__(self,name,pin):
        self.name = name
        self._pin=pin
    def showpin(self):
        return self._pin
obj = A("HI",1234)
print(obj.showpin())
