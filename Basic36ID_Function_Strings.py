# id() Memory address of that object

# a = 10
# print(a)
# print("Address of a : ",id(a))

# #b = 10
# b = 11
# print(b)
# print("Address of b : ",id(b))

# ida = id(a)
# idb = id(b)

# if(ida == idb):
#     print("Both adresses are the same")
# else:
#     print("Different adresses")

##############################################

# str1 = "Hello"
# print("str1: ",str1)
# print("Address of str1: ",id(str1))
# id1 = id(str1)

# str2 = "world"
# print("str2: ",str2)
# print("Address of str2: ",id(str2))
# id2 = id(str2)

# if(id1 == id2):
#     print("Same addresses")
# else: 
#     print("Different addresses")    

#############################################

str1 = "hello"
print("str1: ",str1)
print("Address of str1: ",id(str1))
id1 = id(str1)


# str3 ="ich"
# str2 = str1
# str2 += str3

str3 = "HELLO"
str2 = str3.lower()

print("str2: ",str2)
print("Address of str2: ",id(str2))
id2 = id(str2)

if(id1 == id2):
    print("Same addresses")
else: 
    print("Different addresses")    
