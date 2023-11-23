#Lambda func as an argument to a function
# twice =lambda x: x*2
# thrice =lambda x: x*3

# print(twice(4))
# print(thrice(3))
#######################################
# def func(f,n):
#     print(f(n))
# twice =lambda x: x*2
# thrice =lambda x: x*3

# func(twice,4)
# func(thrice,3)
#######################################
#Program that uses a lambda func to find sum of list 10 natural numbers
number =lambda x: (x*(x+1))/2
print(number(10))
############   OR   #############
number =lambda : sum(range(1,11))
print(number())
######################################
#Fimnd the smallest of the two given number
def small(a,b):
    if(a>b):
        return b
    else:
        return a
sum =lambda x,y : x+y
diff =lambda x,y : x-y
print("Smaller of two numbers: ", small(sum(-3,-9),diff(-1,2)))