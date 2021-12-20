# def cal_sum(x,y,z):
#     print(x + y + z)
#     return x + y + z
#     pass

# s1 = cal_sum(10,20,30)

# a,b,c = 1,2,3

# s2 = cal_sum(a,b,c)

# s3 = 3**2

# cal_sum(s1,s2,s3)


#positional keyword arguments
# q = 1
# def fun(i,j,k):
#     print(i + j)
#     global q
#     q = print(k.upper()
#     )


# fun(10,3.14,'Variable')    
# fun(20,30,'Nothing')



# def print_it(i,j,*args,x,y,**kwargs):
    
    #print(i,j, end = '')

    # for var in args:
    #     print(var)
    #     print(x,y)
    #     for name,value in kwargs.items():
    #         print(name,value,end = '')



# print_it(10,20,x = 3,y = 40)

# print_it(20,30,100,200,x = 30, y = 40)



# def python(*car):
#     print(car)


# python('Lohith','Aditya',"Kolli")


# def delete_it(a,b,c,d,e):
#     print(a,b,c,d,e)



# lst = [10,20,30,40,50]
# tpl = ('A','B','C','D','E')

# delete_it(*lst)

# delete_it(*tpl)


# def remain(**kwargs):
   
#     print(kwargs)


# dic = {'name':'Anil','marks':50}
# remain(**dic)



# def retain(name = 'Sanjay',marks = str(75)):
#     print(name,marks)


# dict_objects = {'name' : 'Lohith','marks':79}


# retain(**dict_objects)



# def ispangram(s):
    
#     alphaset = set('qwertyuiopasdfghjklzxcvbnm')
#     print(alphaset)
#     print(s)
    
#     return alphaset <= set(s.lower())

# print(ispangram('Mika Hakkinen'))

# print(ispangram('Kimi Raikonnen'))




# def convert(s1):
#     items = [s for s in s1.split('-')]
#     items.sort()
#     s2 = '-'.join(items)
#     return s2
# s = 'Here comes the dots followed by hyphens'
# t = convert(s)
# print(t)


# def generate_list():
#     lst = list()
#     print(lst)
#     for i in range(1,11):
#         lst.append((i,i**2,i**3))


#     return lst

# l = generate_list()
# print(l)    



# tup = (1,3,4)

# lis1 = list(tup)

# print(lis1)


  
# def count_lower_upper(*args):
#     len(args)
    
# count_lower_upper('Hello, My Name Is Lohith Aditya Kolli')





# def head():
    

#     lis = list()

#     for i in range(1,10):
#         print(i)
#         lis.append(i)
#     return lis

# answer = head()
# print(answer) 
    



