from functools import reduce

# function 1
def simple_separator():
    s = "**********"
    return s

# function 2
def long_separator(count):
    s = "*" * count
    return s

# function 3
def separator(simbol, count):
    s = simbol*count
    return s

# function 4
def hello_world():
    s = "*"*10 + "\n\nHello World!\n\n" + "#"*10
    return s

# function 5
def hello_who(who='World'):
    s = "{0}\n\nHello {1}!\n\n{2}".format("*"*10, who, "#"*10)
    return s

# function 6
def pow_many(power, *args):
    res = reduce(lambda x,y: x + y, args)**power
    return res

# function 7
def print_key_val(**kwargs):
    s = ""
    for k,v in kwargs.items():
        s += str(k) + " --> " + str(v) + "\n"
    return s

# function 8
def my_filter(iterable, function):
    out = list(filter(function, iterable))
    return out

