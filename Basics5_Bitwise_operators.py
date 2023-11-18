#Bitwise Operators(&(and), |(or), ^(xor), b<<2(Left shift), b>>2(Right Shift))
# 0 & 0 =0
# 0 & 1 =0
# 1 & 0 =0
# 1 & 1 =1

a=10
b=4
print(a&b) 
#10 in binary: 1010
#4 in binary:  0100

print(a|b)
#result will be 1110 means 14

print(a^b)
#xor operation: If the values are same 0, if different then 1
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
# So the result will be 1110 means 14

print(b<<2) #Left shift operation 
# b << 2 means b*(2^2) = 4 * 4 = 16

print(b>>2) #Right shift
# b = 4  and b>>2 means 4/(2^2) = 1

