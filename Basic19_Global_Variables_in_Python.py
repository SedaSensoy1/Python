# x= "awesome"

# def myfunc():
#     print("Python is "+ x)
    
# myfunc()


##############But defining variable in global scope#############


def myfunc():
    global x
    x= "awesome"
    
myfunc()
print("Python is "+ x)
    