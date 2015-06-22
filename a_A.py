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
    
