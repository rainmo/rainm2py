#!/usr/bin/python
# -*- coding: utf-8 -*-

#筛法求素数
MAX = 100000
n = 10001
while n >= 0:         # 利用循环查找第10001个素数
    print(2, end=' ') # 2是最小的素数
    aList = []        # 建立一个空的列表
    for i in range(0, MAX+1):
        aList.append(0)

    for i in range(3, MAX+1, 2):
        for j in range(i+i, MAX+1, i):
            aList[j] = 1

    for i in range(3, MAX+1, 2):
        if(aList[i]==0):
            print(i, end=' ')
    n -= 1
print (i)
