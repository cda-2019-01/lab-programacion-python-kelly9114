##
## Imprima la suma de la segunda columna.
##


file = open('tablas/data.csv', 'r').readlines()


file = [row[0:-1] for row in file]


file = [row.split('\t') for row in file]
data = file

print file
data = []
for idx, arr in enumerate(file):
    data.append([])
    for x in arr:
        x = x.split(',')
        data[idx] += x

suma_col = 0
for e in data:
    suma_col += int(e[1])
print(suma_col)
