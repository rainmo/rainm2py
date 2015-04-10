office = ['Livia', 'Merry', 'Sally', 'Kitty']
for name in office:
    print (name)

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += i
print (sum)
sum = 0
for i in range(101):
    sum += i
print (sum)

sum = 0
i = 0
for i in range(100):
    if i % 2 == 1:
        sum += i
print (sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print (sum)

sum = 0
n = 100
while n >0:
    sum += n
    n = n -2
print (sum)

birth = int(input('birth:'))
if birth < 2000:
    print ('00前')
else:
    print ('00后')
print (type(birth))

m = 0
n = 1
while n > 0:
    print (m)
    n += 1
