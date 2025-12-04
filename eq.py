class account:
    def __init__(Self,name,id):
        Self.name = name
        Self.id = id
    # def __eq__(self, other):
    #     return self.id == other.id
    
p1: account= account(name="meow",id=400)
p2: account = account(name="meow",id=400)               
print(p1==p2)
 