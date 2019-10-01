from matplotlib.pylab import *
#unidades SI
_m = 1.
_mm = _m*1e-3
_gr = 1e-3
_s = 1.
_kg = 1.

#perfil logaritmico de velocidad en x
xi = array([0., 2.1*_mm], dtype = double) #posicion actual
k = 0.41
def vx(y0):
	return 5*log(3*y0)/k
vf = array([5.,0]) #m/s 
vi = array([0., 0.], dtype = double) #velocidad actual

xim1 = zeros(2, dtype = double) #posicion siguiente
vim1 = zeros(2, dtype = double) #velocidad siguiente
d = 2*_mm
g = 9.81*_m/_s**2
rho = 2700*_kg/(_m**3)
rho_w = 1000*_kg/(_m**3)
m = rho*pi*(d**3)*(4./3./8.)
m_w = rho_w*pi*(d**3)*(4./3./8.)
Cd = 0.47 #particula redonda
#Euler en en x0
dt = 1e-6*_s  #paso de tiempo
tmax = 0.5 #tiempo maximo de simulacion

ti = 0. #tiempo actual 


W = array([0, -m*g])
#vf = array([5., 0.]) #Velocidad inicial del fluido 

x_store = []
y_store = []
v_store = []

while ti < tmax:
		
	
	
	if xi[1] <= d/2:
		vi[1] = -vi[1]

	#evaluar vrel
	vrel = vf - vi
	
	norm_vrel = norm(vrel)
	
	#evaluar fuerzas sobre la particula
	Fd = 0.5*Cd*norm_vrel*vrel #Drag force
	Fb = array([0.,m_w*g]) #Bouyancy force
	#print Fd
	Fi = W + Fd + Fb
	#evaluar aceleracion
	ai = Fi / m
	#integrar
	xim1 = xi + vi*dt + ai*(dt**2)/2
	vim1 = vi + ai*dt
	#siguiente paso
	x_store.append(xi[0])
	y_store.append(xi[1])
	v_store.append(vi)
	#print vi
	
	ti += dt
	xi = xim1
	vi = vim1
xlabel("X")
ylabel("Y")
title("Trayectoria de particula")
plot(x_store, y_store)
show()





