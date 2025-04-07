# Control neumático de cilindros de simple efecto

## Objetivo
- Construir el circuito neumático de mando para el control combinacional de cilindros de simple efecto, empleando válvulas neumáticas 3/2.

- Diseñar e implementar el circuito de mando neumático para el control combinacional de cilindros de simple efecto empleando válvulas neumáticas 3/2, y válvulas lógicas OR y AND.

## Marco teórico
Los componentes neumáticos son elementos que utilizan aire comprimido como fuente para su funcionamiento. Existen elementos como cilindros y pistones que realizarán un movimiento mecánico de desplazamiento al serles aplicado aire comprimido por alguna de sus entradas.

Existen, a su vez, elementos de control llamados válvulas; las válvulas todo-nada por ejemplo, son dispositivos binarios que controlan el flujo y la presión de un fluido, aire en el caso neumático. Algunas de estas válvulas permiten conectar una línea de presión al suministro del fluido, o conectar dicha línea a la atmósfera. Otras permiten invertir el sentido del flujo, invirtiendo la presión en una línea de presión.

### Cilindros de simple efecto

En los cilindros de simple efecto, el aire comprimido es aplicado en un solo lado de la cara del pistón; el otro lado está abierto a la atmósfera. Los cilindros pueden desarrollar trabajo en una sola dirección. El regreso del movimiento del pistón es realizado por un resorte interno o por la aplicación de una fuerza externa.

La fuerza del resorte regresa al pistón a su posición inicial con una razonable alta velocidad bajo condiciones sin carga. El golpe de regreso entonces está limitado por las características naturales del resorte.

Este tipo de cilindros requieren sólo una conexión neumática y un puerto de descarga. El puerto de descarga debe estar libre de obstrucciones para asegurar que el pistón no esté restringido por el paso del aire. Es normalmente colocado un filtro en el puerto de descarga.

![Cilindro Simple Efecto](./assets/cilSimEfecto.png)

Figura 1. Cilindro de simple efecto.

El pistón en el cilindro de simple efecto operará entonces por el suministro de aire comprimido por su único puerto de entrada. Cuando la fuente de aire comprimido es eliminada, el pistón regresará a su posición inicial con la ayuda de un resorte interno. 

La figura 1. ilustra el diagrama representativo de un cilindro de simple efecto.
Válvula de dos posiciones tres vías normalmente cerrada. El símbolo utilizado para representar una válvula de este tipo accionada manualmente se muestra en la figura 2.

![Valvula 3/2 accionada manualmente](./assets/valvulaAccMec.png)
Figura 2. Válvula 3/2 accionada manualmente.

La entrada P se conecta a la presión de suministro, la salida A se conecta a la línea de presión que se desea controlar y la toma R es la descarga a la atmósfera. Esta última toma no está disponible para conectarla a ninguna línea.

El funcionamiento de la válvula es de la siguiente forma:

- Cuando la válvula se encuentra en su posición normal, es decir, cuando no se ha accionado, la entrada P está bloqueada y la salida A está conectada a la atmósfera. Ésta es la posición mostrada en el diagrama.

- Cuando se acciona la válvula, la entrada P se conecta a la salida A y el orificio de descarga queda bloqueado.

En el símbolo de la válvula se muestran ambas condiciones. En el cuadro inferior se mues- tra la condición normal (no accionada).

### Función lógica "AND" con componentes neumáticos.

En la figura 3 se muestra una forma de construir la función lógica AND con válvulas neumáticas. Utilizando dos válvulas 3/2 normalmente cerradas de accionamiento neumático. En este caso la salida A es igual a Y, AND Y2, esta salida A es proporcionada directamente por la presión de suministro.

![Función lógica AND con válvulas](./assets/ValAND.png)
Figura 3. Función lógica AND con válvulas.

La única forma de obtener una salida de presión de aire por la salida A es que ambas señales (Y, y Y2) estén presentes. Ante la ausencia de cualquiera de ellas, no habrá presión por A. También existen válvulas preconstruidas para la función AND.

### Función lógica OR con componentes neumáticos.

En la figura 4 se muestra una forma de construir la función lógica OR con válvulas de dos posiciones, tres vías normalmente cerradas, de accionamiento neumático. 


![Función lógica OR con válvulas](./assets/ValOR.png)
Figura 1.4. Función lógica OR con válvulas.



