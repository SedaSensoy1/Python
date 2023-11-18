#Find maximum among two given numbers

def compare(x, y):
    if x>y:
        return x
    elif x==y:
        print("numbers are equal")
        return x
    else:
        return y
 
num1 =int(input("Write the first number: "))
num2 =int(input("Write the first number: "))

print ("The bigger number is ",compare(num1,num2))