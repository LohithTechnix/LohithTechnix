def num(num1):
    want_to1 = int(input('Enter the first number u want to'))
    want_to2 = int(input('Enter the second number u want to'))
    result = (input('Want symbol do u want to enter:'))
    
    if result == '+':
        print(want_to1+ want_to2)
        print(num1 + num1)


    elif result == '-':
        print(num1-num1)
        if want_to1 > want_to2:
            print(want_to1-want_to2)

        else:
            print(want_to2-want_to1)


    elif result == '*':
        print(want_to1 * want_to2)       
        print(num1*num1)


    else:
        print(num1/num1)
        if want_to1 > want_to2:
            print(want_to1/want_to2)

        else:
            print(want_to2/want_to1)
                
num(4)
num(14)