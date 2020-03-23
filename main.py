a = ['casa','famiglia','telefono','computer']
b = []
for e in a:
	for i in e:
		if i == 'e':
			b.append(e)
			break
print(b)