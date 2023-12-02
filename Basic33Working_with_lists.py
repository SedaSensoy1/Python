# Working with Operators on lists

# (+) Operator
# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print(L3)
###############################
# (*) Operator
# L1 = [1,2,3]
# L3 = L1 * 3
# print(L3)
#########################################
#List Methods

#APPEND() METHOD
# List1 = []

# print(List1)
# List1.append(10) #Add an element to the list
# print(List1)
    ###
# for i in range(5):
#     x = int(input("Enter an element: "))
#     List1.append(x)
# print(List1)
    ###
# x = 0
# for i in range(10):
#     x = x+10
#     List1.append(x)
# print(List1)

#CLEAR() METHOD
# list1 = [10,20,30,40,50]
# print(list1)
# list1.clear()
# print(list1)

#COUNT() METHOD
# list1 = [10,20,10,40,50]
# x = 10 
# print(list1.count(x)) #No of repetition x

#EXTEND() METHOD
# list1 = [10,20,30]
# list2 = [40,50,60]
# list1.extend(list2)
# print(list1)

#INDEX() METHOD
# list1 = [10,20,30,40]
# x = 30
# print(list1.index(x))

#INSERT() METHOD
# list1 = [10,20,30,40]
# index = 2
# x = 25
# list1.insert(index,x)
# print(list1)

#POP() METHOD
# list1 = [10,40,20,50,30,5]
# x = list1.pop()
# print(x)
# print(list1)

#REMOVE() METHOD
# list1 = [10,40,20,50,30,5]
# list1.remove(10)
# print(list1)

#REVERSE() METHOD
# list1 = [10,20,50,30,40,50]
# list1.reverse()
# print(list1)

#SORT() METHOD
# list1 = [5,2,4,3,1]
# list1.sort()
# print(list1)

# list1.sort(reverse=True)
# print(list1)

############################################
#Finding Maximum & minimum element in a List

L = [23,35,43,56,4,1,7,99]
# print(min(L))
# print(max(L))
    ###
# max_L = min_L = L[0]
# for item in L:
#     if item > max_L:
#         max_L = item
#     if item < min_L:
#         min_L = item
# print(max_L, min_L)

###########################################
#List Comprehension:
#Short way of creating a list.

#Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

#Create a list of squares for even numbers
even_squares =[x**2 for x in range(10) if x %2 == 0]
print(even_squares)