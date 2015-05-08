#!/usr/bin/python
# -*- coding: utf-8 -*-

sum_1 = 0
sum_2 = 0
for i in range(1, 1000):
    if i % 3 == 0 and i % 5 != 0:    	
        sum_1 += i

for j in range(1, 1000):
    if j % 5 == 0:        
        sum_2 += j

sum = sum_1 + sum_2
print (sum)
