class Student:
    def __init__(self):
        self.name=" "
        self.rollno="0"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printValues(self):
        print(self.name)
        print(self.rollno)
S1=Student("abc","123")
S1.printValues()