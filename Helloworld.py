top = 100
least = 1

print("Select a numbers between {} and {}".format(top,least))


v = int(input())


while v != 50:
    int(input("Please choose another number"))
    if v > 50:
        print("Please choose a lower number")
        continue
    elif v < 50:
        print("Choose a higher number please")
        continue
    else:
        print("You chose the right number")    
        










