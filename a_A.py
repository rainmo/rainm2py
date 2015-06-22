#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************
# 下面的程序是将输入的名字的首字母转化成大写字母后输出
# ***************************

def a_2_A(name):		
	new_name = name.capitalize()
	return new_name

while True:
	print(a_2_A(input('please enter your name:')))
	continue_type = input('Do you need continue type?(Y/N):')
	if continue_type =='Y' or continue_type =='y':
		continue
	elif continue_type =='N' or continue_type =='n':
		break

# ***************************
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):		
	new_name = name.capitalize()
	return new_name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
