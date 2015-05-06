# this is a office info
arron = ['Arron Liu', 22, 'IT']
helen = ['Helen Chen', 21, 'PBX']
office = [arron, helen]
for person in office:
	print (person[0].split()[-1])

NAMES = [person[0] for person in office]
AGES = [person[1] for person in office]
POSITIONS = [person[2] for person in office]

office.append(['Cathy Lee', 20, 'PBX'])
NAMES, AGES, POSITIONS = range(3)
