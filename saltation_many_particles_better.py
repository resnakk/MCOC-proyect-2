from matplotlib.pylab import *
from scipy.integrate import odeint
import random 
from datetime import datetime
import copy
#=================================================================unidades SI=================================================================
_m = 1.
_mm = _m*1e-3
_gr = 1e-3
_s = 1.
_kg = 1.
#=================================================================Condiciones Iniciales=================================================================
n_particulas = 5 #Numero de particulas
a_rio = 1*_mm
uf = array([10*_mm/_s,0])
#=================================================================Datos=================================================================
d = 0.15*_mm
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
dt = 1e-4*_s  #paso de tiempo
tmax = 0.005#tiempo maximo de simulacion
t = arange(0, tmax, dt)
W = array([0, -m*g])
#perfil logaritmico de velocidad en x
#=================================================================Funciones=================================================================

def ux(y0,yi,u0):
	if y0 < 1:
		return 2.8*(yi - y0) + u0
	else:
		return log(30*yi)/k_log

def choque_m_particulas(vector, t):
	F_Choque = [] 
	for i in range(int(len(vector)/4)):
		F_Choque.append([])
	ret = []
	i = 0
	while i < len(vector):
		pos_x1 = vector[i]
		pos_y1 = vector[i + 1]
		j = i + 4 
		while j < len(vector):
			pos_x2 = vector[j]
			pos_y2 = vector[j + 1]
			kk, kk2 = pos_x1 - pos_x2,  pos_y1 - pos_y2
			rij = array([kk, kk2])
			dif = sqrt((pos_x1 - pos_x2)**2 + (pos_y1 - pos_y2)**2)
			F_Choque[int(i/4)] = k_resorte*dif*rij/norm(rij)
			F_Choque[int(j/4)] = -k_resorte*dif*rij/norm(rij)
			j += 4
		F_rebote = array([0,0])
		if pos_y1 <= d/2:
			rji = array([0, pos_y1 - d/2])
			F_rebote = -k_resorte*rji
		print vector	 
		#=================================================================Velocidad relativa=================================================================
		vel_i = array([vector[i + 2], vector[i + 3]])
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
		Fvm = array([-alpha*Cvm*vel_i[1]*uf[0]/(Cvm*pos_y1),0])
		Fi = W + Fd + Fb + F_Choque[int(i/4)] + F_rebote + Fl + Fvm
		#=================================================================retornos=================================================================
		acc = Fi/m
		ret.append(vel_i[0])
		ret.append(vel_i[1])
		ret.append(acc[0])
		ret.append(acc[1])
		i += 4 
	return ret

def movimiento(vector, t):
	ret = []
	vel_i = array([vector[2], vector[3]])
	F_rebote = array([0,0])
	if vector[	1] <= d/2:
		rji = array([0, vector[1] - d/2])
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
	Fvm = array([-alpha*Cvm*vel_i[1]*uf[0]/(Cvm*vector[1]),0])
	Fi = W + Fd + Fb + F_rebote + Fl + Fvm
	#=================================================================retornos=================================================================
	acc = Fi/m
	ret.append(vel_i[0])
	ret.append(vel_i[1])
	ret.append(acc[0])
	ret.append(acc[1])
	return ret

fout = open("results.txt", "w")
#Condiciones iniciales pos, u 
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
v_total = copy.copy(vector_inicial)
#Inicio simulacion
t_actual = 0
k = 0
while k < tmax:
	i = 0
	fout.write("{}".format(k ))

	savetxt(fout, v_total, fmt = '%.24e  ', newline = "")
	fout.write("\n\n")
	while i < len(vector_inicial) - 8:
		pos_x1 = vector_inicial[i]
		pos_y1 = vector_inicial[i + 1]
		vel_x1 = vector_inicial[i + 2]
		vel_y1 = vector_inicial[i + 3]
		p_i =[pos_x1, pos_y1, vel_x1, vel_y1] 
		particulas_chocando = [pos_x1, pos_y1,vel_x1, vel_y1]
		indices_p_chocando = [i]
		j = i + 4
		while j < len(vector_inicial) :
			pos_x2 = vector_inicial[j]
			pos_y2 = vector_inicial[j + 1]
			vel_x2 = vector_inicial[j + 2]
			vel_y2 = vector_inicial[j + 3]
			rij = sqrt((pos_x1 - pos_x2)**2 + (pos_y1 - pos_y2)**2)
			#Condicion de choque
			if rij <= 3*d/2:
				print rij
				particulas_chocando.append(pos_x2)
				particulas_chocando.append(pos_y2)
				particulas_chocando.append(vel_x2)
				particulas_chocando.append(vel_y2)
				indices_p_chocando.append(j)
			j += 4
		#Posicion futura
		if len(particulas_chocando) > 4:
			v_fin = odeint(choque_m_particulas, particulas_chocando, [t_actual , t_actual + dt])

			for l in range(len(indices_p_chocando)):
				c = 0
				for m in v_fin[1]:
					v_total[l + c] = m
					c += 1 
				
				
			i += 4

		else:
		 	#print(len(v_total))
			v_fin = odeint(movimiento, p_i, [t_actual, t_actual + dt])
			for m in v_fin[1]:
				v_total[i] = m
				



			
			
			i += 4
	k += dt	
fout.close()

