#Write a program to display numbers from 1 to n

n = int(input("Write a number:"))
# for numbers in range(1, n+1):
#     #print(numbers)
#     print(numbers,end=' ')
##################################################
f=1
if n>0:
    for i in range(1,n+1):
        f=f*i
    print("Factorial is: ", f)
else:
    print("negative value")
