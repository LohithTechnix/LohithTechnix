# def chrome(*lst):
#     print(lst)


# lis = (1,2,3,4,5)
# lis2 = (6,7,8,9)


# chrome(*lis2)


# def sanitize_list(*args):
#     pass

# lis1 = [1,2,3,4,5,6]
# lis2 = [4,5,6,7,8,9]

# lis1.remove(4),lis1.remove(5),lis1.remove(6),lis2.remove(4),lis2.remove(5),lis2.remove(6)




# print(lis1,lis2)

# sanitize_list(lis1,lis2)


# def num(time,place,animal):

#     print(time,place +''+ animal)

# list_wanted = [9,'Hyd','Hippo']
# num(*list_wanted)    


# def alpha(name = 'Lohith',age = 14):
#     print(name,age)
# dic1 = {'name' : 'Alphatauri','age' : '1'}
# alpha(*dic1)
# alpha(**dic1)


# my_List = [8,2,5,7,9]


# final_List = sum(my_List)

# print(final_List)

#define  function compute()
#it calculates value of n + nn +nnn +nnnn
#n is the digit
#We have to test for 4 and 7

#take digit calling a func
#n 
#nn
# nnn
# nnnn
#4 4+40 4+40+400 4+40+400+4000

# def compute(n):
#     #print(n)
#     digit=n
#     final_ans = 0
#     for i in range(n):
#         final_ans+=n # FA =0 + 0; FA = 0 + 1; FA = 1 + 2; FA = 3 + 4
#         print(final_ans)
        
        
#     print(int(str(4)+str(8)))
        
#     print(final_ans)

# compute(4)
# compute(7)    


def compute1(n):
    print(n)
    res=0
    digit=n
    for i in range(1,n+1):
        res+=n
        n+=digit*(10**i)
    print(n)
    print(res)


compute1(4)    


# def create_array(*n):
#     for i in n:
#         print(i)

# array = [1,2,3]


# create_array(array[0:2])


# def create_list(*lis):
#     pass

# lis1 = [1,2,3]

# lis2 = [2,3,5]
# lis3 = list()

# for i in lis1:
#     if i in lis2:
#         lis3.append(i)
# print(lis3)
# create_list(lis3)



# def sanitize_list(*lis):
#     print(lis)
    
# my_List = [1,2,2,3,3,4,5,5,6,7,7]
 
# your_List = set(my_List)
# print(your_List)    
# All_list = list(your_List)
    



        
# sanitize_list(All_list)


# def fun(a,*args,s = '!'):

#     print(a,s
    
#     )

#     for i in args:
#         print(i,s)


# fun(10)
# fun(10,20)
# fun(10,20,30)
# fun(10,20,30,40,s= '+')


