import math

a = float(input('Input a:'))
b = float(input('Input b:'))
c = float(input('Input c:'))

root = math.sqrt(b ** 2 - 4 * a * c)
x1 = (-b + root) / (2 * a)
x2 = (-b - root) / (2 * a)

print ('The solution are:', x1, x2)