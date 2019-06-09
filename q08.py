##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##

file = open('tablas/data.csv', 'r').readlines()


file = [row[0:-1] for row in file]


file = [row.split('\t') for row in file]
data = file

result = {}

for x in data:
	result[x[1]] = []

for x in data:
	result[x[1]].append(x[0])

result2 = {}

for i in sorted(result.items()):
	result2[i[0]] = sorted(i[1])

for i in sorted(result2.items()):
	print i