#!/usr/bin/python
# -*- coding: utf-8 -*-

# 女子足球队选拔
gender = input('please enter your gender:')
if gender == 'm':
    print ('pass')
elif gender == 'f':
    age = int(input('please enter your age:'))
    if 10 <= age <= 12:
        print ('well down')
