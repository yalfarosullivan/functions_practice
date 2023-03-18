def manyParams(**kwargs):
    strings = []
    numbers = []
    others = []
    for val in kwargs.values():
        if isinstance(val, str):
            strings.append(val)
        elif isinstance(val, bool):
            others.append(val)
        elif isinstance(val, int) or isinstance(val, float):
            numbers.append(val)
        else:
            others.append(val)
    return strings, numbers, others

# print(manyParams(a=1, b=True, c=3, d=False, e=None, f=None, g="a", h="z", i=9, j="x"))

def name_args(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

# name_args(name="Jeff", age=23)

all_true = lambda itr: all(itr)

# print(all_true([1, 2, True]))

def one_true(itr):
    return any(itr)

# print(one_true([0, 0, False]))

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

# print(recursive_factorial(4))

def set_deduplicate(string):
    return "".join(set(string))

# print(set_deduplicate("AABBCCDD"))

def recursive_reverse(string, i=0):
    if i == len(string) - 1:
        return string[0]
    else:
        return string[-1-i] + recursive_reverse(string, i+1)

#print(recursive_reverse("test"))
