# Guía de Laboratorio 2: Leyes de Kirchhoff, Cálculo de Potencia y Componentes Equivalentes

## Objetivos
- **General**: Aplicar las leyes de Kirchhoff para analizar circuitos eléctricos en serie y paralelo con dos bombillos de diferente potencia nominal.
- **Específicos**:
  1. Verificar la ley de voltajes de Kirchhoff (LVK) y la ley de corrientes de Kirchhoff (LCK) en circuitos eléctricos.
  2. Calcular la potencia consumida por los bombillos en un circuito serie y paralelo.
  3. Determinar la resistencia, capacitancia e inductancia equivalentes de circuitos en serie y paralelo.
  4. Usar un medidor LCR para medir la inductancia, capacitancia y resistencia de los componentes.

## Prelaboratorio

### Preguntas y Consultas:
1. ¿Qué son las leyes de Kirchhoff y cómo se aplican en los circuitos eléctricos?
2. ¿Cuál es la diferencia entre un circuito en serie y un circuito en paralelo?
3. ¿Cómo se calcula la potencia en un circuito eléctrico?
4. ¿Cómo se determina la resistencia equivalente en un circuito en paralelo?
5. ¿Cómo se determinan la capacitancia e inductancia equivalentes en circuitos de componentes en paralelo y en serie?
6. ¿Cuál es el principio de funcionamiento de un medidor LCR y cómo se utiliza?

## Lista de Materiales
- 2 bombillos DC de diferente potencia nominal (por ejemplo, 10 W y 20 W) o diferente color (ejemplo [Bombillo](https://ferretronica.com/products/bombillo-candelabro-120v-ac-verde-rosca-e12?_pos=6&_sid=4f9831ce0&_ss=r)).
- Roseta plastica. Ejemplo:[Roseta](https://ferretronica.com/products/roseta-plastica-de-rosca-e12-para-bombillo-candelabro?_pos=2&_sid=4f9831ce0&_ss=r)
- Condensador electrolitico de 100 µF y 470 µF.
- Bobina Axial Tipo Resistencia 33uH - 1/4W
- Bobina Axial Tipo Resistencia 22uH - 1/4W
- 2 metros Cable duplex calibre 22.
- 1 clavija macho.
- Protoboard.
- Pinzas.
- Destornillador.
- Cinta aislante.

## Fundamento Teórico

### Leyes de Kirchhoff
- **Ley de Corrientes de Kirchhoff (LCK)**: La suma algebraica de todas las corrientes que entran y salen de un nodo es igual a cero.
  
  \[
  \sum I_{\text{entrantes}} = \sum I_{\text{salientes}}
  \]

- **Ley de Voltajes de Kirchhoff (LVK)**: La suma algebraica de las diferencias de potencial en un lazo cerrado es igual a cero.

  \[
  \sum V_{\text{fuentes}} = \sum V_{\text{caídas}}
  \]

### Potencia en Circuitos Eléctricos
La potencia se calcula con la fórmula:

\[
P = V \times I
\]

donde \(V\) es el voltaje y \(I\) la corriente. La potencia también puede calcularse con:

\[
P = I^2 R = \frac{V^2}{R}
\]

### Resistencia Equivalente
- En **circuitos en serie**, la resistencia equivalente es la suma de las resistencias:

\[
R_{\text{eq}} = R_1 + R_2 + \cdots + R_n
\]

- En **circuitos en paralelo**, la resistencia equivalente se calcula como:

\[
\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_n}
\]

### Capacitancia e Inductancia Equivalentes
- **Capacitancia en paralelo**: La capacitancia equivalente es la suma de las capacitancias:

\[
C_{\text{eq}} = C_1 + C_2 + \cdots + C_n
\]

- **Capacitancia en serie**: La capacitancia equivalente se calcula como:

\[
\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots + \frac{1}{C_n}
\]

- **Inductancia en paralelo**: La inductancia equivalente es:

\[
\frac{1}{L_{\text{eq}}} = \frac{1}{L_1} + \frac{1}{L_2} + \cdots + \frac{1}{L_n}
\]

- **Inductancia en serie**: La inductancia equivalente es la suma de las inductancias:

\[
L_{\text{eq}} = L_1 + L_2 + \cdots + L_n
\]

## Procedimiento

1. **Montaje del Circuito Serie**:
   - Conecta los dos bombillos en serie.
   - Mide el voltaje total aplicado y la corriente utilizando el multímetro.
   - Calcula la potencia de cada bombillo utilizando \(P = V \times I\).

2. **Montaje del Circuito Paralelo**:
   - Conecta los dos bombillos en paralelo con la misma fuente de alimentación.
   - Mide el voltaje en cada bombillo y la corriente en el circuito.
   - Calcula la potencia de cada bombillo de manera individual y la potencia total.

3. **Medición de Resistencia Equivalente**:
   - En el circuito en serie, calcula la resistencia total utilizando la fórmula correspondiente.
   - Repite lo mismo para el circuito en paralelo.

4. **Medición de Capacitancia e Inductancia Equivalentes**:
   - Conecta un condensador y un inductor en serie y en paralelo.
   - Mide la capacitancia e inductancia utilizando el medidor LCR.
   - Calcula los valores equivalentes en ambos casos.

## Tablas de Registro de Datos

### Tabla 1: Datos del Circuito Serie

| Bombillo  | Potencia Nominal (W) | Voltaje (V) | Corriente (A) | Potencia Medida (W) |
|-----------|----------------------|-------------|---------------|---------------------|
| Bombillo 1| 10                   |             |               |                     |
| Bombillo 2| 20                   |             |               |                     |
| Total     |                      |             |               |                     |

### Tabla 2: Datos del Circuito Paralelo

| Bombillo  | Potencia Nominal (W) | Voltaje (V) | Corriente (A) | Potencia Medida (W) |
|-----------|----------------------|-------------|---------------|---------------------|
| Bombillo 1| 10                   |             |               |                     |
| Bombillo 2| 20                   |             |               |                     |
| Total     |                      |             |               |                     |

### Tabla 3: Medición de Resistencia, Capacitancia e Inductancia

| Componente | Tipo       | Valor Medido | Valor Calculado |
|------------|------------|--------------|-----------------|
| Resistor   | Resistencia |              |                 |
| Condensador| Capacitancia|              |                 |
| Inductor   | Inductancia |              |                 |

## Preguntas para Informe

1. ¿Cómo verificaste experimentalmente las leyes de Kirchhoff en este laboratorio?
2. ¿Cuál fue la diferencia en la potencia medida para los bombillos en los circuitos en serie y paralelo? Explique el motivo de esta diferencia.
3. ¿Cómo afectaron la resistencia, la capacitancia y la inductancia equivalentes a las mediciones en los circuitos de prueba?
4. ¿Qué factores pueden influir en la exactitud de las mediciones realizadas con el medidor LCR?
5. ¿Qué observaste al comparar las mediciones experimentales con los cálculos teóricos?

