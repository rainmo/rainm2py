#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 随机生成一个秘密数字，进行猜数小游戏

import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print('AHOY! I\'m the Dread Pirate Robers, and I have a secret!')
print('It is a number from 1 to 99. I\'ll give you 6 tries.')

while guess != secret and tries <6:
	guess = int(input('What\'s your guess?'))
	if guess < secret:
		print ('Too low, you scurvy dog!')
	elif guess > secret:
		print ('Too high, landlubber!')
	tries += 1

if guess == secret:
	print('Bingo! You got it！ Found my secret, you did!')
	print('The secret number was:', secret)
