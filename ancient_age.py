#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 古代对不同年纪的称谓
age = int(input('请输入您的年龄：'))
gender = input('请输入您的性别(女 / 男):')
if age <= 1:
    print ('襁褓')
elif age >= 2 and age <3:
    print ('孩提')
elif age == 7 and gender == girl:
    print ('髫年')
elif age == 8 and gender == boy:
    print ('龆年')
elif age <= 10:
    print ('黄口')
elif age == 12 and gender == girl:
    print ('金钗之年')
elif age == 13 and gender == girl:
    print ('豆蔻年华')
elif age >= 13 and age < 15:
    print ('舞勺之年')
elif age == 15 and gender == girl:
    print ('及笄之年')
elif age == 16 and gender == girl:
    print ('碧玉年华')
elif age > 15 and age < 20:
    print ('舞象之年')
elif age == 20:
    print ('桃李年华')
elif age >= 21:
    print ('弱冠')
