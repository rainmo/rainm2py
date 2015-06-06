#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import easygui

secret = random.randint(1, 100)
guess = 0
tries = 0

easygui.msgbox("""AHOY! I\'m the Dread Pirate Robers, and I have a secret!
	It is a number from 1 to 99. I\'ll give you 6 tries.""")

while guess != secret and tries < 6:
	guess = easygui.integerbox('What\'s your guess?')
	if not guess:
		break
	if guess < secret:
		easygui.msgbox(str(guess) + 'is too low, you scurvy dog!')
	elif guess > secret:
		easygui.msgbox(str(guess) + 'is too high, landlubber!')
	tries += 1

if guess == secret:
	easygui.msgbox('Bingo! You got it！ Found my secret, you did!')
else:
	easygui.msgbox('The secret number was:', secret)
