# 1
import random


def safe_int(s):
    try:
        return int(s)
    except:
        return None

# 2

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "undefined"

# 3

def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"

# 4

def  parse_ints(values):
    list_of_integers=[]
    for i in values:
        try:
            list_of_integers.append(int(i))
        except ValueError:
            continue
    return list_of_integers

# 5

def set_age(age):
    if 150>= age >= 0:
        return age
    raise ValueError

# 6

def func(n):
    return int(n)

def retry(func, n):
    while n:
        try:
            # return func(random.choice([1,"a","k","ff","j"]))
            return func("n")
        except:
            print("no good")
            n-=1
            if n==0:
                raise

# 7

def count_errors(funcs):
    counter=0
    for func in funcs:
        try:
            func()
        except:
            counter+=1
    return counter

# 8

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as  f:
            return int(f.readline())
    except ValueError:
        raise RuntimeError("failed to loadconfig") from ValueError

