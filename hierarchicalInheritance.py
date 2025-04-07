class A:
    rollno = 1234

    def wish(self):
        print("HI")

class B(A):
    name = "JOE"
class C(A):
    branch = "CSE"
child1 = B()
child2 = C()
print(child1.name)#attribute of B
print(child1.rollno)#attribute of A
child1.wish()#method of A
print(child2.branch)#attribute of C
print(child2.rollno)#attribute of A
child2.wish()#method of A

