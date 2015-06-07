#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 女子足球队选拔

gender = input('please enter your gender(male/female):')
if gender == 'male':
    print ('pass')
	
elif gender == 'female':
    age = int(input('please enter your age:'))   
    if 10 <= age <= 12:
        print ('Congratulations！')
    elif age < 10 or age > 12:
    	print ('Sorry, mismatch condition.')
