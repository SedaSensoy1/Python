#Keyword and Variable Length arguments in Python
# def display (str, int_x, float_y):
#     print("The string is ", str)
#     print("The integer value is ",int_x)
#     print("The floating point value is: ", float_y)
# display(float_y=5678.956, str="Hello", int_x=1234)

######################################################

#Variable-Lenght args
#Syntex:
# def functionname([arg1, arg2,...])*var_args_tuple:
#     function statements
#     return [expression]

######################################################

def fun(name,*fav_subjects): # *is a feature in the function definition and is called "arguments unpacking. This expression gathers any additional arguments passed to the function into a tuple.
    print("in", name, "likes to read")
    for subject in fav_subjects:
        print(subject)
fun("Laxman", "Python", "Maths", "Graph Theory")