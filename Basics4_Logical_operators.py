#Logical Operators(and, or, not)

#AND
#T and T is T but the others are false
a=10
b=20
c=30
#print(a<b and b<c) #True
#print(a>b and b<c) #False
#print(a<b and b>c) #False
#print(a>b and b>c) #False

#OR: Only one True relation is enough to have a True result
#print(a<b or b<c) #True
#print(a>b or b<c) #True
#print(a<b or b>c) #True
#print(a>b or b>c) #False

#NOT: 
# not(T) = F 
# not(F) = T
print(not(a<b)) #False
