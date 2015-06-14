#!usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def compare(type_num):   
    secret = random.randint(1, 100)
    print('secret =', secret)
    if secret == type_num:
        print('equal')
    elif secret > type_num:
        print('too low')
    else:
        print('too high')
                  
while True:            
    type_num = int(input())
    compare(type_num)
    ask_people = input('Do you need next compare?(y/n):')
    if ask_people == 'y':
        continue
    elif ask_people == 'n':
        break
