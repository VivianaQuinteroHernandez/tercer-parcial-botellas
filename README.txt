## Optimizando la ecuación del calor con Cython

### Creating a Cython extension

Escribe un `setup.py` para crear una version de Cython del modulo [heat.py](heat.py), 
y usarlo desde el programa principal [heat_main.py](heat_main.py). 
¿Cúanto hace la simple Citonizacion mejorar el rendimiento?\

### Optimizando

Basado en el perfil de la medicion del rendimiento
[ejercicio](../../rendimiento/perfil) optimizan la parte del algoritmo que más tiempo consume. 

Utiliza todos los trucos que has aprendido hasta ahora (escribe las declaraciones,
...indexacion rapida, directivas del compilador, funciones C, ...).

Haga una tabla comparativa de rendimiento junto con el SpeedUp.
