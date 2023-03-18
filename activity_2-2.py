def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        countdown(n-1)

#countdown(5)

def natural_numbers(n, i):
    if i > n:
        return
    else:
        print(i)
        natural_numbers(n, i+1)

#natural_numbers(3, 2)

def fibbonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

#print(fibbonacci(7))

def exponent(a, b):
    if b == 1:
        return a
    else:
        return a * exponent(a, b-1)
    
#print(exponent(2, 4))

# madam = ["m", "a", "d", "a", "m"]
def palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else:
        return (str[0] == str[-1]) and palindrome(str[1:-1])

#print(palindrome("racecars"))
