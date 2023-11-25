#Python program to print the numbers from a given number n till 0 using recursion
#NORMAL WAY
# def numbers(n):
#     for i in range (0,n):
#         print(n)
#         n -=1
         
# n= int(input("Write a number: "))    
# numbers(n)
##################################### 
#RECURSION WAY
# def listnum(n):
#     if n > 0:
#         print(n)
#         listnum(n-1)

# x=int(input("enter any integer: "))
# listnum(x)

######################################### NEW ASSIGNMENT
#Python program to find the factorial of a number using recursion
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else: 
#         n=n*fact(n-1)
#         return n
# number=int(input("Write a number:"))
# print(fact(number))
    
####################################### NEW ASSIGNMENT

def Fib(n):
    if n<0:
        print("input cannot be negative.")
    if n==1:
        return 1
    if n==2:
        return 1
    else: 
        return Fib(n-1)+Fib(n-2)
    
N=int(input("Write a number. "))
print(Fib(N))
# print(Fib(7))
    