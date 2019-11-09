from matplotlib.pylab import *
archivo = open("results.txt", "r")
datos = []
lista = []
for i in archivo:
    a = i.split(" ")
    if a[0] == str(0):
        lista.append([[], []])
    else:
        break

cont = 0
for i in archivo:
    a = i.split(" ")
    a[2] = a[2][0:-1]
    tiempo = float(a[0])
    x = float(a[1])
    y = float(a[2])
    lista[cont][0].append(x)
    lista[cont][1].append(y)
    cont += 1
    if cont == len(lista):
        cont = 0

print(lista[0])
xlabel("X")
ylabel("Y")
title("particle trajectory")

for i in lista:
    plot(i[0], i[1])
show()