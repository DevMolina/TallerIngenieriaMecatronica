


# Guía de Laboratorio 7: Compuertas Lógicas y Circuito de Enclavamiento FluidSim

## Objetivo
Implementar equivalentes a compuertas lógicas y un circuito de enclavamiento utilizando lógica cableada y su respectiva simulación en FluidSIM.

## Actividades

### Prelaboratorio

1. Descargar el software FluidSim [Link de Descarga](https://www.mediafire.com/file/bxmoebrrxp96j2r/Festo_Fluidsim_4.2.rar). Contraseña: xdpluss
2. Repasar conceptos de lógica cableada vistos en clase.
3. Ver vídeo de implementación de equivalencia de compuertas lógicas en FluidSim [Link vídeo](https://www.youtube.com/watch?v=hcwWnzJZdnU)
4. Ver vídeo de enclavamiento eléctrico hasta el minuto 7:05 [Link vídeo](https://www.youtube.com/watch?v=7NiUux0t8eY)
5. Consultar fundamentos de las compuertas NAND, NOR, XOR, XNOR y su equivalente en lógica cableada.
6. Simular en FluidSIM los circuitos equivalentes en lógica cableada para las compuertas AND, OR, NOT, NAND, NOR, XOR y XNOR.
7. Simular en FluidSim el circuito de enclavamiento eléctrico. 


### 1. Implementación de Compuertas Lógicas con Lógica Cableada

De acuerdo a las indicaciones dadas en laboratorio e implementando módulos Festo realizar el montaje y verificación de:

#### Compuerta AND

1. Conectar dos pulsadores normalmente abiertos en serie.
2. Conectar una lámpara en serie con los pulsadores.
3. Alimentar el circuito con 24V DC.
4. Verificar que la lámpara solo se enciende cuando ambos pulsadores están presionados.

#### Compuerta OR
1. Conectar dos pulsadores normalmente abiertos en paralelo.
2. Conectar una lámpara en serie con los pulsadores.
3. Alimentar el circuito con 24V DC.
4. Verificar que la lámpara se enciende si al menos uno de los pulsadores está presionado.

#### Compuerta NOT
1. Utilizar un relé con un contacto normalmente cerrado.
2. Conectar el contacto normalmente cerrado en serie con una lámpara.
3. Alimentar el circuito con 24V DC.
4. Verificar que la lámpara está encendida cuando el relé no está activado y se apaga cuando se activa.

#### Realizar la implementación de las demas compuertas lógicas en su equivalente en lógica cableada. NAND, NOR, XOR y XNOR

### 2. Implementación de Circuito de Enclavamiento
1. Conectar un pulsador normalmente abierto (Start) en serie con la bobina de un relé.
2. Conectar un contacto normalmente abierto del mismo relé en paralelo con el pulsador Start.
3. Conectar un pulsador normalmente cerrado (Stop) en serie con la bobina del relé.
4. Conectar una lámpara en paralelo con la bobina del relé.
5. Alimentar el circuito con 24V DC.
6. Verificar que al presionar Start, la lámpara se enciende y permanece encendida hasta presionar Stop.


## Cuestionario
1. ¿Cuál es la diferencia entre lógica cableada y el uso de compuertas lógicas?
2. ¿Qué aplicaciones tienen los circuitos de enclavamiento en la industria?
3. ¿El comportamiento del circuito simulado es igual al montaje físico?

## Entrega
Subir un informe con:
- Fotos de los montajes físicos.
- Capturas de pantalla de las simulaciones en FluidSIM.
- Respuestas al cuestionario.
- Conclusiones sobre el funcionamiento y diferencias entre la implementación física y la simulación.
