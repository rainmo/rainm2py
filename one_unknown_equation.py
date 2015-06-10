#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	delta = b ** 2 - 4 * a * c  # delta △ 快捷键：alt+41463
	if delta > 0:
		x_1 = -b + math.sqrt(delta)
		x_2 = -b - math.sqrt(delta)
		
	elif delta == 0:
		x_1 = - (b / (2 * a))
		x_2 = x_1
		
	elif delta < 0:
		print ('No solution')

	return x_1, x_2
