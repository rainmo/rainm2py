#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

def disp_1():
    print ('Via Lumia830')
def disp_2(event):
    print(event.time, event.type)
    

root = Tk()
root.title('Skype -arron@intertouch')


lab = Label(root, fg = 'white', bg = 'DarkTurquoise', width = 136, heigh = 40, text = 'Welcome to Skype!')
lab.pack()

menubar = Menu(root) # 需要指定该菜单是属于谁
menu_1 = Menu(menubar, tearoff = 0)
#for item in ["Skype", "联系人(C)", "会话", "通话", "查看", "工具"]:
#    menubar.add_command(label = item, command = disp_1)
for item in ["在线状态", "个人资料", "隐私...", "我的账户", "购买skype点数"]:
    menu_1.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "Skype", menu = menu_1) # 把menu_1变成Skype的子菜单

menu_2 = Menu(menubar, tearoff = 0)
for item in ["添加联系人", "导入联系人", "创建新组..."]:
    menu_2.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "联系人(C)", menu = menu_2)

menu_3 = Menu(menubar, tearoff = 0)
for item in ["发送", "重命名", "更改主题..."]:
    menu_3.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "会话", menu = menu_3)

menu_4 = Menu(menubar, tearoff = 0)
for item in ["通话", "视频通话", "应答"]:
    menu_4.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "通话", menu = menu_4)

menu_5 = Menu(menubar, tearoff = 0)
for item in ["联系人", "最近通话记录", "简洁边栏视图"]:
    menu_5.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "查看", menu = menu_5)

menu_6 = Menu(menubar, tearoff = 0)
for item in ["更改语言", "Skype WIFI", "选项..."]:
    menu_6.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "工具", menu = menu_6)

menu_7 = Menu(menubar, tearoff = 0)
for item in ["寻求支持", "检查更新", "关于skype..."]:
    menu_7.add_command(label = item, command = disp_1)
menubar.add_cascade(label = "帮助", menu = menu_7)
root['menu'] = menubar

# 建立右键弹出菜单
'''
for item in ["使用bing搜索", "跳转回", "复制消息", "选择全部"]:
    menubar.add_command(label = item, command = disp_1)
root['menu'] = menubar
def pop(event):
    menubar.post(event.x_root, event.y_root)
root.bind("<Button-3>", pop)
'''
def hello(event):
    print (event.x, event.y)

root.bind("<Button-1>", hello)

root.mainloop()
          







