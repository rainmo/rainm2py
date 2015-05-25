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
                        
# ++++++++++++++++++++++++++++++++++++++++++++++++

#!/usr/bin/python

c=0
while True:
	for b in range(0,c):
		for a in range(0,b):
			if a**2 + b**2 == c**2:
				if a+b+c == 1000:
					print （"a = %d, b = %d, c = %d a * b * c = %d" % (a, b, c,a * b * c)）
	c+=1
