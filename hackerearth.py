# myList = [[2 -i for i in range(1,2)]for i in range(1,2)]
# print(myList)

# q = input(myList)
# if q == 'no':
#     print('ok')

# else:
#     print('not ok')

def fun(func):
    return func * func


yourList = [1,2,3,4]
myList = [5,6,7,8]
for i in myList:
    if i in yourList not in myList:
        x = myList.append(i)
        print(x)
        
print(myList)
main_List = myList
print(main_List)


NotmainList = main_List
main_List.append('Hello')
print(NotmainList)
if NotmainList is main_List:
    print('This is the required output')


else:
    print('This output is  not required')


print(fun(8))    

