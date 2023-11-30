#Write a Python program to find the odd numbers in a List

numbers = [8,3,1,6,2,4,5,9]
odd = [] #Create an empty list

for i in range (len(numbers)):
    if numbers[i] % 2 != 0:
        odd.append(numbers[i])
        
print(odd)
        
