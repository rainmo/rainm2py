#!/usr/bin/python
# -*- coding: utf-8 -*-

# 制作一个具有基本功能的音乐播放器

from tkinter import *
import pygame
import sys
import easygui
import ctypes
import struct


pygame.init ()
pygame.mixer.init ()



#song_lst = ['Indian Summer', 'One Day in Spring', 'Orinoco Dreams',
#'Starry Sky', 'The_Rain', 'Woodland Night']
easygui.msgbox('唯爱与音乐不可辜负')
#fav_song = easygui.buttonbox("选择需要播放的曲目", choices = song_lst)
#easygui.msgbox('你选择的曲目' + fav_song)
def song_1():	
	pygame.mixer.music.load('Indian Summer.mp3')
	pygame.mixer.music.play()

def song_2():	
	pygame.mixer.music.load('The_Rain.mp3')
	pygame.mixer.music.play()

def song_3():
	pygame.mixer.music.load('One Day in Spring.mp3')
	pygame.mixer.music.play()

def song_4():
	pygame.mixer.music.load('Orinoco Dreams.mp3')
	pygame.mixer.music.play()
def song_5():	
	pygame.mixer.music.load('Starry Sky.mp3')
	pygame.mixer.music.play()
def song_6():
	pygame.mixer.music.load('Woodland Night.mp3')
	pygame.mixer.music.play()

root = Tk()
root.title('Music for Arron')


def disp_1():
    print ('Via Lumia830')
def disp_2(event):
    print(event.time, event.type)

butt_1 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = '播放目录')
butt_2 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'Indian Summer', command = song_1)
butt_3 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'The_Rain', command = song_2)
butt_4 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'One Day in Spring', command = song_3)
butt_5 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'Orinoco Dreams', command = song_4)
butt_6 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'Starry Sky', command = song_5)
butt_7 = Button(root, fg = 'white', bg = 'DarkTurquoise', width = 50, heigh = 2, text = 'Woodland Night', command = song_6)

butt_1.pack()
butt_2.pack()
butt_3.pack()
butt_4.pack()
butt_5.pack()
butt_6.pack()
butt_7.pack()

#调节音量
def vol_1():
	pygame.mixer.music.set_volume(0.3)
butt_8 = Button(root, fg = 'white', bg = 'Brown', width = 50, heigh = 2, text = '音量（30%）', command = vol_1)
butt_8.pack()

def vol_2():
	pygame.mixer.music.set_volume(0.7)
butt_9 = Button(root, fg = 'white', bg = 'Brown', width = 50, heigh = 2, text = '音量（70%）', command = vol_2)
butt_9.pack()

def vol_3():
	pygame.mixer.music.set_volume(1.0)
butt_10 = Button(root, fg = 'white', bg = 'Brown', width = 50, heigh = 2, text = '音量（100%）', command = vol_3)
butt_10.pack()

butt_8.pack()
butt_9.pack()
butt_10.pack()


menubar = Menu(root) # 需要指定该菜单是属于谁
menu_1 = Menu(menubar, tearoff = 0)
for item in ["音乐列表", "添加本地音乐", "云音乐"]:
    menu_1.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "文件", menu = menu_1) # 把menu_1变成Skype的子菜单

menu_2 = Menu(menubar, tearoff = 0)
for item in ["最近播放记录", "简洁边栏视图"]:
    menu_2.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "查看", menu = menu_2)

menu_3 = Menu(menubar, tearoff = 0)
for item in ["更改语言", "Music WIFI", "选项..."]:
    menu_3.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "工具", menu = menu_3)

menu_4 = Menu(menubar, tearoff = 0)
for item in ["寻求支持", "检查更新", "关于..."]:
    menu_4.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "帮助", menu = menu_4)
root['menu'] = menubar
'''
# 建立右键弹出菜单

for item in ["使用bing搜索", "跳转回", "复制消息", "选择全部"]:
    menubar.add_command(label = item, command = disp_1)
root['menu'] = menubar
def pop(event):
    menubar.post(event.x_root, event.y_root)
root.bind("<Button-3>", pop)

# 记录鼠标左键点击的坐标
def hello(event):
    print (event.x, event.y)

root.bind("<Button-1>", hello)
'''


root.mainloop()
