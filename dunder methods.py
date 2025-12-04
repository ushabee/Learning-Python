# class Num:
#     def __init__(self,n:int)->None:
#         self.n=n
#     def __add__(self,other):
#         return self.n + other.n
# print(Num(10)+Num(20))

class dog:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def __str__(self):
         return f"name:{self.name}, age: {self.age}"
    def __repr__(self):
        return f"dog('{self.name}', {self.age})" 
Canine = dog("Max",5)
print(Canine)
print (repr(Canine))
