# MCOC-proyect-2

Nombre:
=============
Tomás García


INTRODUCCIÓN:
=============
En este proyecto se modeló el movimiento de particulas dentro de un fluido, ambos con propiedades y caracteristicas conocidas. Los objetivos del estudió de este comportamiento, es predecir el movimiento de la particula, con información de un solo instante de la particula, en este caso, las condiciones iniciales de esta.
Las posibles aplicaciones de esto son dentro del analisis de rios y lagos o el transporte de material como hormigón, ya que, conocer como se comporta, se puede idear una mejor estrategia al momento de construir, por ejemplo puentes o represas. 

MODELO:
=============
El programa grafica en 2-D la trayectoria de N particulas en el espacio, en un tiempo conocido.

Supuestos
-------------
+ Las particulas son esfericas con el mismo radio, siendo este de 2 mm, es decir catalogado como arena fina.
+ Las particulas se distribuyen aleatoriamente, con la precaución de que ninguna esta superpuesta con otra.
+ El rebote contra el suelo es la misma magnitud y sentido en el eje X, pero en el eje Y, la magnitud es la misma pero el sentido es el contrario.
+ El flujo se rige por un perfil logarítmico, el cual se basa en la ley de von Kárnmán-Prandtl. https://sites.google.com/site/scientiaestpotentiaplus/espessura-de-camada-limite
+ Los choques entre particulas son totalmente elasticos, solo se altera las velocidades en X e Y.

Ya conociendo el comportamiento de una particula, se consideraron las siguientes fuerzas que afectan a cada una de estas:

Fuerzas
-------------
+ Gravedad.
+ Masa virtual.
+ Arrastre (Drag).
+ Flotacion (Bouyacy).
+ Empuje (Lift).

Donde sumando estas y diviendo por el peso de la particula, obtenemos la aceleración y con esto se modifica la trayectoria de cada particula por el intervalo de tiempo dado.
Lo anterior se integra a traves de la funcione odeint, la cual es una funcion se sympy, la cual consiste en un metodo de python, el cual esta optimizado, con el objetivo de que el codigo se demore poco tiempo, en promedio de 12,5 segundos para 5 particulas, para 15 particulas 125 segundos, ya con 20 de estas el computador colapsando.


RESULTADOS:
=============
![Resultado](https://github.com/resnakk/MCOC-proyect-2/Mauricio%20Sanchez/blob/master/1p.png)
Grafico para 1 particula

![Resultado](https://github.com/resnakk/MCOC-proyect-2/Mauricio%20Sanchez/blob/master/3p.png)
Grafico para 3 particulas

![Resultado](https://github.com/resnakk/MCOC-proyect-2/Mauricio%20Sanchez/blob/master/5p.png)
Grafico para 5 particulas

![Resultado](https://github.com/resnakk/MCOC-proyect-2/Mauricio%20Sanchez/blob/master/10p.png)
Grafico para 10 particulas


COMENTARIOS:
=============
La modelación de una particula funciono, generando una trayectoria razonable, sin embargo, cuando existieron choques entre particulas, la primera que detecta el golpe cambia la trayectoria, sin embargo, la segunda, es decir contra la que hubo un contacto, esta no se ve afectada, continuando como si no hubiera ocurrido nada, ademas de este error, cuando se encuentran en el piso, esto se modela de manera extraña, en algunos casos, subiendo un radio de distancia el conjunto de particulas, continuando con una trayectoria inversa en comparacion con el rebote normal.

Los errores anteriores podrian deberse a que no guardamos la informacion de la segunda particula afectada, ya que a esta sus fuerzas cambian, esto no se hizo ya que, como cada particula se integra en el mismo momento, la segunda, al momento de ser integrada su trayectoria, esta tambien deberia de cambiar. Las condiciones en el suelo, cuando hay mas de una particula, el programa cuando integra debe generar trayectorias que se interponen unas con otras por las condiciones de borde, habra que trabajar en esas condiciones para la version del programa.

La velocidad del flujo fue modelada como uniforme, porque, cuando se utilizo el perfil logaritmico el codigo arrojaba errores o trayectorias incoherentes, por lo cual se opto por utilizar una uniforme, con meta para la siguiente version implementar el perfil correspondiente.
