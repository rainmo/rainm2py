print ('Enter 5 names:')
a = input()
b = input()
c = input()
d = input()
e = input()
names = [a, b, c, d, e]
print ('The names are:', a, b, c, d, e)
rep = int(input('Replace one name. Which one? (1-5):'))
if rep == 1:
    del names[0]
    names.insert(0, input('New name:'))
    print ('The names are:', end=' ')
    for i in names:
        print (i, end=' ')
elif rep == 2:
    del names[1]
    names.insert(1, input('New name:'))
    print ('The names are:', end=' ')
    for i in names:
        print (i, end=' ')
elif rep == 3:
    del names[2]
    names.insert(2, input('New name:'))
    print ('The names are:', end=' ')
    for i in names:
        print (i, end=' ')
elif rep == 4:
    del names[3]
    names.insert(3, input('New name:'))
    print ('The names are:', end=' ')
    for i in names:
        print (i, end=' ')
elif rep == 5:
    del names[4]
    names.insert(4, input('New name:'))
    print ('The names are:', end=' ')
    for i in names:
        print (i, end=' ')
    
