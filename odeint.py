from matplotlib.pylab import *
from scipy.integrate import odeint
import random 
#=================================================================unidades SI=================================================================
_m = 1.
_mm = _m*1e-3
_gr = 1e-3
_s = 1.
_kg = 1.
#=================================================================Condiciones Iniciales=================================================================
n_particulas = 10 #Numero de particulas
a_rio = 40*_mm
uf = array([10*_mm/_s,0])
#=================================================================Datos=================================================================
d = 2*_mm
A = pi*(d/2)**2
g = 9.81*_m/_s**2
rho = 2700*_kg/(_m**3)
rho_w = 1000*_kg/(_m**3)
m = rho*pi*(d**3)*(4./3./8.)
m_w = rho_w*pi*(d**3)*(4./3./8.)
Cd = 0.47 #drag coefficient
Cvm = 0.5 #virtual mass coefficient
Cl = 0.2 #Lift force coefficient
k_log = 0.41 #K para perfil logaritmico
k_resorte = 1000*0.5*Cd*rho_w*A*norm(uf[0])/(1*_mm) #K para simular el choque 
#Euler en en x0
dt = 1e-3*_s  #paso de tiempo
tmax = 3#tiempo maximo de simulacion
t = arange(0, tmax, dt)
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
#=================================================================Funciones=================================================================
def ux(y0,yi,u0):
	if y0 < 1:
		return 2.8*(yi - y0) + u0
	else:
		return log(30*yi)/k_log
def movimiento(vector, t):
	ret  = []
	F_Choque = []
	for i in range(len(vector)):
		F_Choque.append(array([0,0]))
	i = 0
	while i < len(vector):
		pos_i = array([vector[i],vector[i + 1]])
		vel_i = array([vector[i + 2],vector[i + 3]]) 
		#=================================================================condicion de choque=================================================================
		j = 0
		while j < len(vector):
			if i == j:
				j += 4
			else:
				pos_j = array([vector[j],vector[j + 1]])
				#vel_j = array([vector[j + 2],vector[j + 3]])
				dif = sqrt((pos_i[0] - pos_j[0])**2 + (pos_i[1] - pos_j[1])**2)
				#Choque con Ley de hook
				if dif < d:
					rij = pos_j - pos_i
					i2 = int(i/4)
					j2 = int(j/4)
					F_Choque[i2] = k_resorte*dif*rij/norm(rij)
					F_Choque[j2] = -k_resorte*dif*rij/norm(rij)
			j += 4
		#=================================================================condicion de suelo=================================================================
		F_rebote = array([0,0])
		if pos_i[1] <= d/2:
			rji = array([0, pos_i[1] - d/2])
			F_rebote = -k_resorte*rji	 
		#=================================================================Velocidad relativa=================================================================
		urel = uf - vel_i 
		norm_urel = norm(urel)
		#=================================================================Fuerzas sobre la particula=================================================================
		Fd = 0.5*Cd*norm_urel*urel #Drag force
		Fb = array([0.,m_w*g]) #Bouyancy force
		#Lift force
		R = (rho/rho_w - 1)
		alpha = (1 + R + Cvm)**-1 
		Fl = array([0, (3/4)*alpha*Cl*(norm(0.9*vel_i)**2 - norm(1.1*vel_i)**2)])
		#Virtual mass force
		Fvm = array([-alpha*Cvm*vel_i[1]*uf[0]/(Cvm*pos_i[1]),0])
		i1 = int(i/4)
		Fi = W + Fd + Fb + F_Choque[i1] + F_rebote + Fl + Fvm
		#=================================================================retornos=================================================================
		acc = Fi/m
		ret.append(vel_i[0])
		ret.append(vel_i[1])
		ret.append(acc[0])
		ret.append(acc[1])
		i += 4 
	return ret
#=================================================================Prediccion=================================================================
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
#=================================================================Integracion con odeint=================================================================	
v_final = odeint(movimiento,vector_inicial, t)
print(v_final)
x = v_final[:,0::4]
y = v_final[:,1::4]
plot(x,y)
savefig("figura1")
