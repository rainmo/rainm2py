#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import count, islice

def isprime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n)-1)))

print(isprime(int(input('Please enter a number: '))))


####################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 质数（prime number）又称素数，有无限个。除了1和它本身以外不再有其他的因数。

import math
import itertools

def isprime(n):
	if n < 2:
		return False
	else:
		return all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n) - 1)))
	
print(isprime(int(input('Please enter a number: '))))
