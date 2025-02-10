# Circuito Eléctrico con Ecuaciones

## Descripción del Circuito

Se considera un circuito con una fuente de voltaje \( V \), una resistencia \( R \) y una bobina de inductancia \( L \), conectadas en serie. El comportamiento del circuito está gobernado por la siguiente ecuación diferencial:

$$
V = L \frac{dI}{dt} + RI
$$

## Diagrama del Circuito

     +----R----L----+
     |             |
     V             |
     |             |
     +-------------+


## Resolviendo la Ecuación

La ecuación diferencial puede resolverse asumiendo condiciones iniciales. La solución general para la corriente \( I(t) \) en el circuito es:

$$
I(t) = \frac{V}{R} \left( 1 - e^{-\frac{R}{L}t} \right)
$$

## Interpretación

- Cuando \( t = 0 \), la corriente es cero.
- A medida que el tiempo avanza, la corriente tiende a \( $$\frac{V}{R}$$ \).
- La constante de tiempo del circuito está dada por \( \tau = \frac{L}{R} \), indicando la rapidez con la que el circuito alcanza su estado estable.

Este circuito representa un sistema RL típico y su análisis es útil en aplicaciones de electrónica y control de sistemas eléctricos.
