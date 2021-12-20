# doubts
# question 10 pcep-4
# q16 pcep 4
# q19 pcep 4
# q21,26
# {% comment %} q21 pcep 3
# q25
# q13 pcep 2
# q11 pcep 1
# q21 pcep 1
# q26 {% endcomment %}

# x=2
# print(x<<1,x<<2,x<<3,x<<4)
# def fun1(car):
#     print(car)
#     return car
# def fun2(car):
#     return car * car
# def fun3(fun,car):#formal parameter
#     print(fun(car))




# fun3(fun1,4)    #actual parameter
# fun3(fun2,6)



class Python():
    def __init__(self,a,b):
        print(a)        
    def line(self,c,d):
        self.d = d

        self.c = c
        print(c * d)
      

variable = Python(10,20)
variable.line(4,5)

class Program(Python):
    def __init__(self, a, b,e,f = 10,g = 20):
        self.e = e
        self.f = f
        self.a = a
        self.b = b
        
        print(a * b * e)
        print(f * g)
        super().__init__(a,b)

    def chrome(self):
        print('Nothing')


v1 = Program(1,2,3)
v1.line(1,2)
 