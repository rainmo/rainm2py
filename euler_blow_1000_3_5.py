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

# http://www.jb51.net/article/59663.htm
'''
问题描述：假设我有这样两个list，
          一个是list1，list1 = [1, 2, 3, 4, 5]
          一个是list2，list2 = [1, 4, 5] 
          我们如何得到一个新的list，list3，
          list3中包括所有不在list2中出现的list1中的元素。
          即：list3 = list1 – list2
          
解决方案：我们可以用set（集合）操作
          list3 = list(set(list1) – set(list2))
