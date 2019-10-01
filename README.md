# MCOC-proyect-2
Integrantes:
=============
```
Tomás García
Javier Marín
Mauricio Sánchez
```

Introducción.

En este proyecto se busca desarrollar un programa que permita mostrar el movimiento de una partícula a través de un flujo continuo.

La anterior es una tarea de gran importancia y dificultad. Esto debido a que, de poder simular la forma en que se va a comportar una partícula en un momento determinado, se pueden hacer predicciones de su comportamiento a futuro.

Actualmente, el desarrollo de este programa está siendo estudiado por ingenieros, que buscan poder entender el comportamiento que poseen ríos y, de esta forma, construir de manera que la estructura  aguante de la mejor manera posible las interacciones con el río.


Planteamiento.

En este proyecto se trabaja para lograr una correcta anticipación del comportamiento de una partícula que se mueve en dos dimensiones, siendo estas el eje x y el eje y.

Para poder empezar a trabajar en un código que nos permita predecir el movimiento de la partícula se tiene que entender algunos puntos:

	1.- La partícula que se usa es un punto al cual se le asignó un radio de 2 mm, debido a que simplifica el código y reduce la cantidad de variables a considerar.

	2.- Se eligió este radio para que sea catalogada como arena fina, que es lo que se quiere estudiar.

	3.- Debido a que la “partícula” es un punto, se tienen que hacer arreglos para que nunca llegue a tocar el suelo, acercándose un máximo igual al tamaño del radio que se le asignó.

	4.- Al llegar a una distancia igual al radio del suelo, se considera que la partícula rebotará. Esto significa que la velocidad en x será la misma y, en cambio, la velocidad en y mantendrá el mismo módulo, pero cambiará el sentido.

	5.- Esta partícula es sometida a fuerzas continuas en ambos ejes que determinarán su comportamiento.

	6.- Debido a la interacción con fuerzas externas, además de la velocidad en el eje x e y, la partícula posee velocidad angular.

Una vez considerado estos puntos se puede proceder ver el movimiento que posee la partícula. Para esto se necesita estudiar las fuerzas que afectan a la partícula, las cuales se separan dependiendo del eje en el que actuan.

Fuerzas.

Eje x: Sólo existe una fuerza que afecta a la partícula, la cual es Drag Force. Al ser la única fuerza en esta dirección, marca la velocidad que tiene en este plano.

Eje y: Se tienen dos fuerzas que afectan a la partícula, la gravedad y bouyancy force. Al existir dos fuerzas en esta dirección, la velocidad que tendrá la partícula es el resultado de la suma de ambas fuerzas.

