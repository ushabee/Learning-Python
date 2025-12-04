# class myname:
#  x=2
# p1= myname()
# print(p1.x)
class person:
    def __init__(self,name:str,age:int):
        self.name= name
        self.age= age 
    def __str__(self): #to print the values itself
      return f"Name:{self.name} ,Age:{self.age}"
p1 = person("jkjk",10)
print(p1)
    

