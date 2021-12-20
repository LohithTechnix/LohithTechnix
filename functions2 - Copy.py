#exercise pg 134 q 2
# def compute(n):
    
#     digit_calc = n +n*n +n*n*n +n*n*n*n
#     print(digit_calc)


# compute(4)
# compute(7)


#q3 contd..

# def create_array(a,b,c):
#     Array_required = a * b * c 
#     print(Array_required)

    

# create_array(2,3,5)



#q4 

# def create_list(*lis):
#     print(lis)

# lis1 = [1,2,3,4,5,6]
# lis2 = [4,5,6,7,8,9]
# lis_common = lis1[3] + lis1[3]  + lis1[3] + lis1[3] +lis1[3]
# create_list(lis1,lis2)
# create_list(lis_common)    


# def sanitize_list(*args):
#     pass

# lis1 = [1,2,3,4,5,6]
# lis2 = [4,5,6,7,8,9]

# lis1.remove(4),lis1.remove(5),lis1.remove(6),lis2.remove(4),lis2.remove(5),lis2.remove(6)

# print(lis1,lis2)

# sanitize_list(lis1,lis2)

# def print_it(i,a,s,*args):
#     print()
#     print(i,a,s,end = '')
#     for var in args:
#         print(var,end = '')


# print_it(10,3.14,)
# print_it(20,s = 'Hi',a = 6.28)
# print_it(a = 6.28,s = 'Hello',i = 30)
# print_it(40,2.35,'Nag','Mum',10)

# def fun(a,*args,s = '!'):
#     print(a,s)

#     for i in args:
#         print(i,s)

# fun(10)
# fun(10,20)
# fun(10,20,30)
# fun(10,20,30,40,s = '+')        


def chrome(browse):
    print(browse)



tup =  (1,3,4,5,6,6,9)
lis = [1,3,5,6,8,9]



chrome(*tup)
