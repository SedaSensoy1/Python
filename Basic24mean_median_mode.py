from statistics import mean, median, mode
list1 =[15,20,23,7,45,63,46,37,237]
print("Mean is: ", mean(list1))
print("Median is: ", median(list1)) #The middle number
print("Mode is : ", mode(list1)) # The mode is the value that appears most frequently in the list. If no value repeats, or if multiple values have the same highest frequency, the mode function raises a StatisticsError.