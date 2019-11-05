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
				vel_j = array([vector[j + 2],vector[j + 3]])
				dif = sqrt((pos_i[0] - pos_j[0])**2 + (pos_i[1] - pos_j[1])**2)
				#Choque con Ley de hook
				if dif < d:
					rij = pos_j - pos_i 
					F_Choque[i/4] = k_resorte*dif*rij/norm(rij)
					F_Choque[j/4] = -k_resorte*dif*rij/norm(rij)
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
		Fi = W + Fd + Fb + F_Choque[i/4] + F_rebote + Fl + Fvm
		#=================================================================retornos=================================================================
		acc = Fi/m
		ret.append(vel_i[0])
		ret.append(vel_i[1])
		ret.append(acc[0])
		ret.append(acc[1])
		i += 4 
	return ret