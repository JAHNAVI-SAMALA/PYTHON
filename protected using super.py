#super keyword
class A:
    _var = 2

class B(A):
    def test(self):
        return super()._var

obj = B()
print(obj._var)
