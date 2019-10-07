# MCOC-proyect-2


Nombre:
=============
```
Tomás García
```
=============

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
+ Gravedad
+ Masa virtual
+ Arrastre
+ Flotacion

Donde sumando estas y diviendo por el peso de la particula, obtenemos la aceleración y con esto se modifica la trayectoria de cada particula por el intervalo de tiempo dado.


RESULTADOS:
=============


COMENTARIOS:
=============

