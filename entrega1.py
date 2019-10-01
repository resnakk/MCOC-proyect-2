from matplotlib.pylab import *
a = 1. # Ancho de estanque
b = 1. # Largo de estanque
Nx = 30 # Numero de intervalos en x
Ny = 30 # Numero de intervalos en y
s = 3600 #Tiempo a evaluar, s
Nt = 3600 #Numero de intervalos de tiempo

dx = a/Nx # Disretizacion espacial en x
dy = b/Ny # En y
dt = s/Nt #en t

#Parametros
coords = lambda i,j,t : (dx*i, dy*j, dt*t)
x, y, t = coords(1,1,0) # Posicion inicial rn instante t0
g = 9.8 #m/s2
k = 0.41
#velocidad como perfil logaritmico
def ux(y0):
	return log(30*y0)/k
u0x = ux(y)
for i in range(Nt)
	#Posicion en x
	x1 = v0x*t
	#Posicion en y
	y1 = v0y+(g*t**2)*0.5

#Ecuacion de movimiento
def F(x,v,t):
	rho = 1000 #densidad del agua
	Vrel = Vf - Vp  #fluido, particula
	fd = 0.5*rho*Cd*norm(Vrel)*(Vrel)

#Integracion
ai = Fi/m
xi_1 = xi + vi*dt + ai*dt**2/2