class A:
    def __init__(self,name,pin):
        self.pin=pin
    def showpin(self):
        return self.pin
obj = A("HI",1234)
print(obj.showpin())
