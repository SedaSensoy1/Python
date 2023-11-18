#Write a Python program to generate the prime numbers from 1 to N

num=int(input("write a number to generate prime numbers up to given number: "))
#if number is 5

for n in range(2,num+1): #n is in range from 2 to 5
  for i in range (2,n): #I need to print from 2 to n
    if n%i==0:
     break
    
    else:
     print(n)
     break
  