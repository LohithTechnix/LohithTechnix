#create a function:
def myfunction():
    global z, f 
    z = "hu"
    f = "gl"
    x = "hello"
    return x,f,z
       
#execute the function:
y = myfunction()

#x should now be global, and accessible in the global scope.
print(y)
print(z + " "+f)
    