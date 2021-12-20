class Vehicle():
    def __init__(self,mod=None,fuel=None):
        self.model=mod
        self.fuel=fuel
    
    @staticmethod
    def display(car,brand):#Vehicle.display()
        pass
        print(car,brand)

    def display(self):
        
        print(self.model,self.fuel)        
# class Air(Vehicle):
# class water(Vehicle):
# class Land(Vehicle):

class TwoWheeler(Vehicle):
    def __init__(self,mod,fuel,license,colour,wheel=2):
        self.license=license
        self.colour=colour
        #self.model=mod
       # self.fuel=fuel
        super().__init__(mod,fuel)
        self.wheel=wheel
    
    def display(self):
        super().display()
        print(self.license,self.colour)
    
#instance or object
v1=TwoWheeler('123','petrol','123es','Red')
v1.display()
print('============================')
v1.fuel = '220'
v1.display()

# def swap_case():   
#     answer = input('Write something')
#     for i in answer:
#         if i.islower():
#             print(i.upper(),end='')

#         else:
#             print(i.lower(),end='')    
# swap_case()            



# myList = [1,2]
# yourList = myList[:]#[0::]
# yourList.append(7)
# print(myList)
# print(yourList)