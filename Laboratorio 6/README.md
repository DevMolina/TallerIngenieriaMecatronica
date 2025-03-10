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
1. Diseñe un circuito de encendido de motor que funcione bajo las siguientes condiciones:
   - Entrada A: Llave de encendido girada.
   - Entrada B: Sensor de embrague o freno presionado.
   - Entrada C: Batería con carga suficiente.
   - Salida F: Motor arranca si A y B están activos y la batería (C) tiene carga.
2. Obtenga la expresión booleana correspondiente y represéntela con compuertas lógicas.
3. Dibuje el diagrama de conexiones o realice la simulacion usando TinkerCAD.
4. Dibuje el circuto equivalente en lógica de contactos.
3. Implemente el circuito en el protoboard.


### **6. Problema Aplicado: Control de nivel de tanques de almacenamiento de agua**
1. Diseñe un sistema de control de una bomba para el llenado de un tanque con las siguientes condiciones:
   - Se dispone de dos tanques de agua, el primero es un tanque subterraneo (Tanque A) de 5000L con disponibilidad de una bomba para conducirla a un tanque elevado (Tanque B) de 1000L, cada tanque cuenta con un sensor tipo flotador que permite obtener una el estado del nivel
   - Detector de nivel Tanque A. Nivel de agua bajo = 0.
   - Detector de nivel Tanque B. Nivel de agua bajo = 0.
   - Entrada C: Botón de encendido de la bomba modo manual.
   - Salida bomba: Mediante un led simule la activación o inactivación del motor de la bomba. La bomba se debe activar cuando el Tanque A se encuentre con nivel bajo de agua y en el Tanque A nivel alto. Con la Entrada C el usuario puede activar la bomba manualmente siempre y cuando el Tanque A tenga nivel de agua alto.
   - Salida indicador emergencia. Se debe activar un indicador (Led) que indique al usuario cuando los dos tanques tengan nivel de agua bajo.
2. Obtenga la expresión booleana y represéntela con compuertas lógicas.
3. Obtenga el diagrama de conexiones empleando TinkerCAD.
4. Dibuje el diagrama de contactos equivalente.
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