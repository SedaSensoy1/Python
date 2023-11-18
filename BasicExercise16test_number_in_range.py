#Test a number in a range

def test_range(num):
    if num in range(3,7):
        print("%s is in the range" %str(num))
    else:
        print("number is not in the range.")
test_range(5) 