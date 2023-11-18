#Check whether the given integer is a multiple of both 5 and 7.

num =int(input("Write a number: "))

# if num%7==0:
#     if num%5==0:
#         print("Number is multiple of 5 and 7.")
#     else:
#         print("Number is not multiple of both 5 and 7.")
# else:
#     print("Number is not multiple of 5 and 7.")

##############################  OR  ##############################

if num%7==0 and num%5==0:
    print(num, "is multiple of 5 and 7.")
else:
    print(num, "is not multiple of 5 and 7.")