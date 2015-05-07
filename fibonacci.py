#!/usr/bin/python
# -*- coding: utf-8 -*-

def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b
