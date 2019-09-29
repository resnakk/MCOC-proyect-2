from matplotlib.pylab import *
a = 1. # Ancho de estanque
b = 1. # Largo de estanque
Nx = 30 # Numero de intervalos en x
Ny = 30 # Numero de intervalos en y

dx = a/Nx # Disretizacion espacial en x
dy = b/Ny # En y

coords = lambda i,j: (dx*i, dy*j)
x, y = coords(1,1) # Posicion inicial
