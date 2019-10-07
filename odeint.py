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
dt = 1e-5*_s  #paso de tiempo
tmax = 2.5#tiempo maximo de simulacion
t = arange(0, tmax, dt)
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
k = 0.41
#Condiciones Iniciales
n_particulas = 5 #Numero de particulas
a_rio = 11*_mm
uf = array([500*_mm/_s,0])
#Funciones
def ux(y0,yi,u0):
	if y0 < 1:
		return 2.8*(yi - y0) + u0
	else:
		return log(30*yi)/k
		print "hola"
def movimiento(vector, t):
	ret = []
	i = 0
	while i < len(vector):
		pos_i = array([vector[i],vector[i + 1]])
		vel_i = array([vector[i + 2],vector[i + 3]])
		#print pos_i
		#uf = -log(30*pos_i[1])/k
		#print uf 
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
					u1_x = vel_i[0]
					u1_y = vel_i[1]
					u2_x = vel_j[0]
					u2_y = vel_j[1]
					u3_x = ((u1_x + u2_x) + abs(u1_x - u2_x))/2
					u4_x = u1_x + u2_x - u3_x
					u3_y = ((u1_y + u2_y) + abs(u1_y - u2_y))/2
					u4_y = u1_y + u2_y - u3_y
					vel_i = array([u3_x,u3_y])
					vel_j = array([u4_x,u4_y])
					#vector[j + 2] = u4_x
					#vector[j + 3] = u4_y
					j += 4
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
		acc = Fi/m
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
	u_x = random.random()*random.randint(1,5)
	u_y = random.random()*random.randint(1,5)
	p_x = random.random()*0.004
	p_y = (valor*(i+1)) + d 
	vector_inicial.append(p_x)
	vector_inicial.append(p_y)
	vector_inicial.append(u_x)
	vector_inicial.append(u_y)
#Integracion con odeint	

#exit()
v_final = odeint(movimiento,vector_inicial, t)

print v_final
print len(v_final)
x =[]
y = []
for i in range(n_particulas):
	x.append([])
	y.append([])


i = 0
while i < len(v_final) - 1:
	cont = 0
	j = 0
	while j < len(v_final[i]) - 1:
		if j%4 == 0:
			x[cont].append(v_final[i][j])
		if j%4 == 1:
			y[cont].append(v_final[i][j])
			cont += 1
		j += 1
	i += 1

#exit()
k = 0
while k < len(x):
	plot(x[k], y[k])
	#print x[k]
	k += 1
show()
