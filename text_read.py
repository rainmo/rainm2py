#!/usr/bin/python
# -*- coding: utf-8 -*-

test_file = open('C:\\Users\Arron\\rainm2py\\Zen_of_Python.txt')
text_1 = test_file.read()
print (text_1)

test_file_c = open('C:\\Users\Arron\\rainm2py\\Zen_of_Python_C.txt', 'w')
test_file_c.write(text_1)
#test_file_c.close()

text_2 = test_file_c.read()
print (text_2)