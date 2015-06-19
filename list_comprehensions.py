#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# 期待输出: ['hello', 'world', 'apple']

L1 = ['Hello', 'World', 18, 'Apple', None]
[L1.remove(m) for m in L1 if not isinstance(m, str)]
L2 = L1
print([n.lower() for n in L2])
