#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入5个名字，选择进行修改替换

name_list = []
n = 5
print ('Enter 5 name_list:')
while n > 0:
    type_name = input()
    name_list.append(type_name)
    n -= 1
print ('The name_list are:', name_list)

rep = int(input('Replace one name. Which one? (1-5):'))
if rep == 1:
    del name_list[0]
    name_list.insert(0, input('New name:'))
    print ('The name_list are:', end=' ')
    for i in name_list:
        print (i, end=' ')
elif rep == 2:
    del name_list[1]
    name_list.insert(1, input('New name:'))
    print ('The name_list are:', end=' ')
    for i in name_list:
        print (i, end=' ')
elif rep == 3:
    del name_list[2]
    name_list.insert(2, input('New name:'))
    print ('The name_list are:', end=' ')
    for i in name_list:
        print (i, end=' ')
elif rep == 4:
    del name_list[3]
    name_list.insert(3, input('New name:'))
    print ('The name_list are:', end=' ')
    for i in name_list:
        print (i, end=' ')
elif rep == 5:
    del name_list[4]
    name_list.insert(4, input('New name:'))
    print ('The name_list are:', end=' ')
    for i in name_list:
        print (i, end=' ')
