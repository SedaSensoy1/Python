#Some built-in functions to work with Lists

list1 = [10, 30, 20, 50, 40, 20, 10, 20]

print("Original list is: ", list1)

print(list1.index(20)) #20 is second index

print("Frequency of 20 is: ", list1.count(20))

list1.append(100)
print("New list is: ", list1)

list1.remove(100)
print(list1)