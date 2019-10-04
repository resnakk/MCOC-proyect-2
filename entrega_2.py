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
Cd = 0.47 #drag coefficient
Cvm = 0.5 #virtual mass coefficient
#Euler en en x0
dt = 1e-6*_s  #paso de tiempo
tmax = 3.5#tiempo maximo de simulacion
ti = 0. #tiempo actual 
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
k = 0.41

def vx(y0,yi,v0):
	if y0 < 1:
		return 2.8*(yi - y0) + v0
	else:
		return log(30*yi)/k


#Condiciones Iniciales
n_particulas = 5 #Numero de particulas
a_rio = 11*_mm
vf = array([250*_mm*_s,0])
#historial de las particulas
x_particulas = []
v_particulas = [] 
x_p = []
y_p = []
for i in range(n_particulas): 
	valor = a_rio/n_particulas
	x_p.append([])
	y_p.append([])
	v_x = random.random()*random.randint(0,5)
	v_y = random.random()*random.randint(-2,10)
	p_x = 0. #random.random()*0.004
	p_y = (valor*(i+1)) + d 
	xi = array([p_x,p_y])
	print xi
	vi = array([v_x,v_y])
	x_particulas.append(xi)
	v_particulas.append(vi)

print v_particulas
#Iteracion en el tiempo	
xim1 = []
vim1 = []
while ti < tmax:
	for i in range(n_particulas):
		#Evaluando flujo del rio
		u1 = array([vx(x_particulas[i - 1][1],x_particulas[i][1],vf[0]), 0])
		u0 = vf	
		vf[0] = u1[0]

		#Condicion de choque entre particulas
		for t in range(n_particulas):
			if i == t:
				continue
			else:
				dif = sqrt((x_particulas[i][0] - x_particulas[t][0])**2 + (x_particulas[i][1] - x_particulas[t][1])**2)
				if dif <= d :

					v1_x = v_particulas[i][0]
					v1_y = v_particulas[i][1]
					v2_x = v_particulas[t][0]
					v2_y = v_particulas[t][1]
					v3_x = ((v1_x + v2_x) + abs(v1_x - v2_x))/2
					v4_x = v1_x + v2_x - v3_x
					v3_y = ((v1_y + v2_y) + abs(v1_y - v2_y))/2
					v4_y = v1_y + v2_y - v3_y
					v_particulas[i] = array([v3_x, v3_y])
					v_particulas[t] = array([v4_x, v4_y])
		#Condicion de suelo	
		if x_particulas[i][1] <= d/2:
			v_particulas[i][1] = -v_particulas[i][1]

		#evaluar vrel
		vrel = vf - v_particulas[i]
		norm_vrel = norm(vrel)

		#evaluar fuerzas sobre la particula
		Fd = 0.5*Cd*norm_vrel*vrel #Drag force
		Fb = array([0.,m_w*g]) #Bouyancy force
		Fvm = Cvm*(u1 - u0)/dt #Virtual mass force Fvmc
		Fi = W + Fd + Fb + Fvm
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
print v_particulas
xlabel("X")
ylabel("Y")
title("Trayectoria de particula")
for i in range(n_particulas):
	plot(x_p[i], y_p[i])
show()
#savefig("figura.png")





