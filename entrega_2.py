from matplotlib.pylab import *
import random 
#unidades SI
_m = 1.
_mm = _m*1e-3
_gr = 1e-3
_s = 1.
_kg = 1.
#Datos
d = 2*_mm
g = 9.81*_m/_s**2
rho = 2700*_kg/(_m**3)
rho_w = 1000*_kg/(_m**3)
m = rho*pi*(d**3)*(4./3./8.)
m_w = rho_w*pi*(d**3)*(4./3./8.)
Cd = 0.47 #particula redonda
#Euler en en x0
dt = 1e-6*_s  #paso de tiempo
tmax = 1 #tiempo maximo de simulacion
ti = 0. #tiempo actual 
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
k = 0.41
def vx(y0,yi):
	return -log(30*y0)/k
#Condiciones Iniciales
n_particulas = 5 #Numero de particulas
vf = array([5*_m*_s,0])
#historial de las particulas
x_particulas = []
v_particulas = [] 
x_p = []
y_p = []
for i in range(n_particulas): 
	x_p.append([])
	y_p.append([])
	v_x = 0
	v_y = 0
	p_x = (d)*random.random() + d
	p_y = (d)*random.random() + d
	xi = array([p_x,p_y])
	vi = array([v_x,v_y])
	x_particulas.append(xi)
	v_particulas.append(vi)
#Iteracion en el tiempo	
xim1 = []
vim1 = []
while ti < tmax:
	for i in range(n_particulas):
		if dt == 0:
			u = vx(x_particulas[i][1], x_particulas[i][1])	
			vf[0] = u
		else:
			u = vx(x_particulas[i - 1][1], x_particulas[i][1])	
			vf[0] = u


		if x_particulas[i][1] <= d/2:
			v_particulas[i][1] = -v_particulas[i][1]

		#evaluar vrel
		#print vf, v_particulas[i]
		vrel = vf - v_particulas[i]
		norm_vrel = norm(vrel)

		#evaluar fuerzas sobre la particula
		Fd = 0.5*Cd*norm_vrel*vrel #Drag force

		Fb = array([0.,m_w*g]) #Bouyancy force
		#print Fd
		Fi = W + Fd + Fb
		#evaluar aceleracion
		ai = Fi / m
		#integrar
		xim1 = x_particulas[i] + v_particulas[i]*dt + ai*(dt**2)/2
		vim1 = v_particulas[i] + ai*dt
		#siguiente paso
		x_p.append(x_particulas[i][0])
		y_p.append(x_particulas[i][1])

		ti += dt
		x_p[i].append(x_particulas[i][0])
		y_p[i].append(x_particulas[i][1])
		x_particulas[i] = xim1
		v_particulas[i] = vim1
#Ploteo de las trayectorias
xlabel("X")
ylabel("Y")
title("Trayectoria de particula")
for i in range(n_particulas):
	plot(x_p[i], y_p[i])
show()





