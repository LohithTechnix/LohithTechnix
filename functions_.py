def fun1(text):
    return text+text
def fun2(text):
    return text.upper()

def fun3(func,text):
    print(func(text))
    
fun3(fun1,12)
fun3(fun2,'qwerty')

# 6=n
# 12, 14 16 17 62 66 = n integers
# sum of all
# 21
# '''n = int(input())
# print(n)
# num=[]
# sum=0
# m = input()
# print(m.split()[2])
# for i in m.split():
#     num.append(int(i))
# print(num)
# for i in num:
#     sum+=i
# print(sum)'''
#default parameters with init function and inheritance
'''def sum(a,b=10):
    print(a+b)
sum('12','10')
def sum(a,b):
    print(a+b)
sum(12,12)'''
# class Vehicle():
#    def __init__(self,mod=None,fuel=None):
#     self.model=0
#     self.fuel=0
    
#     @staticmethod
#     def display(car,brand):#Vehicle.display()
#         pass
#         print(car,brand)
# class Air(Vehicle):
# class water(Vehicle):
# class Land(Vehicle):

# class TwoWheeler(Vehicle):
#     def __init__(self,mod,fuel,license,colour,wheel=2):
#         self.license=license
#         self.colour=colour
#         #self.model=mod
#        # self.fuel=fuel
#         super().__init__(mod,fuel)
#         self.wheel=wheel
    
#     def display(self):
#         super().display()
#         print(self.license,self.colour)
    
# #instance or object
# v1=TwoWheeler('123','petrol','123es','Red')
# v2=Vehicle()
# v2.model='145'
# v2.fuel="deisel"
# #v1.display()
# v3 = TwoWheeler()


# class Device():
#     def __init__(self,x,y):
#         self.q = x
#         self.r = y
#         print(x + y)
#     def opt(self):
#         print(self.q,self.r)        


# alpha_1 = Device('123','123')

# alpha_2 = Device('456','456')

# alpha_1.opt()
# alpha_2.opt()

    
# class Book():
#     def __init__(self,me,you):
#         self.me = me
#         self.you = you
#         print(me,you)
       
#     def cars(self,model,brand):
#         self.model = 'Vento'
#         self.brand = 'Volkswagen'
#         print(model,brand)
# list1 = ['Lohith','Aditya','Kolli','Adi']

# tup = (1,22)
# list1.append(tup)
# dic1 = {'Lohith':'Aditya'}        
# brand1 = Book(list1,'Windows')

# brand1.cars('XUV','Mahindra')
 

