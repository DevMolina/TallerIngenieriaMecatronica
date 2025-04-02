# Examen Parcial

## 1. Si un LED tiene una resistencia serie de 220 Ω y se conecta a una fuente de 9V, asumiendo una caída de voltaje de 2V en el LED, ¿cuál es la corriente que circula por el circuito?  
- [ ] a) 20 mA  
- [ ] b) 25 mA  
- [ ] c) 31.8 mA  
- [ ] d) 10 mA  

<!-- **Cálculo:**  
c) \( I = \frac{V}{R} = \frac{9V - 2V}{220Ω} = \frac{7V}{220Ω} = 31.8mA \)  

--- -->

## 2. Según la Ley de Ohm, si se duplica el voltaje aplicado a una resistencia fija, ¿qué sucede con la corriente que la atraviesa?  
- [ ] a) Se mantiene constante  
- [ ] b) Se duplica  
- [ ] c) Se reduce a la mitad  
- [ ] d) Aumenta de manera exponencial  

<!-- **Explicación:**  
b) \( V = IR \), si \( R \) es constante y \( V \) se duplica, entonces \( I \) también se duplica.   -->

---

## 3. El brillo de un LED aumenta cuando:  
- [ ] a) Se aumenta la resistencia en serie  
- [ ] b) Se disminuye el voltaje aplicado  
- [ ] c) Se aumenta la corriente que pasa por él  
- [ ] d) Se invierte la polaridad del LED  

<!-- **Explicación:**  
c) El brillo del LED depende de la corriente. Más corriente significa más brillo, hasta un límite seguro.   -->

---

## 4. Si un hilo de nicrom inicialmente a temperatura ambiente aumenta su temperatura al pasar corriente, ¿qué efecto tiene esto en su resistencia?  
- [ ] a) Disminuye  
- [ ] b) Aumenta  
- [ ] c) Se mantiene constante  
- [ ] d) Se vuelve cero  

<!-- **Explicación:**  
b) El nicrom es un material con coeficiente de temperatura positivo, lo que significa que su resistencia aumenta con la temperatura.   -->

## 5. En un circuito en paralelo con tres resistencias de 10Ω, 20Ω y 30Ω, ¿cuál es la resistencia equivalente?  
- [ ] a) 60Ω  
- [ ] b) 20Ω  
- [ ] c) 5.45Ω  
- [ ] d) 10Ω  

<!-- **Cálculo:**  
c)
\[
\frac{1}{R_{eq}} = \frac{1}{10} + \frac{1}{20} + \frac{1}{30} = \frac{6}{60} + \frac{3}{60} + \frac{2}{60} = \frac{11}{60}
\]
\[
R_{eq} = \frac{60}{11} ≈ 5.45Ω
\] -->
---
## 6. ¿Cuál de los siguientes factores puede afectar la precisión de las mediciones realizadas con un medidor LCR?  
- [ ] a) Solo la temperatura ambiente.  
- [ ] b) La humedad y la presión atmosférica.  
- [ ] c) La frecuencia de la señal de prueba.  
- [ ] d) Todas las anteriores.  

<!-- **Explicación:**  
d) Todas: Las mediciones con un medidor LCR pueden verse afectadas por la temperatura, la humedad, la presión atmosférica y la frecuencia de la señal de prueba, ya que estos factores pueden influir en las propiedades eléctricas de los componentes medidos. -->

## 7. En un circuito astable con el temporizador 555, ¿cómo afecta un aumento en el valor de la resistencia R2 a la señal de salida?  
- [ ] a) La frecuencia aumenta y el ciclo de trabajo disminuye.  
- [ ] b) La frecuencia disminuye y el ciclo de trabajo aumenta.  
- [ ] c) La frecuencia permanece constante y solo cambia la amplitud de la señal.  
- [ ] d) No tiene efecto en la señal de salida.  

<!-- **Explicación:**  
b) En un circuito astable con 555, la frecuencia de oscilación depende de R1, R2 y el condensador. Un aumento en R2 incrementa el tiempo en alto, reduciendo la frecuencia total. -->

---

## 8. ¿Cuál de las siguientes es una posible causa de discrepancias entre los valores medidos en un osciloscopio y los configurados en un generador de señales?  
- [ ] a) Ruido en el circuito o interferencias electromagnéticas.  
- [ ] b) Impedancia de entrada del osciloscopio.  
- [ ] c) Errores en la calibración del generador o del osciloscopio.  
- [ ] d) Todas las anteriores.  

<!-- **Explicación:**  
d) Factores como ruido eléctrico, diferencias de impedancia y errores de calibración pueden afectar la medición de señales en un osciloscopio. -->

## 9. ¿Por qué es importante usar un diodo flyback cuando se activa un relé?  
- [ ] a) Para aumentar la corriente que circula por la bobina del relé.  
- [ ] b) Para reducir la resistencia interna del relé.  
- [ ] c) Para proteger el transistor de picos de voltaje inducidos al desactivar el relé.  
- [ ] d) Para mejorar la velocidad de conmutación del relé.  

