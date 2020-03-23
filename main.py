a = ['casa','famiglia','telefono','computer']
b = []
for e in a:
	for i in e:
		if i == 'e':
			b.append(e)
			break
print(b)
d = 1
c = int(input('inserisci un numero --> '))
for e in range(c):
	print('ciao',d) 
	d += 1