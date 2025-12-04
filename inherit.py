class Person:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname = lname 
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):# inherits from the person
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduatedyear=year
    def welcome(self):
        print("welcome",self.fname,self.lname, "to the class of ",self.graduatedyear)
x= Student("Mike","Mandala",1990)
x.welcome()