# 汉诺塔思想笔记
# 认识汉诺塔的目标，把A柱子上的n个盘子移动到C柱子上
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前(n - 1)个盘子从A移动到B上
# 子目标2：将最底下的最后一个盘子从A移动到C上
# 子目标3：将B上的(n - 1)个盘子移动到C上
# 然后每个子目标又是一个独立的汉诺塔游戏，也就可以继续分解目标直到n为1

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

n = int(input('enter the number:'))
move(n, 'A', 'B', 'C')
