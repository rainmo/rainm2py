import easygui

name = easygui.enterbox('Please enter your name')
locat = easygui.enterbox('Please enter your location',
	default = 'ShenZhen road')
post = easygui.enterbox('Please enter your zip code',
	default = '518000')
easygui.msgbox(name + "\n" + locat + "\n" + post)
