##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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
	for key in x[3]:
		if key in result:
			result[key] += int(x[1])
		else:
			result[key] = int(x[1])

print result

for key in sorted(result.keys()):
     print(key + ',' + str(result[key]))