<!-- **Explicación:**  
c) Cuando se desactiva un relé, la energía almacenada en la bobina puede generar un alto voltaje inverso que podría dañar el transistor. El diodo flyback proporciona un camino para disipar esa energía de manera segura.   -->

---

## 10. ¿Cuál es la función del resistor de base en un transistor BJT o de gate en un MOSFET cuando se usa para controlar un relé?  
- [ ] a) Evitar el paso de corriente al transistor.  
- [ ] b) Aumentar la velocidad de conmutación del relé.  
- [ ] c) Limitar la corriente de entrada y proteger el transistor de daños.  
- [ ] d) Reducir el voltaje aplicado al relé.  

<!-- **Explicación:**  
c) El resistor de base en un BJT o de gate en un MOSFET controla la corriente de activación del transistor, evitando daños por sobrecorriente y asegurando un funcionamiento eficiente.   -->

## 11. En un amplificador operacional inversor con una resistencia de retroalimentación de 100 kΩ, ¿qué valor debe tener la resistencia de entrada para obtener una ganancia de 100?  
- [ ] a) 0.1 kΩ  
- [ ] b) 10 kΩ  
- [ ] c) 1 kΩ  
- [ ] d) 100 Ω  

<!-- **Cálculo:**  
c)
La ecuación de ganancia para un amplificador inversor es:  
\[
A_v = -\frac{R_f}{R_{in}}
\]
Dado que \( A_v = -100 \) y \( R_f = 100kΩ \), despejamos \( R_{in} \):  
\[
R_{in} = \frac{R_f}{|A_v|} = \frac{100kΩ}{100} = 1kΩ
\] -->

---

## 12. Un amplificador operacional en modo comparador tiene una referencia de 2V en la entrada inversora y una señal variable en la entrada no inversora. ¿Qué sucede si la señal de entrada no inversora sube de 1V a 3V?  
- [ ] a) La salida se mantiene en 0V.  
- [ ] b) La salida fluctúa entre valores altos y bajos.  
- [ ] c) La salida sigue la señal de entrada.  
- [ ] d) La salida cambia de nivel bajo a nivel alto.  

<!-- **Explicación:**  
d) En modo comparador, si la entrada no inversora supera a la entrada inversora, la salida del OpAmp se satura al voltaje positivo de alimentación (nivel alto). -->


## 13. En un circuito lógico, ¿cuál de las siguientes afirmaciones es correcta respecto a la minimización de funciones booleanas?  
- [ ] a) La minimización de funciones siempre reduce la cantidad de entradas del circuito.  
- [ ] b) La simplificación solo es útil para circuitos combinacionales y no para circuitos secuenciales.  
- [ ] c) La reducción de compuertas mediante minimización siempre mejora la velocidad del circuito.  
- [ ] d) La minimización reduce la cantidad de compuertas, lo que disminuye el costo y el consumo de energía del circuito.  

<!-- **Explicación:**  
d) La minimización de funciones booleanas optimiza el diseño del circuito, reduciendo la cantidad de compuertas necesarias, lo que puede disminuir el costo, el consumo de energía y mejorar la eficiencia del sistema. -->

---

## 14. ¿Cómo se representa la lógica de contactos en comparación con las compuertas lógicas en circuitos digitales?  
- [ ] a) La lógica de contactos es idéntica a un diagrama de compuertas lógicas.  
- [ ] b) La lógica de contactos solo se usa en sistemas electrónicos modernos.  
- [ ] c) La lógica de contactos usa relés y contactos para representar operaciones lógicas como AND, OR y NOT.  
- [ ] d) No existe relación entre la lógica de contactos y las compuertas lógicas.  

<!-- **Explicación:**  
c) La lógica de contactos, utilizada en sistemas eléctricos e industriales, representa funciones lógicas mediante relés y contactos, equivalentes a compuertas AND, OR y NOT en circuitos digitales. -->

## 15. ¿Cuál es la diferencia principal entre la lógica cableada y el uso de compuertas lógicas?  
- [ ] a) La lógica cableada solo se usa en circuitos analógicos, mientras que las compuertas lógicas se usan en digitales.  
- [ ] b) La lógica cableada siempre es más eficiente que las compuertas lógicas.  
- [ ] c) La lógica cableada implementa funciones lógicas directamente con conexiones físicas, mientras que las compuertas lógicas utilizan circuitos integrados.  
- [ ] d) No hay ninguna diferencia significativa entre ambas.  

<!-- **Explicación:**  
c) La lógica cableada implementa funciones lógicas mediante conexiones físicas de componentes sin necesidad de compuertas lógicas. En cambio, las compuertas lógicas realizan las mismas funciones internamente mediante circuitos integrados, facilitando el diseño y modificación de circuitos. -->

---

