#Calculate the area of triangle using Heron's Formula
# area = sqrt(s(s-a)(s-b)(s-c)) and s=(a+b+c)/2

a= int(input("Write the first length of the triangle"))
b= int(input("Write the second length of the triangle"))
c= int(input("Write the second length of the triangle"))

s= (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)