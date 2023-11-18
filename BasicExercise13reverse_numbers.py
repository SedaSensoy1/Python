#Write a Python program to display the given integer in reverse

number = int(input("Enter a positive integer: "))
new=0

while number>0:
    digit = number%10 #last digit of the number. If the number is 12, digit is 2
    new=(new*10)+ digit #I need to hold this 2 and change the position
    number= number//10
print(new)