## 16. ¿Por qué los circuitos de enclavamiento son fundamentales en aplicaciones industriales?  
- [ ] a) Porque permiten reducir el consumo de energía en sistemas digitales.  
- [ ] b) Porque eliminan la necesidad de sensores en procesos automatizados.  
- [ ] c) Porque garantizan que un sistema se mantenga en un estado seguro hasta que una condición específica lo cambie.  
- [ ] d) Porque aumentan la velocidad de respuesta de los sistemas de control.  

<!-- **Explicación:**  
c) Los circuitos de enclavamiento se usan en la industria para mantener un sistema en un estado específico, como en controles de seguridad y procesos automatizados, hasta que una condición determinada permita el cambio de estado. -->

## 17. Pérdida de potencia en una línea de transmisión  
Una línea de alta tensión de **15 km** transporta una corriente de **1.2 kA** a **500 kV**. La resistencia total del cable es de **8.5 mΩ/km**.  

¿Cuánta potencia se pierde en la línea de transmisión?.  

- [ ] a) 21.5 MW  
- [ ] b) 18.36 kW  
- [ ] c) 18.36 MW  
- [ ] d) 21.5 kW  

<!-- **Explicación:**  
c) La potencia disipada por efecto Joule en la línea se calcula con la ecuación:  

\[
P_{\text{pérdida}} = I^2 R
\]

Donde:  
- \( I = 1.2 \) kA = **1200 A**  
- \( R = (8.5 \text{ mΩ/km}) \times (15 \text{ km}) = 0.1275 \ Ω \)  

\[
P_{\text{pérdida}} = (1200)^2 \times 0.1275 = 18.36 \text{ MW}
\]   -->

---

## 18. Consumo de una fábrica  
Una fábrica opera con un suministro de **13.8 kV** y consume una potencia de **1.2 MW**.  ¿Cuál es la corriente consumida?   Si la fábrica opera 24/7 durante un mes, ¿cuánta energía consumió?  

- [ ] a) 87 A, 0.864 GWh
- [ ] b) 92 A, 0.954 GWh  
- [ ] c) 100 A, 1.002 GWh  
- [ ] d) 80 A, 0.754 GWh  

<!-- **Explicación:**  
a) La corriente se calcula con:  

\[
I = \frac{P}{V}
\]

\[
I = \frac{1.2 \times 10^6}{13.8 \times 10^3} = 87 \text{ A}
\]

La energía consumida en un mes es:  

\[
E = P \times t = (1.2 \text{ MW}) \times (24 \times 30)
\]

\[
E = 0.864 \text{ GWh}
\] -->

---

## 19. Comparación de caída de voltaje en cables de cobre y aluminio  
Se necesita transportar **250 A** a lo largo de **500 m** en una planta industrial. Se comparan dos tipos de cables:  

- **Cobre:** resistencia de **0.017 Ω/km**  
- **Aluminio:** resistencia de **0.028 Ω/km**  

¿Cuál será la caída de voltaje en cada caso?  

- [ ] a) Cobre: 2.12 V, Aluminio: 3.5 V
- [ ] b) Cobre: 3.5 V, Aluminio: 4.8 V  
- [ ] c) Cobre: 1.5 V, Aluminio: 2.9 V  
- [ ] d) Cobre: 4.2 V, Aluminio: 6.1 V  

<!-- **Explicación:**  
a) La caída de voltaje en un conductor se calcula con:  

\[
V = I \times R
\]

Para cobre:  

\[
R_{\text{cobre}} = (0.017 \text{ Ω/km}) \times (1 \text{ km}) = 0.017 Ω
\]

\[
V_{\text{cobre}} = 250 \times 0.017 = 2.12 V
\]

Para aluminio:  

\[
R_{\text{aluminio}} = (0.028 \text{ Ω/km}) \times (1 \text{ km}) = 0.028 Ω
\]

\[
V_{\text{aluminio}} = 250 \times 0.028 = 3.5 V 
\]-->


---

## 20. Efecto de una resistencia de carga en un divisor de voltaje  
Se tiene un divisor de voltaje con **R1 = 1 kΩ** y **R2 = 2 kΩ** conectado a **12V**. Si se conecta una resistencia de carga **RL = 2 kΩ** en paralelo con R2, ¿cómo cambia el voltaje en la salida?  

- [ ] a) Disminuye  
- [ ] b) Aumenta  
- [ ] c) No cambia  
- [ ] d) Depende de la corriente  

<!-- **Explicación:**  
a)
Sin carga:  

\[
V_{\text{out}} = 12V \times \frac{2kΩ}{1kΩ + 2kΩ} = 8V
\]

Con carga:  

\[
R_{\text{eq}} = \frac{(2kΩ \times 2kΩ)}{(2kΩ + 2kΩ)} = 1kΩ
\]

\[
V_{\text{out}} = 12V \times \frac{1kΩ}{1kΩ + 1kΩ} = 6V
\]

Disminuye debido al cambio en la resistencia equivalente.   -->

---