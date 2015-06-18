#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 古代对不同年纪的称谓

def ancient_age(age):
    if age <= 1:
        print ('襁褓')
    elif 2 <= age <= 3:
        print ('孩提')
    elif age == 7:
        print ('髫年')
    elif age == 8:
        print ('童龀[chèn], 总角')
    elif age == 9:
        print ('九龄')
    elif age <= 10:
        print ('黄口')
    elif age == 12:
        print ('金钗之年')
    elif age == 13:
        print ('豆蔻年华')
    elif age >= 13:
        print ('舞勺之年')
    elif age == 15:
        print ('及笄之年')
    elif age == 16:
        print ('碧玉年华')
    elif age > 15 and age < 20:
        print ('舞象之年')
    elif age == 20:
        print ('桃李年华')
    elif age >= 21:
        print ('弱冠')

while True:
    ancient_age(age = int(input('请输入您的年龄：')))
    ask_people = input('Do you need next type?(y/n):')
    if ask_people == 'Y' or ask_people == 'y':
        continue
    elif ask_people == 'N' or ask_people == 'n':
        break
