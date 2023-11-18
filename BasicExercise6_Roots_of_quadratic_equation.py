#Write a Python program to find the roots of a quadratic equation

# equation: a*(x**2) + b*x + c = 0


a= int(input("Write a to find the roots of quadratic equation: "))
b= int(input("Write b to find the roots of quadratic equation: "))
c= int(input("Write c to find the roots of quadratic equation: "))

discriminant =((b**2)-(4*a*c))

if (a != 0):
    
    
    if discriminant == 0:
        print("The roots are equal")
        x= -b/(2*a)
        print("The roots are" , r)
        
    elif discriminant > 0:
        x = (-b + 0.5*((b**2-4*a*c))/(2*a))
        y = (-b - 0.5*((b**2-4*a*c))/(2*a))
        print("roots are ", x, "and", y)
        
    else:
        print("no real root, imaginary")
        x =-b/(2*a)
        imaginary= (0.5*(-discriminant))/(2*a)
        print("roots are ", x, "+", imaginary,"i", " and ", x, "-", imaginary,"i")
else: 
    print("It is not a quadratic equation.")
