#Recursion: Function calling itself
#Factorial

def fact(number):
    if number==0 or number==1:
        return 1
    else: 
        number=number*fact(number-1)
    return number

num=int(input("Enter a number to calculate the factorial: "))

print("the factroalof",num,"is",fact(num))