#Example programs to illustrate Lists in

List = [1,2,3]
print(List)
print(len(List))

List = [1.34, 2.45, 7.89, 6.54]
print(List)
print(len(List))

List = ["Hello", "world", "welcome", "to", "python"]
print(List)
print(len(List))

List = [1, 1.45, "hello", 2.89, 7, "world"]
print(List)
print(len(List))
print(List[2])

List = [[1,2,3], [4,5,6], [7,8,9]] #3x3 Matrix
print(List)
#List[0][0] =1
#List[0][1] =2
#List[0][2] =3
...
#List[2][2] =9
print(List[2][1]) #Working with matrix. This line is to find 8
print(len(List))

List=[1,2,[4,5]]
print(List)
print(len(List))