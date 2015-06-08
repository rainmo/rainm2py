#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import easygui

F = easygui.integerbox('please enter Fahrenheit:')
C = round(5 / 9 * (F - 32), 2)  # round(2.456, 2) gives 2.46 
easygui.msgbox(C, "℃")

