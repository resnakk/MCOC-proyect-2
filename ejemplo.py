from matplotlib.pylab import *
import random 
#unidades SI
_m = 1.
_mm = _m*1e-3
_gr = 1e-3
_s = 1.
_kg = 1.

dicc = {}
dicc["a"] = [1, 2, 3]
print(dicc.get("a"))


xi = array([0., 2.1*_mm], dtype = double) #posicion actual 
k = 0.41
#perfil logaritmico de velocidad en x
def vx(y0,v0,yi):
    if y0 < 1:
        return 2.8*(yi - y0) + v0
    else:
        return v0*log(3*y0)/k
#Condiciones Iniciales
n_particulas = 5 #Numero de particulas
x_particulas = []
v_particulas = []
vf = array([5**_m/_s,0])  
x_p = {}
y_p = {}
for i in range(n_particulas): 
    x_particula_i = "xp_{}".format(i + 1)
    y_particula_i = "yp_{}".format(i + 1)
    x_p[x_particula_i] = []
    y_p[y_particula_i] = []
    v_x = 0
    v_y = 0
    p_x = 5*random.random()
    p_y = 5*random.random()
    xi = array([p_x,p_y])
    vi = array([v_x,v_y])

    x_particulas.append(xi) #Le da posiciones iniciales a todas las partículas
    v_particulas.append(vi) #Le da velocidades iniciales 0 a todas las partículas
    

d = 2*_mm
g = 9.81*_m/_s**2
rho = 2700*_kg/(_m**3)
rho_w = 1000*_kg/(_m**3)
m = rho*pi*(d**3)*(4./3./8.)
m_w = rho_w*pi*(d**3)*(4./3./8.)
Cd = 0.47 #particula redonda
#Euler en en x0
dt = 1e-6*_s  #paso de tiempo
tmax = 0.1 #tiempo maximo de simulacion
ti = 0. #tiempo actual 
W = array([0, -m*g])

x_store = []
y_store = []
v_store = []
xim1 = []
vim1 = []
y_inicial = []

for i in x_particulas: #Agrega las posiciones en y iniciales de todas las partículas. NO es necesario este ciclo, se puede usar la lista inicial 
    y_inicial.append(i[1])

while ti < tmax: #Se recorre en cada tiempo para todas las partículas
    for i in range(n_particulas):

        x_particula_i = "xp_{}".format(i + 1) #Asigna los nombres de la particula en x
        y_particula_i = "yp_{}".format(i + 1) #Asigna los nombres de la particula en y
        u = vx(y_inicial[i], vf[0], x_particulas[i][1]) #Actualiza la velocidad en y de cada partícula. El primer y el último parámetro son iguales
        vf[0] = u #guarda la velocidad para usarla en el próximo ciclo

        if x_particulas[i][1] <= d/2: #Se asegura que la particula no llegue al piso
            vi[1] = -vi[1]

        #evaluar vrel
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
        prueba = x_p.get(x_particula_i) + [x_particulas[i][0]]
        x_p[x_particula_i] = prueba

        prueba = y_p.get(y_particula_i) + [x_particulas[i][1]]
        y_p[y_particula_i] = prueba
        
        ti += dt
        x_particulas[i] = xim1
        v_particulas[i] = vim1

xlabel("X")
ylabel("Y")
title("Trayectoria de particula")
for i in range(n_particulas):
    plot(x_p["xp_{}".format(i + 1)], y_p["yp_{}".format(i + 1)])
#plot(x_p["xp_1"], y_p["yp_1"])
show()




