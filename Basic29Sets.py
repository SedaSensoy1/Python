#SETS: Containers with the same meaning they do in mathematics(Kümeler)
#No dublicates, they are removed. sets are used with brackets { }

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1.union(set2))        # Union
# print(set1.intersection(set2))  # Intersection
# print(set1.difference(set2))   # Difference

####################################################

myset = {1, 2, 3}
print(myset)

myset = set([1, 2, 3, 2]) #Dublicates are removed
print(myset)

print(set([])) #Create an empty set

###################################################

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(1 in set1)
print(1 in set2)