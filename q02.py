##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##


file = open('tablas/data.csv', 'r').readlines()


file = [row[0:-1] for row in file]

file = [row.split('\t') for row in file]
data = file


result = {}

for x in data:
	result[x[0]] = 0

for x in data:
	result[x[0]] = result[x[0]] + 1

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))

