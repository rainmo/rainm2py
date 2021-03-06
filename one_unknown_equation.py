#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一元二次方程

import math

def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c  # delta △ 快捷键：alt+41463
    if delta > 0:
        x_1 = -b + math.sqrt(delta)
        x_2 = -b - math.sqrt(delta)
        return x_1, x_2
    elif delta == 0:
        x_1 = -(b / (2 * a))
        x_2 = x_1
        return x_1, x_2
    elif delta < 0:
        print ('No solution')
        
###################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
	if delta == 0:
		return -b
	if delta < 0:
		return None
	else:
		return -b + math.sqrt(delta), -b - math.sqrt(delta)
		
a = int(input('please enter a: '))
b = int(input('please enter b: '))
c = int(input('please enter c: '))
delta = b * b - 4 * a * c
print(quadratic(a, b, c))
