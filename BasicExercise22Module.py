# Calculate the trigonometric functions of an angle.

# Prompt the user to enter an angle in degrees.

# Convert the angle to radians using the math.radians() function.

# Calculate the sine, cosine, and tangent of the angle using the math.sin(), math.cos(), and math.tan() functions respectively.

# Display the sine, cosine, and tangent of the angle.
import math 
angle= int(input("Write an angle in degrees:"))
radian= math.radians(angle)
print("radian: ",radian,"sin: ",math.sin(radian),math.cos(radian),math.tan(radian))

