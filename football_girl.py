#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 女子足球队选拔

gender = input('please enter your gender(male/female):')
if gender == 'male':
    print ('pass')
    break
elif gender == 'female':
    age = int(input('please enter your age:'))
    if 10 <= age <= 12:
        print ('well down')
