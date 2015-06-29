# rainm2py
-------------------------------------
本文档主要用于Python的相关学习
-------------------------------------
+ python语法
  + 函数（function）
    + 函数参数
      + 位置参数
      + 默认参数(Default Argument Values)
      + 可变参数
      + 关键字参数(Keyword Arguments)
      + 命名关键字参数
    + 递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
      阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示: fact(n)可以表示为n x fact(n-1)

      + def fact(n):
        + if n==1:
          + return 1
      + return n * fact(n - 1) 

      + 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
+ 爬虫
  + 基本需求
    + 抓取
    + 存储
    + 分析
    + 展示
+ 框架
+ linux
+ 项目
  + Air-Music
    + 项目目标
      + 外观漂亮，具备基本功能的本地播放器
      + 可以播放本地音乐
