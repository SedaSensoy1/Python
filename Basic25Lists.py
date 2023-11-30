#Containers
#Lists:Store the objects in sequences.
#Integer, float, classes
#myList =[1, "a", 6.58]
#len(myList) #return the number of elements in a list.
#########################
# list1=[1,2,3] 
# list1*2 -> [1,2,3,1,2,3]
############################
# list4 =list()
# print(list4)
############################
# primes =[2,3,5,7,11,13,17] #from index 0 to n
# print(primes[4])
# print(primes[:4]) #upto 3
# print(primes[4:]) #from begining to 4
# print(primes[2:4]) #from 2 to 4
# print(primes[::-1]) #reverse a list # -1 represent the last index
# print(primes[-1:-5:-1]) #output is [17, 13, 11, 7] the last -1 is for reversing and if we reverse the order, we start to count from right to left like -1, -2,..
############################
# myList =[1, "a", 6.58]
# myList[1] ="e"
# print(myList)
# print(myList[2])
############################
# mylist =["a", "b"]
# mylist.append("c") #Adds the element to the end of the list
# print(mylist)
############################
# mylist =["a", "b"]

# mylist.extend(["d","e"]) #Adds the element to the end of the list
# print(mylist)

# mylist.insert(1,"z") #Inserts an element at a given position
# print(mylist)

# mylist.pop() #Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
# print(mylist)
# mylist.pop(0) 
# print(mylist)

# mylist.remove("b") #finds the item in list and removes it
# print(mylist)

################################################################
# fib = [1,1,"a","a",5,"a",13]

# print(fib.count("a")) #counts the number of repetition of given element

# print(fib.index(13))
################################################################
#REVERSE()

# letters =["a", "b", "c"]
# letters.reverse()
# print(letters)

################################################################
#   SORTED()

# numbers = [2, 10, 3, 26, 5]
# # print(sorted(numbers)) #This does not modifies the existing list
# # print(numbers)

# numbers.sort() #This changes the existing list
# print(numbers)
################################################################
#   REVERSE ORDER SORTING

# numbers = [2, 10, 3, 26, 5]
# print(sorted(numbers, reverse=True))
################################################################
#   MIN & MAX FUNCTION 

# numbers = [2, 10, 3, 26, 5]
# print("min:",min(numbers), " max:",max(numbers))