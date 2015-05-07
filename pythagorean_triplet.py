#!/usr/bin/python
# -*- coding: utf-8 -*-

# 找出唯一满足a + b + c = 1000的毕达哥拉斯三元组
# a ** 2 + b **　2 = c ** 2

for c in range(1000):
    for b in range(1000):
        for a in range(1000):
            if a < b < c:
                if c == (a ** 2 + b ** 2) ** 0.5:
                    if c == 1000 - a - b:
                        print (a, b, c)
                        d = a * b * c
                        print (d)
