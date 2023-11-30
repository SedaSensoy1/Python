#Dictionaries: Dictionaries are containers where items are accessed by a key.

# dic2 = {} #Creating an empty dictionary
# print(dic2)
####################################################
dic1 = {"x":1, "y":2, "z":3} # key: value pairs
# print(dic1)

# print(dic1["y"])
####################################################
#Dictionary values can be changed using = operator

dic1["y"] = 10 
print(dic1)

dic1["w"] = 0 #We can add new key
print(dic1)

print(dic1.get("a")) #get returns None if the key does not exist.
print(dic1.get("a", 42)) #but get can also return a default value