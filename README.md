# Guía de Laboratorio 1: Variables Fundamentales Electrónica

**Yeison Daniel Molina Monsalve**  
**February 10, 2025**  

## 1. Objetivos

- Medir voltaje, corriente y resistencia en un circuito con LED.
- Verificar experimentalmente la Ley de Ohm.
- Observar cómo varía el brillo del LED con cambios en la corriente.
- Analizar la disipación de potencia en un hilo de nicrom mediante la Ley de Joule.
- Comprender el uso del multímetro y el protoboard en mediciones eléctricas.

## 2. Prelaboratorio

Antes de realizar este laboratorio, el estudiante debe estudiar los siguientes conceptos:

- **Carga eléctrica**: $Q = I \cdot t$
- **Ley de Ohm**: $V = I \cdot R$
- **Ley de Joule**: $P = I^2 \cdot R$
- **Resistencia de un conductor**: $R = \frac{\rho L}{A}$
- **Uso del multímetro** para medir resistencia, voltaje y corriente.
- **Uso del protoboard** para el armado de circuitos eléctricos.

## Problemas

### Problema 1: Resistencia de un filamento

Un filamento de una bombilla tiene una resistencia de $2.2\Omega$ cuando está frío, pero cuando se calienta su resistencia aumenta a $330\Omega$. Si la bombilla está conectada a una batería de $12V$, ¿cuál es la corriente en el filamento en ambos estados? Exprese los resultados en miliamperios (mA).

### Problema 2: Resistencia de un cable largo

Un cable de cobre de $100m$ tiene una resistencia de $8.5m\Omega$ por metro. Si se usa este cable para transmitir una corriente de $15A$, ¿cuál es la caída de tensión total en el cable? Exprese la respuesta en voltios (V) y en milivoltios (mV).

### Problema 3: Energía consumida por un circuito

Un motor eléctrico de $50W$ funciona con una batería de $24V$. ¿Cuál es la corriente que consume el motor? ¿Cuánta energía en joules consume en una hora de funcionamiento? Expresa los resultados en amperios (A), miliamperios (mA) y kilojoules (kJ).

### Problema 4: Potencia en un resistor desconocido

Se tiene un resistor desconocido conectado a una fuente de $15V$. Se mide una corriente de $2mA$. ¿Cuál es el valor de la resistencia? ¿Cuánta potencia disipa el resistor? Expresa los resultados en kiloohmios ($k\Omega$) y microwatts ($\mu W$).

### Entrega
Cada respuesta debe incluir el análisis del problema, las ecuaciones utilizadas y los cálculos detallados con unidades en notación de ingeniería.

## 3. Lista de Materiales

| Cantidad | Material |
|----------|----------|
| 1 | Resistencias de $1k\Omega$ |
| 1 | Resistencia de $470\Omega$ |
| 1 | LEDs de diferentes colores |
| 1 | Protoboard |
| 4 | Cables para protoboard |
| 1 | Hilo de nicrom (30 cm) |
| 1 | Pinzas |

## 4. Procedimiento

### Fundamento Teórico

Un circuito en serie con un LED y una resistencia permite limitar la corriente que pasa a través del LED para evitar daños. La Ley de Ohm se expresa como:

$$V = I \cdot R$$

La tolerancia de la resistencia se calcula comparando el valor medido con el valor nominal usando la ecuación:

$$\text{Tolerancia} = \left( \frac{|R_{medido} - R_{nominal}|}{R_{nominal}} \right) \times 100\%$$

### Procedimiento Experimental

**Medición de la resistencia**
1. Medir el valor real de cada resistencia con el multímetro.
2. Registrar el valor obtenido.

**Medición de voltaje y corriente en el circuito**
1. Conectar la resistencia y el LED en serie sobre la protoboard.
2. Conectar la fuente de alimentación a $5V$.
3. Medir y registrar la caída de voltaje en la resistencia y en el LED.
4. Medir y registrar la corriente en el circuito.
5. Repetir las mediciones aumentando el voltaje de la fuente a $7V$, $9V$ y $12V$.
6. Observar y describir el cambio en el brillo del LED.

## 5. Preguntas para el Informe

1. ¿Cómo afecta el cambio de voltaje al brillo del LED?
2. ¿Coinciden los valores experimentales con la Ley de Ohm?
3. ¿Cuál es la relación entre el voltaje y la corriente en el LED?
4. ¿Cómo varió la temperatura del hilo de nicrom con el tiempo?
5. ¿Cómo se comparan la potencia calculada y la observada mediante el cambio de temperatura?

## 6. Consultas Adicionales

- Explica el concepto de culombio ($C$) en relación con la cantidad de carga transportada.
- Relaciona la Ley de Joule con el uso de resistencias en electrodomésticos.
- Compara el comportamiento del hilo de nicrom con una resistencia convencional.
- Investiga el uso del multímetro en la medición de resistencia, voltaje y corriente.
- Explica el funcionamiento del protoboard y cómo facilita el montaje de circuitos.

graph TD;
    A[Fuente de alimentación] -->|5V| B[Resistencia 1kΩ];
    B --> C[LED];
    C --> D[Tierra];


## Tablas de Referencia

### Prefijos de Ingeniería

| Prefijo | Símbolo | Factor |
|---------|---------|--------|
| Kilo | k | $10^3$ |
| Mili | m | $10^{-3}$ |
| Micro | $\mu$ | $10^{-6}$ |
| Nano | n | $10^{-9}$ |

### Código de Colores de Resistencias

| Color | 1ª Banda | 2ª Banda | Multiplicador | Tolerancia |
|-------|---------|---------|--------------|------------|
| Rojo  | 2       | 2       | $10^2$       | ±2%        |
| Azul  | 6       | 6       | $10^6$       | ±0.25%     |

### Características de LEDs

| Color | Material | Voltaje de Caída (V) |
|-------|---------|------------------|
| Rojo  | AlGaInP | 1.8 - 2.2        |
| Azul  | GaN     | 3.0 - 3.5        |
