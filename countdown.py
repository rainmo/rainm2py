import time
your_time = int(input("请输入倒计时数："))
for i in range(your_time,0,-1):
    j = 0
    while j < i:        
        j = j + 1    
    print (i, '*' * i)
    time.sleep(1)
print ("BLAST OFF!")
