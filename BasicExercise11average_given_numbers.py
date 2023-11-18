#Assignment: Write a Python program to find out the average of a set of integers
num_elements=int(input("How many numbers do you have to calculate the average:" ))

counter=1
sum=0

while counter < num_elements+1:
    num = int(input("Write the number: "))
    counter +=1
    sum = sum+num
    avg= sum/num_elements
    
print(avg)