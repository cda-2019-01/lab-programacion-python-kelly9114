##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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
		result[aux[0]] = []

for x in data:
	for f in x[4]:
		aux = f.split(':')
		result[aux[0]].append(int(aux[1]))

print (result)

for key in sorted(result.keys()):  
     print(key + ',' + str(min(result[key])) + ',' + str(max(result[key])))