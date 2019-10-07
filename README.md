#README Mauricio Sánchez

El presente trabajo busca modelar mediante un método lagrangiano el transporte de sedimentos en canales de agua de flujo continuo, no turbulento, principalmente de arenas finas y gravas. Sumado a lo anterior, el segundo foco de este proyecto, es estudiar como influye la decisión del algoritmo a implementar, y como varía su rendimiento a medida que se le exige más al modelo.

Para la realización de este modelo se consideraron varios supuestos de tal manera que fuera valido: 
```
	1.- Se consideró que todas las particulas son identicas, y tienen un diametro de 2 mm, puesto que este diametro diferencia a las arenas finas de las gruesas.
	2.- El modelo esta pensado para particulas esféricas perfectas, sin dar a alugar a particulas no uniformes. 
	3.- Todas las particulas son identicas, pero inician sus trayectorias con posiciones y velocidades aleatorias
	4.- Se asume que el suelo es liso, y sin coeficiente de roce. 
	5.- El flujo del canal se rige por un perfil logaritmico basado en la ley de Von Kárnmán-Prandtl.
```
Como este modelo busca predecir la trayectoria de varias particulas al mismo tiempo, se requiere de métodos de integración que retornen el comportamiento de estas, en base a las condiciones mencionadas anteriormente, los cuales se ven limitados por la cantidad de particulas, y por el tiempo en que se estudia su monvimiento.

Primero se utilizó el método de euler, el cual se ve extremadamente limitado por el tiempo de estudio, más que por el número de 
Para hacer esto se utilizó el método de euler para realizar la integración; este método si bien cumple su objetivo, se ve muy limitado cuando se aumenta mucho el numero de particulas
Planteamiento.
==============

En este proyecto se trabaja para lograr una correcta anticipación del comportamiento de una partícula que se mueve en dos dimensiones, siendo estas el eje x y el eje y.

Para poder empezar a trabajar en un código que nos permita predecir el movimiento de la partícula se tiene que entender algunos puntos:

	1.- La partícula que se usa es un punto al cual se le asignó un radio de 2 mm, debido a que simplifica el código y reduce la cantidad de variables a considerar.

	2.- Se eligió este radio para que sea catalogada como arena fina, que es lo que se quiere estudiar.

	3.- Debido a que la “partícula” es un punto, se tienen que hacer arreglos para que nunca llegue a tocar el suelo, acercándose un máximo igual al tamaño del radio que se le asignó.

	4.- Al llegar a una distancia igual al radio del suelo, se considera que la partícula rebotará. Esto significa que la velocidad en x será la misma y, en cambio, la velocidad en y mantendrá el mismo módulo, pero cambiará el sentido.

	5.- Esta partícula es sometida a fuerzas continuas en ambos ejes que determinarán su comportamiento.

	6.- El flujo se rige por un perfil logarítmico, el cual se basa en la ley de von Kárnmán-Prandtl.

La velocidad según la ley de von Kárnmán-Prandtl sigue el siguiente comportamiento:
https://github.com/resnakk/MCOC-proyect-2/blob/master/figure_13.jpeg

Una vez considerado estos puntos se puede proceder ver el movimiento que posee la partícula. Para esto se necesita estudiar las fuerzas que afectan a la partícula, las cuales se separan dependiendo del eje en el que actuan.


Fuerzas.
========

Eje x: Sólo existe una fuerza que afecta a la partícula, la cual es Drag Force. Al ser la única fuerza en esta dirección, marca la velocidad que tiene en este plano.

Eje y: Se tienen dos fuerzas que afectan a la partícula, la gravedad y bouyancy force. Al existir dos fuerzas en esta dirección, la velocidad que tendrá la partícula es el resultado de la suma de ambas fuerzas.


Resultados.
===========

![Resultado](https://github.com/resnakk/MCOC-proyect-2/blob/master/figure_1.png)
![Resultado](https://github.com/resnakk/MCOC-proyect-2/blob/master/figure_12.png)


Comentarios.
============

La primera imagen muestra el movimiento de la partícula, el cual es agrandado en la imagen siguiente para que se pueda apreciar de mejor manera el movimiento parabólico que esta posee.

Se puede apreciar que la partícula posee velocidad tanto en el eje x como y, observandose que la velocidad en el eje x no sufre cambios aparente. En cambio, se puede ver que después de cada rebote la altura que alcanza la partícula es menor, lo que provoca que cada salto que haga sea menor que el anterior. Este es el comportamiento que se espera de la partícula
