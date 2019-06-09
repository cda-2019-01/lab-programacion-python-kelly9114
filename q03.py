##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

file = open('tablas/data.csv', 'r').readlines()

file = [row[0:-1] for row in file]


file = [row.split('\t') for row in file]
data = file

print (data)

result = {}

for x in data:
	result[x[0]] = 0

for x in data:
	result[x[0]] = result[x[0]] + int(x[1])

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))
