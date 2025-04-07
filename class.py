class Student:
    college = "SWEC"

    def reading(self):#self is useful when we want to specify a particular object
        print("Hello")
        
s= Student()
print(s.college)
s.reading()
#In a class "self" keyword (it should be function parameter)is must while defining a function

