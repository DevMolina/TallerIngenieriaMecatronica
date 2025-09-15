# Guía de Laboratorio 6: Diseño de Circuitos Combinacionales

## Objetivo
- Comprender el funcionamiento de las compuertas lógicas AND, OR y NOT.
- Implementar circuitos combinacionales utilizando compuertas lógicas y lógica de contactos.
- Aplicar los conceptos a problemas prácticos relacionados con sistemas de control en vehículos e industria.

## Materiales
- Protoboard
- Compuertas lógicas AND, OR y NOT (Circuitos Integrados 7404, 7408, 7432)
- DIP Switch de 4 posiciones
- Fuente de alimentación (5V DC)
- Resistencias (220Ω, 1kΩ)
- LEDs 
- Cables de conexión

## Prelaboratorio

1. Construya la tabla de verdad para las compuertas AND, OR y NOT.
2. Identifique su equivalencia en lógica de contactos.
3. Dibuje los circuitos lógicos para cada compuerta.
4. Elaborar la tabla de verdad para cada una de las compuertas mencionadas.

## 4. Teoría
Las compuertas lógicas son dispositivos electrónicos que operan sobre señales digitales y permiten realizar operaciones lógicas fundamentales. Se clasifican en:

- **Compuerta AND**: La salida es 1 solo si ambas entradas son 1.
- **Compuerta OR**: La salida es 1 si al menos una de las entradas es 1.
- **Compuerta NOT**: Invierte el estado de la señal de entrada.
- **Compuerta XOR**: La salida es 1 si las entradas son diferentes.
- **Compuerta NAND**: La salida es la negación de la compuerta AND.
- **Compuerta NOR**: La salida es la negación de la compuerta OR.

Los circuitos combinacionales se diseñan a partir de estas compuertas y dependen únicamente de las entradas presentes en un instante determinado.

### Procedimiento 

**1. Implementación en Hardware**
1. Arme los circuitos en el protoboard utilizando compuertas lógicas NOT, AND y OR.
2. Verifique su funcionamiento activando distintas combinaciones de entradas.
3. Registre los valores de entrada y salida.

**2. Problema Aplicado: Sistema de Encendido en un Vehículo**
1. Diseñe un circuito lógico para un automóvil moderno, el sistema de encendido del motor (S) depende de cuatro condiciones:

- A = Llave de encendido girada (1 = sí, 0 = no).
- B = Botón de encendido presionado (1 = sí, 0 = no).
- C = Sensor de seguridad (1 = detecta falla, 0 = todo correcto).
- D = Estado de la puerta (1 = puerta abierta, 0 = cerrada).

El motor debe encenderse (S = 1) cuando se cumpla lo siguiente:

- El motor puede arrancar si el conductor gira la llave (A) O presiona el botón (B).
- No debe haber fallas de seguridad → es decir, $\overline{C}$
- La puerta debe estar cerrada → es decir, $\overline{D}$

2. Obtenga la expresión booleana correspondiente y represéntela con compuertas lógicas.
3. Dibuje el diagrama de conexiones o realice la simulacion usando TinkerCAD.
4. Dibuje el circuto equivalente en lógica de contactos.
3. Implemente el circuito en el protoboard.

##### NOTA: puede hacer uso del [Simplificador mapa K Online](http://www.32x8.com/index.html)

## Cuestionario
1. ¿Cuál es la función de cada compuerta lógica utilizada?
2. ¿Cómo se representa la lógica de contactos en comparación con las compuertas lógicas?
3. Explique cómo la minimización de funciones puede optimizar un circuito.
4. ¿Cuál es la diferencia entre un circuito combinacional y un circuito secuencial?
5. ¿Cómo afecta el uso de diferentes compuertas en el diseño de un circuito lógico?
6. ¿Cómo se puede reducir el número de compuertas en un diseño lógico sin alterar su funcionamiento?
7. ¿Qué aplicaciones prácticas tienen los circuitos combinacionales en la vida real?

---