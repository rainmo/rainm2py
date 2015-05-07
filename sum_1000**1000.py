#!/usr/bin/python
# -*- coding: utf-8 -*-

# 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

lst = []
m = 10
sum = 0
for i in range(1001):        
    j = i ** i
    lst.append(j)             # 将求幂的结果存储在列表中
lst.remove(1)                 # 未知的原因，列表里出现两次1，移除一个

while m > 0:
    k += lst.pop(0)           # 利用list.pop将列表中的每一个数字提取出来并相加
    m -= 1
    
print (sum)
