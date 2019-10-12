#README Javier Marín

Introducción
=============

En este proyecto se usó de base el proyecto pasado, con la diferencia de que se agregaron n partículas, siendo n el número de interes, y más fuerzas. Todo esto con el interes de hacer un planteamiento del modelo y del movimiento de partículas más real. Cabe destacar que este planteamiento todavía está lejos de ser cercano a la realidad, debido a que faltan mejoras en el rebote de las partículas y planteamiento de las fuerzas

Planteamiento.
==============

En este proyecto se trabaja para lograr una correcta anticipación del comportamiento de n partículas que se mueve en dos dimensiones, siendo estas el eje x y el eje y.

Para lograr una estimación más aproximada se utilizaron las carpetas de simpy y de matplotlib de python. Estas son librerias que tienen funciones que nos ayudaron a modelar nuestro moviemiento de partículas.

Para poder entender las diferencias de entre el modelamiento de una partícula, con el de n partículas y con fuerzas extas se tiene que entender lo siguiente:

	1) Gravedad, que es la fuerza que mueve las partículas hacia el "eje y", cuando el módulo del mismo es 0.
	2) Lift force, que es la fuerza de empuje del agua que mueve las partículas en el "eje y" hacia número más grande.
	3) Drag force, que es la fuerza que ejerce el rio en el "eje x" a la partícula.
	4) Bouyanci force, es la fuerza que, dependiente de la dencidad del líquido y la masa externa, la partícula intenta establecerse en un lugar, para llegar al lugar al cual está en equilibrio de presiones.
	5) La masa que le generamos a la partícula para que esta se vea afectada por las fuerzas anteriores y sus velocidades se vean afectadas por las mismas.

Una vez considerado estos puntos se puede proceder ver el movimiento que poseen las partículas. Para esto se necesita estudiar las fuerzas que afectan a la partícula, las cuales se separan dependiendo del eje en el que actuan.
5 particulas 5 segundos 17 segundos

Fuerzas.
========

Eje x: Sólo existe una fuerza que afecta a la partícula, la cual es Drag Force. Al ser la única fuerza en esta dirección, marca la velocidad que tiene en este plano.

Eje y: Se tienen tres fuerzas que afectan a la partícula, la gravedad, lift force y bouyancy force. Al existir tres fuerzas en esta dirección, la velocidad que tendrá la partícula es el resultado de la suma de todas las fuerzas.


Resultados.
===========

![Resultado](https://github.com/resnakk/MCOC-proyect-2/blob/master/Mauricio%20Sanchez/3p.png)
![Resultado](https://github.com/resnakk/MCOC-proyect-2/blob/master/Mauricio%20Sanchez/5p.png)
![Resultado](https://github.com/resnakk/MCOC-proyect-2/blob/master/Mauricio%20Sanchez/10p.png)

Comentarios.
============

En las imagenes se pueden observar como todas las partículas, que parten en lugares diferentes, siguien un movimiento parecido, debido a las fuerzas que en ellas actuan. Además, podemos apreciar que estas sufren choques notorios, en los cuales desvían su camino.

Este codigo fué implementado para 3, 5 y 10 partículas, demorandose cada implemtación un tiempo considerablemente diferente. 

