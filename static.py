# class calculator:
#     without staticmethod
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         return self.a+self.b
    
# addition = calculator(2,3)
# print(addition.add())
#with static methpd
class calc:
    @staticmethod
    def add(a,b):
        return a+b
ca = calc.add(3,4)
print(ca)   
    