from typing import List

tupla = (13, 1, 8, 3, 2, 5, 8)

tuplalist: list[int] = list(tupla)

for t in tuplalist:
    n = 0
    if t >= 5:
        tuplalist.pop(n)
        n+= 1
else:
    print(tuplalist)

#other solution
#Dada la siguiente tupla,
# crear una lista que sólo incluya los números menor que 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)