#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************
# 下面的程序是将输入的名字的首字母转化成大写字母后输出
# ***************************

def a_2_A():
	while True:
		name = input('please enter your name:')
		new_name = name.capitalize()
		print (new_name)
		continue_type = input('Do you need continue type?(Y/N)')
		if continue_type == 'Y' or 'y':
			continue
		elif continue_type == 'N' or 'n':
			break
		
print (a_2_A())
    
