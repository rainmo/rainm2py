#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 制作一个倒计时程序
import time

your_time = int(input("请输入倒计时数：")) #输入计时时长
for i in range(your_time, 0, -1):
    j = 0
    while j < i:               # 条件循环
        j = j + 1    
    print (i, '*' * i)
    time.sleep(1)
print ("BLAST OFF!")
