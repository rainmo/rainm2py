#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import count, islice

def isprime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n)-1)))

print (isprime(int(input('Please enter a number: '))))
