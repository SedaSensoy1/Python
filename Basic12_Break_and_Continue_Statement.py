#Break and Continue Statement

for i in range(1,10):    # 1 2 3 4 5 6 7 8 9 
    if i==5:    # 1 3 4 but if i is 5 then break
        #break
        continue # if i=5, skip the current iteration 1 2 3 4 "no 5" 6 7 8 9 
    print(i,end=' ')