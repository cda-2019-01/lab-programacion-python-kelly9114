##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
file = open('tablas/data.csv', 'r').readlines()

file = [row[0:-1] for row in file]

file = [row.split('\t') for row in file]

data = []
i = 0
for x in file:
	data.append([])
	for e in x:
		a = e.split(',')
		if(len(a) == 1):
			data[i].append(a[0])
		else:
			data[i].append(a)
	i += 1

result = {}

for x in data:
	for f in x[4]:
		aux = f.split(':')
		result[aux[0]] = 0

for x in data:
	for f in x[4]:
		aux = f.split(':')
		result[aux[0]] += 1

for e in sorted(result):
    print(e + ',' + str(result[e]))