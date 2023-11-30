# Write a Python program to display the sum of n numbers using a list

numbers = [] #Create an empty list
n = int(input("Number of numbers: "))

for i in range (n):
    num = int(input("Enter the number: "))
    numbers.append(num)
print(sum(numbers))