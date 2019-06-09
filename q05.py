##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

file = open('tablas/data.csv', 'r').readlines()


file = [row[0:-1] for row in file]


file = [row.split('\t') for row in file]
data = file

result = {}

for x in data:
	result[x[0]] = []

for x in data:
	result[x[0]].append(int(x[1]))

for key in sorted(result.keys()):  
     print(key + ',' + str(max(result[key])) + ',' + str(min(result[key])))