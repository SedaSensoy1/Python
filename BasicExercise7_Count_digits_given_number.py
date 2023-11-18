#Write a program to display count of digits in a given number

n=int(input("Enter any number: "))
counter = 0

while n>0:
    n=n//10
    counter+= 1
print(counter)