from abc import ABC , abstractmethod
class A:
    @abstractmethod
    def test(self,a):
        pass
obj = A()


from abc import ABC , abstractmethod
class Bike(ABC):
    @abstractmethod
    def gear(self):
        pass
obj = Bike()


from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
    class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius
        def area(self):
            return 3.14 * self.radius * self.radius
        def perimeter(self):
            return 2*3.14*self.radius
obj = Circle(2.5)
print(obj.area())
print(obj.perimeter())
