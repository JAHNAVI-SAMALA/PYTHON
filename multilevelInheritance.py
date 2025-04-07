class A:
    rollno = 1234

    def wish(self):
        print("HI")

class B(A):
    name = "JOE"
class C(B):
    branch = "CSE"

child = C()
print(child.name)#attribute of B
print(child.branch)#attribute of C
print(child.rollno)#attribute of A
child.wish()#method of A
