# def compute(n):
#     n = 0
#     n+=n
#     var = 0
#     for i in range(n):

#         n = int(str(n) + str(n))
#         q = int(str(n)+ str(n))

#         var+= n


#     print(var)    




# compute(4)
# compute(7)



    



def count_lower_upper():
    n = int(input('Please enter the value of n'))
    print(n)


    for i in n:
        if i in n.isupper():
            print(i)
            q = len(i)
            print(q)

        if i in n.islower():
            print(i)
            p = len(i)
            print(p)
  

        else:
            print('Nothing')



