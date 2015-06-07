#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %s占位的使用

first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
welcome = 'Hi there, %s %s!'
print (welcome % (first_name, last_name))

# 小明的成绩从去年的72分提升到了今年的85分
# 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位

s1 = 72
s2 = 85
r = (s2 - s1) / s2 * 100
print('%.1f %%' % r)

'''
常见的占位符有：

%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
