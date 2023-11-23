#Nested Fuctions

# def outer_func():
#     var=10
#     def inner_func():
#         var=20
#         print("inner variable= ",var)
    
#     inner_func()
#     print("outer variable= ", var)
    
# outer_func()
##########################################
# def cube(x):
#     c = x*x*x
#     def square(x):
#         s=x*x
#         print(s)
#     square(n)    
#     print(c)
    
# n=int(input("Enter a value: "))
# cube(n)
#########################################
def cube(x):
    
    def square(x):
        s=x*x
        return s
    c=square(n)*x
    print(c)
    
n=int(input("Enter a value: "))
cube(n)



