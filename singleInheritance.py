class A:
    rollno = 1234

    def wish(self):
        print("HI")

class B(A):
    name = "JOE"

child = B()
print(child.name)
print(child.rollno)
child.wish()
