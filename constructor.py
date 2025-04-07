class Student:
    college = "SWEC"#class attribute

    def __init__(self,name,rollno):#constructor
        self.name = name#instance attributes
        self.rollno = rollno
        
    def reading(self):#method
        print("Hello")
        
s= Student("Joe",1234)
print(s.name)
print(s.rollno)
print(s.college)
s.reading()
