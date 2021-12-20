# n = 5
# p = 2


# if n > p :
#     print('ok')


# else:
#     print('not ok')

# print('Lohith is {} years old'.format(9))

# 'ok' if n > p else 'not ok'


# n = range(1,10)

# for i in n:
#     print(i)

# list(n)

# print(list(n))

# print(tuple(n))


# string = 'Lohith     '

# print(string)

Lohith = 'I am Lohith'

print(Lohith.replace('h','H',2))

# print(Lohith)

# sets = {'Lohith','Shift','Short','Hello'}

# sets.add('Caps Lock')


# print(sets)


# My_List = ['google','Edge','laptop']


# My_List.insert(2,'Mozilla')

# print(My_List)


# string = '2'
# integer = 5
# string2 = 'Myname'

# print(string.isnumeric())
# n = string2.isupper()
# print(n)


# def show(**object):
#     for i in object:
#         print(i,object['arg'])




# show(arg = 'hello',kwarg = 'bye')


# import collections


# menu = collections.deque()

# print(dir(collections))

# menu.append('Non-veg')
# menu.append(':')
# menu.append('Chicken')
# menu.appendleft('Veg')

# print(menu)


# def who(**kwargs):
#     for j in kwargs:
#         print(j,kwargs['hi'])


# who(hi= 'sup what are u doing?', nothing='Ok')



# def adi(*args):
#     print('args')


# adi('Hello','Hi')    



# import collections


# enlist = collections.deque()

# enlist.append('How are you doing?')

# enlist.appendleft('Ok I am doing good')


# def my_function(*kids):
#     print('My name is {}'.format(kids[1]))



# my_function('Lohith','Aditya')    


#list pg80 g
# list2 = [2,3,4,4,4,1]

# median = len(list2) + 1

# median2 = median/ 2

# print('The median is the observation',median2)


# my_List = [1,3,5,7,9]

# my_List[3] = [0,2,4,6]

# print(my_List)


# list3 = [1,1,2,2,3,3,4,4,5,5]
# print(list3)
# list3.remove(1)
# list3.remove(2)

# list3.remove(3)
# list3.remove(4)
# list3.remove(5)


# print(list3,'all the duplicates have been removed from the list')


# yourList = [-1,-3,-5,1,3,5]

# Negative_List = list(yourList[0:3])
# Positive_List = list(yourList[3:6])

# print(Negative_List)
# print(Positive_List)


#pg80 #q5
# List_wanted = ['Adi','Lohith','Aditya','Kolli']

# bonus = List_wanted[0]
# bonus2 = List_wanted[1]
# bonus3 = List_wanted[2]
# bonus4 = List_wanted[3]

# w = bonus.upper()
# x = bonus2.upper()
# y = bonus3.upper()
# z = bonus4.upper()
 

# print(w,x,y,z)

# Hello = w,x,y,z

# me = list(Hello)

# print(me)



# tup1 = (9,10,2006)
# tup2 = (11,9,2006)

# if tup2[0] & tup2[1] & tup2[2] > tup1[0] & tup1[1] & tup1[2]:

#     no_of_days = tup2[0] - tup1[0], tup2[1] - tup1[1],tup2[2] - tup1[2]

#     print(no_of_days)


# else:

#     no_of_days_two = tup1[0] - tup2[0], tup1[1] - tup2[1],tup1[2] - tup2[2]


#     print(no_of_days_two)

#pg89 question b
# tup1 = [(14.0,'Pizza',),(10.0,'Burger'),(7.0,'Shawarma'),(8.0,'Cutlet'),(6.0,'Chicken Nuggets')]    


# descending = sorted(tup1,reverse = True)
# print(descending)



# dict1 = {'Lohith':9,
# 'Krishna':1,
# 'Mahi':8,
# 'Rajya':31}


# dict1['Lohith'] = 99

# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
# dict1.pop('Lohith')

# print(dict1)

# set1 = {'Python','Java','c','c++'}


# set1.add('Nothing')

# print(set1)
# print(list(set1))
# set1.discard('Java')
# print(set1)
# set1.remove('Python')
# print(set1)
# set1.clear()

# print(set1)

# input('Which number is ur fav?')

# answer = int(input('It is..'))

# if answer > 9:
#     print('Ok urs is pretty high.')


# elif answer == 9:
#     print('Hey, mine too.')


# else:
#     print('Ok ur wish')



# q = 2
# print(q)
# def cars(automotive):
#     for i in automotive:
#         print(i)
    
#     global q
#     q = q + 1
#     print(q)

# cars('Audi')     

# print(q)
# import random

# random_number = random.random(1,20)

# print(random_number)

# compound = 'Argon'
# print(compound)
# def element(atom):
#     print(atom)
#     global compound
#     compound = 'Hydrogen' +' '+ atom

#     print(compound)

# element('oxygen')

# print(compound)






