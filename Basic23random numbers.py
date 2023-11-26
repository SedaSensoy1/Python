#OTP: One time pad
# import random
# a = random.random()
# print(a) #Numbers between 0-1
# print(a*10) #Numbers between 0-10
###############################################

# import random,math
# b=math.floor(a*10)  #Numbers between 0-10
# print(b)

###############################################

import random,math
def generateOTP(): #OTP: One time pad. Generates random numbers and the number of digits.
    digits= "0123456789"
    OTP = " "
    for i in range(1,5):
        a = random.random()
        b = math.floor(a*10)
        OTP += digits[b] # b is in integer format, to make it a string wed use digits[..]
    return OTP
print("OTP of 4 digits:", generateOTP())