class A:
    def wish(self):
        print("hey")
class B(A):
    def wish(self):
        print("hello")

child = B()
child.wish()
"""if method names are same then wish() in class B is executed if diff acquires from class A
this is an example of polymorphism
same function name in both parent as well as child class but different implementation is called method overriding
"""
