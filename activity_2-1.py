# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)

#arb_args(1, False, None, "2", {"name":"Jeff", "age":23})

# inner_func - Takes in two integers. Two nested functions should perform separate,
#  distinct math operations using the integers. The result of both nested functions 
# should then be added together and printed.

def inner_func(int_1, int_2):
    def divide():
        return int_1 / int_2
    def modulus():
        return int_1 % int_2
    print(divide() + modulus())

#inner_func(5, 17)

#lunch_lady - Takes in two strings: a student's name and their lunch preference. T
# the function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(str_1, str_2 = "Mystery Meat"):
    print(str_1, str_2)

#lunch_lady("Jeff", "Pizza")
#lunch_lady("Megan")

#sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(int_1, int_2):
    return int_1+int_2, int_1*int_2

#print(sum_n_product(1,2))

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions
#  in Python just like they can in JS. Alternatively, you can call a function from inside
#  another function.
alias_arb_args = arb_args

#alias_arb_args("test", 0)

#arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        total = 0
        for arg in args:
            total += arg
        print(total/len(args))

#arb_mean(10, 20)


#arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    longest = ""
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    return(longest)

#print(arb_longest_string("test", "really super ultra long test", "t", "really super long test"))