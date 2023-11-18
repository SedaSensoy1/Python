#Find the factorial of given number.

def factorial(num):
    n=1
    for i in range (1,num+1):
        n*=i
    return n
 
x=int(input("Write a number: "))

print(factorial(x))