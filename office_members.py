# list
office = ['Livia', 'Merry', 'Sally', 'Kitty']
print (len(office))
print (office[0])
print (office[1])
print (office[2])
print (office[3])
print (office[-1])
office.append('Arron')
print (office)
office.insert(1, 'Vivian')
print (office)
office.pop(2)
print (office)
office[2] = 'Merry'
print (office)
office.insert(1, ['Apple', 'Orange'])
print (office)
print (len(office))

# tuple
office = ('Livia', 'Merry', 'Sally', 'Kitty')
print (office[0])
print (office[1])
print (office[2])
print (office[3])
print (office[-1])
office = (1,)
print(office)
office = ('Livia', 'Merry', ['Sally', 'Kitty'])
print(office)
office[2][0] = 'Apple'
office[2][1] = 'Orange'
print(office)
