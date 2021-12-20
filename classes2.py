class Vehicle():
    def __init__(self,mod,fuel):
        self.model=0
        self.fuel=0
    
    @staticmethod
    def display(self,num,number):#Vehicle.display()
        pass
        self.num = num
        self.number = number

class Trucks(Vehicle):
    def __init__(self,alpha,device,mod,fuel):
        self.alpha = alpha
        self.device = device
        super().__init__(mod,fuel)
        print(alpha,device)
        
        

    def food(self,x,y):
        print(self.device,self.model)
v1 = Trucks('a','laptop','audi','shell')
v1.fuel = 'indian oil'

v2 = Trucks('b','Monitor','bmw','indian oil')
v1.food('5','6')
print(v2.alpha,'This')
v1.alpha = 'Lohith'
v2.alpha  = 'Aditya'
print(v2.alpha)


# class Device():
#     def __init__(self,x,y):
        
#         self.x = 'Mahindra'
#         self.y = 'Audi'
#         # print(x * y)
#         # print(self.x,self.y)

        
#     def alpha(self,q,r):
#         self.x = 'Nothing'
#         self.y = 'Everything'
#         # print(q*r)
#         # print(self.x,self.y)
        

#     def speed(self,gear,clutch):
#         print(gear)
#         print('The car has {} gears and it is manual'.format(gear))


# result = Device(9,10)
# result.alpha(9 , 8)
# result.speed('8','gears')
# class Thing(Device):
#     def __init__(self, x, y,l,m) :
#         self.l = x
#         self.m = y
#         super().__init__(x,y)
#         print(x * y * l * m)

#     def thing(self,time= None,date = None):
#         self.time = 0
#         self.time = 0
        
        



# menu = Thing(1,2,3,4)
# menu.speed('8 O clock','11:45')
# menu.speed()
# menu.alpha(10,20)
# Device.speed()
# Thing.thing()

# def trans(x = 1,y =3,z = 20 ):
#     print(x * y * z)



# trans(x = 5,y = 10,z = 30)
    

