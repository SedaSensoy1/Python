#Accessing Elements & Searching element in a List
L =[23,35,43,56,4,1,7,99]

# for item in L:
#     print(item,end=' ')

#####################################################

# n= len(L)
# for i in range(n):
#     print(L[i], end='\t') # \t => space as tap
    
#####################################################

#key =int(input("Enter number to be searched: "))
#for item in L: 
#    if item==key:
#        print("Element is found")
#        break
    
#####################################################

# key =int(input("Enter number to be searched: "))
# found = False
# for item in L: 
#     if item==key:
#         found = True
#         break
# if (found == True):
#     print("Element is found")
# else: 
#     print("Element is not found")
    
#####################################################

total = 0
for item in L:
    total = total + item
print("Total is: ", total)
print("Total is: ", sum(L))
    
    