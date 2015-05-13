#!/usr/bin/python
# -*- coding: utf-8 -*-

# %s占位的使用

first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
welcome = 'Hi there, %s %s!'
print (welcome % (first_name, last_name))
