#create a function:
z = 2
f = 9
def myfunction():
    global z, f 
    z = "hu"
    f = "gl"
    x = "hello"
    
       
#execute the function:
print(f,z)
#x should now be global, and accessible in the global scope.
print(z +f)
    