#1
def f(x):
    return x * x
print (list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#2
from functools import reduce

def add(x, y):
    return x + y

print (reduce(add, [2, 4, 6, 8, 10]))
#3
import functools

def add(x, y):
    return x * y

print (functools.reduce(add, [1, 3, 5]))
