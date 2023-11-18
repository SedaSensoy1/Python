#Write a number to display sum of digits in a given number using while loop

num = int(input("Write a number to calculate the digits: "))
hold=0
sum=0

while num > 0:
    hold=num%10  #123 ->3     #12->2
    sum +=hold   #+3          #hold 2
    num= num//10 #12  and the new num is also 12
    
print(sum)