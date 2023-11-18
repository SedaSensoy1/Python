a = 100
#print ("value of a =", a)

b = 200
a = b # b will be equal to a
#print(a)

a = 3 
b = 5
c = a * b  #or c = a + b
#print(c)

a = 2
b = 5
c = a ** b # ** means ^ power operation
#print(c)

a = 10
b = 3
c = a / b
c = a // b #The // in this code represents the floor division operator in Python. It divides the left operand by the right operand and returns the largest integer that is less than or equal to the result. So, in this case, it's dividing 100 by 200, which results in 0.5, but the // operator gives you the largest integer (0 in this case).
#print(c)

# E=mc^2
m = 3
c = 4 
E = m * c ** 2
#print("result is : ", E)

#print("ben")
    #print("sen") # That will cause an error due to indentation

#a = int(input("Enter first number: ")) #If I dont write int, the type will be a string
#b = int(input("Enter second number"))
avg = (a+b)/2
#print("Average of two given numbers is : ", avg)

radius = float(input("Enter radius: "))
area = 3.1412 * radius ** 2
circumference = 2 * 3.1412 * radius
print("Area of circle = ", area)
print ("Circumference of the circle = ", circumference)