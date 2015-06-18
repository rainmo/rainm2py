#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 古代对不同年纪的称谓


def ancient_age(age):
    if age <= 1:
        print ('''襁褓
注释：指初知发笑尚在襁褓中的幼儿，未满周岁的婴儿
            '''
            )
    elif 2 <= age <= 3:
        print ('''孩提
注释：韩愈诗中就有“两家各生子，提孩巧相如”
            '''
            )
    elif age == 7:
        print ('''髫年
注释：幼童时期。古儿童尚未束发时自然下垂的短发，故称之，也称作“垂发”
            '''
            )
    elif age == 8:
        print ('''童龀[chèn], 总角
注释：古代儿童将头发分作左右两半，在头顶各扎成一个结，
      形如两个羊角，故称“总角”，《说文》中有“男八月生齿、八岁而龀；
      女七月生齿、七岁而龀”的说法。可以看出，孩子乳牙脱落，长出恒牙，称为“龀”
            '''
            )
    elif age == 9:
        print ('''九龄
注释：教数之年指儿童9岁。语出《礼记》
            '''
            )
    elif age <= 10:
        print ('''黄口
注释：10岁以下的少儿通称，即稚气未脱的男孩或女孩代称也
            '''
            )
    elif age == 12:
        print ('''金钗之年(女)
注释：女孩子到了12岁就可以头带金钗
            '''
            )
    elif age == 13:
        print ('''豆蔻年华（女）
注释：多年生草本植物，产岭南，其花很美，
      尚未大开的花形如怀孕之身，南方人称为含胎花。
      诗文中常用以喻指少女，语出唐·杜牧《赠别》诗：
      “娉娉袅袅十三余，豆蔻梢头二月初。”
            '''
            )
    elif age >= 13:
        print ('舞勺之年')
    elif age == 15:
        print ('及笄之年')
    elif age == 16:
        print ('碧玉年华')
    elif age > 15 and age < 20:
        print ('舞象之年')
    elif age == 20:
        print ('桃李年华')
    elif age >= 21:
        print ('弱冠')

while True:
    ancient_age(age = int(input('请输入您的年龄：')))
    ask_people = input('Do you need next type?(y/n):')
    if ask_people == 'Y' or ask_people == 'y':
        continue
    elif ask_people == 'N' or ask_people == 'n':
        break
