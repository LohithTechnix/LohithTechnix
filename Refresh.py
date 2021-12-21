# print('My name is: \nLohith Aditya')
# q = (1,2,3)
# list1 = [i for i in q if i%2==0]

# print(list1)

# i = 2
# while i is int('2'):
#     print(i)

#     i+=2
    
# class Store:
#     def __init__(self,x,y):
#         self.x = 10
#         self.y = 20
#         print(self.x + self.y)
        
        
        
#     @staticmethod
#     def terminate(q=2,z=10):
        
        
        
#         print(q+z)    
        
# book = Store(x=10,y= 5)
           
# l = book.terminate(50,60)


# def pilot(x=20,y=10,Place='Tokyo'):
    
#     q = x+y
#     if q %2!=0:
#         print(q)
        
#     else:
#         print('Not an odd number')    
        
        
        
# pilot(x=30,y=5,Place='Hyderabad')   



# def argument(*args,**kwargs):
#     print(args,kwargs)     
    
#     #args=tuples
#     #kwargs=dictionaries
    
# argument('hello','hola',English='hello',Spanish='hola')    


# def arg1(*kwargs,**args):
#     print(kwargs,args)
    
# tuple1 = (1,2,3,4,5)
# dict1 = {'Name':'Ben'}

# arg1(*tuple1,**dict1)    

# def fun1(text):
#     return text+text
# def fun2(text):
#     return text.upper()

# def fun3(func,text):
#     print(func(text))
    
# fun3(fun1,12)
# fun3(fun2,'qwerty')


# list1 = (1,2,3,4,5)



# print(len(list1))


def lis1(*s1):
    print(s1)  
    print(list(s1))      
           
    
    
list1 = [1,2,3,4,5]   


list2 = list1[0],list1[4] = list1[4],list1[0]
lis1(*list1)    
    
    
def string(s):
    
    str1 = 'Name'
    str2 = str1.split(' ')
    
    str2 = ' '.join(reversed(str1))
    print(str2)
    
    
    
string(5)        

def num1(num):
    return num+num

def num2(num):
    return num*num

def num3(func,num):
    print(func(num))
    
    
num3(num1,3)
num3(num2,4)