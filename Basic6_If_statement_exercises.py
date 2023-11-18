# If statement

#x = int(input("x=? "))
#y = int(input("y=? "))

# if x < y:
#     print("x is less than y")

# if x > y:
#     print("x is more than y")

# if x == y:
#     print("x is equal to y")

###################################################################

# #Write a program to determine whether a person is eligible to vote

# age = int(input("Provide your age: "))

# if (age >= 18):
#     print("Eligible to vote.")
# else: 
#     print("Not eligible to work.")
    
# print("Your age is ")
# print(age)

#################################################################

# x = int(input("What's x: "))

# if (x % 2 ==0):
#     print("Even")
    
# else:
#     print("Odd")

##################################################################

# Write a python code to check the entered character is alphabet or digit

# character = input("Write a character: ")

# if (character.isalpha()):
#     print("Character is alphabet")
# if (character.isdigit()):
#     print("character is digit.")
# if (character.isspace()):
#     print("Character is space")
# else:
#     print("Character is combination of digit and alphabet")

#################################################################

#Write a program whether given character is an alphabet

# character = input("Write a character: ")

# if (character >= 'a' and character <='z' or character >='A' and character <='Z'):
#     print(character,"is an alphabet")
    
# else:
#     print(character,"is not an alphabet")
    


#################################################################

#Check whether given character is vowel.

# x=input("Write a character to check whether is wovel")
# if(x=='a' or x=='A' or x=='e' or x=='E' or x=='i' or x=='I' or x=='o' or x=='O' or x=='u' or x=='U'):
#     print("It's a vowel")
# else:
#     print("It's not a vowel")

#################################################################

#Check whether the given year is leap year or not.

#A leap year s must be multiples of 4
#If a year is multiple of 100, only those are divisible by 400 without reminder are leap years

year = int(input("Write a year to check it's a leap year or not: "))

if (year%4==0 and year!=100 or year%400==0):
    print(year,"is a leap year")
else: 
    print(year,"is not a leap year")