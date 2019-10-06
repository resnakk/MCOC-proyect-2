from matplotlib.pylab import *
from scipy.integrate import odeint
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
tmax = 3#tiempo maximo de simulacion
t = arange(0, tmax, dt)
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
k = 0.41
#Condiciones Iniciales
n_particulas = 5 #Numero de particulas
a_rio = 11*_mm
uf = array([250*_mm*_s,0])
#Funciones
def ux(y0,yi,u0):
	if y0 < 1:
		return 2.8*(yi - y0) + u0
	else:
		return log(30*yi)/k
def movimiento(vector, t):
	ret = []
	i = 0
	while i < len(vector):
		pos_i = array([vector[i],vector[i + 1]])
		vel_i = array([vector[i + 2],vector[i + 3]])
		#condicion de choque
		j = 0
		while j < len(vector):
			if i == j:
				j += 4
			else:
				pos_j = array([vector[j],vector[j + 1]])
				vel_j = array([vector[j + 2],vector[j + 3]])
				dif = sqrt((pos_i[0] - pos_j[0])**2 + (pos_i[1] - pos_j[1])**2)
				if dif <= d:
					u1_x = pos_i[0]
					u1_y = pos_j[1]
					u2_x = pos_i[0]
					u2_y = pos_j[1]
					u3_x = ((u1_x + u2_x) + abs(u1_x - u2_x))/2
					u4_x = u1_x + u2_x - u3_x
					u3_y = ((u1_y + u2_y) + abs(u1_y - u2_y))/2
					u4_y = u1_y + u2_y - u3_y
					vel_i = array([u3_x,u3_y])
					vel_j = array([u4_x,u4_y])
					vector[j + 2] = u4_x
					vector[j + 3] = u4_y
					
				 
			j += 4
		#condicion de suelo
		if pos_i[1] <= d/2:
			vel_i[1] = -vel_i[1]
		#Velocidad relativa
		urel = uf - vel_i
		norm_urel = norm(urel)
		#Fuerzas sobre la particula
		Fd = 0.5*Cd*norm_urel*urel #Drag force
		Fb = array([0.,m_w*g]) #Bouyancy force
		Fvm = Cvm*(uf)/dt #Virtual mass force Fvmc
		Fi = W + Fd + Fb + Fvm
		#retornos
		ret.append(pos_i[0])
		ret.append(pos_i[1])
		ret.append(vel_i[0])
		ret.append(vel_i[1])
		i += 4 
	return ret 
#Prediccion
vector_inicial = []
for i in range(n_particulas): 
	valor = a_rio/n_particulas
	u_x = random.random()*random.randint(0,5)
	u_y = random.random()*random.randint(-2,10)
	p_x = 0. #random.random()*0.004
	p_y = (valor*(i+1)) + d 
	vector_inicial.append(p_x)
	vector_inicial.append(p_y)
	vector_inicial.append(u_x)
	vector_inicial.append(u_y)
print (len(vector_inicial))
#Integracion con odeint	

v_final = odeint(movimiento,vector_inicial, t)

i = 0
while i < range(len(v_final)):
	plot(v_final[i], v_final[i + 1])
	print v_final[i]
	print len(v_final)
	break
show()




"""
pos_xy = []
k = 0
while k < len(v_final)/4:
	if k%4 == 0:
		pos_xy.append([])
	pos = v_final[k]
"""


'''
#Iteracion en el tiempo	
xim1 = []
uim1 = []
while ti < tmax:
	for i in range(n_particulas):
		#Evaluando flujo del rio
		u1 = array([vx(x_particulas[i - 1][1],x_particulas[i][1],uf[0]), 0])
		u0 = uf	
		uf[0] = u1[0]

		#Condicion de choque entre particulas
		for t in range(n_particulas):
			if i == t:
				continue
			else:
				dif = sqrt((x_particulas[i][0] - x_particulas[t][0])**2 + (x_particulas[i][1] - x_particulas[t][1])**2)
				if dif <= d :

					u1_x = u_particulas[i][0]
					u1_y = u_particulas[i][1]
					u2_x = u_particulas[t][0]
					u2_y = u_particulas[t][1]
					u3_x = ((u1_x + u2_x) + abs(u1_x - u2_x))/2
					u4_x = u1_x + u2_x - u3_x
					u3_y = ((u1_y + u2_y) + abs(u1_y - u2_y))/2
					u4_y = u1_y + u2_y - u3_y
					u_particulas[i] = array([u3_x, u3_y])
					u_particulas[t] = array([u4_x, u4_y])
		#Condicion de suelo	
		if x_particulas[i][1] <= d/2:
			u_particulas[i][1] = -u_particulas[i][1]

		#evaluar vrel
		urel = uf - u_particulas[i]
		norm_urel = norm(urel)

		#evaluar fuerzas sobre la particula
		Fd = 0.5*Cd*norm_urel*urel #Drag force
		Fb = array([0.,m_w*g]) #Bouyancy force
		Fvm = Cvm*(u1 - u0)/dt #Virtual mass force Fvmc
		Fi = W + Fd + Fb + Fvm
		#evaluar aceleracion
		ai = Fi / m
		#integrar
		xim1 = x_particulas[i] + u_particulas[i]*dt + ai*(dt**2)/2
		uim1 = u_particulas[i] + ai*dt
		#siguiente paso
		x_p.append(x_particulas[i][0])
		y_p.append(x_particulas[i][1])
		ti += dt
		x_p[i].append(x_particulas[i][0])
		y_p[i].append(x_particulas[i][1])
		x_particulas[i] = xim1
		u_particulas[i] = uim1
#Ploteo de las trayectorias
xlabel("X")
ylabel("Y")
title("Trayectoria de particula")
for i in range(n_particulas):
	plot(x_p[i], y_p[i])
show()
#savefig("figura.png")
'''



