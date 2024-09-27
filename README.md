# CNYT
# operaciones_complex

 Operaciones Complejas

## Descripción
`operaciones_complex` es una librería en Python que permite realizar operaciones con números complejos en sus formas cartesianas y polares. Esta guía ofrece una explicación histórica de los números complejos y detalla las funciones disponibles en la librería.

## Historia de los Números Complejos

Los números complejos surgieron en el siglo XVI como una herramienta para resolver ecuaciones polinómicas que no podían ser resueltas usando números reales. En 1545, el matemático italiano Gerolamo Cardano introdujo la idea de las soluciones a ecuaciones cuadráticas que incluían raíces cuadradas de números negativos, aunque no fue hasta más tarde que estas "cantidades imaginarias" fueron formalmente aceptadas y comprendidas.

El número complejo se define como una combinación de un número real y una cantidad imaginaria, generalmente representado como \( z = a + bi \), donde \( a \) y \( b \) son números reales y \( i \) es la unidad imaginaria, definida como \( i^2 = -1 \). Con el tiempo, los números complejos encontraron aplicaciones en diversas áreas de las matemáticas, la física y la ingeniería, particularmente en el análisis de circuitos eléctricos y en la teoría de señales.

## Funcionalidades de la Librería

La librería `operaciones_complex` proporciona las siguientes funciones para operar con números complejos:

### 1. Suma de Números Complejos: `suma_complex(x, y)`

- **Descripción**: Realiza la suma de dos números complejos representados como listas `[a, b]` donde `a` es la parte real y `b` es la parte imaginaria.
- **Ejemplo**:
  ```python
  x = [3, 2]
  y = [1, 7]
  resultado = suma_complex(x, y)  # Resultado: [4, 9]
  ```

### 2. Resta de Números Complejos: `resta_complex(x, y)`
- **Descripción**: Realiza la resta de dos números complejos representados como listas `[a, b]` donde `a` es la parte real y `b` es la parte imaginaria.
- **Ejemplo**:
   ```python
   x = [3, 2]
   y = [1, 7]
   resultado = resta_complex(x, y)  # Resultado: [2, -5]
   ```

### 3. Producto de Números Complejos: `mult_complex(x, y)`
- ![image](https://github.com/user-attachments/assets/365e37bf-bf54-4291-8e5a-ea13fc4d6ead)

  \[
  (a + bi) 	imes (c + di) = (ac - bd) + (ad + bc)i
  \]

- **Ejemplo**:
  ```python
  x = [3, 2]
  y = [1, 7]
  resultado = mult_complex(x, y)  # Resultado: [-11, 23]
  ```

### 4. División de Números Complejos: `division_complex(x, y)`
-![image](https://github.com/user-attachments/assets/f5c14c7e-a0a5-4e12-8baf-a880b8d46952)

- **Ejemplo**:
  ```python
  x = [3, 2]
  y = [1, 7]
  resultado = division_complex(x, y)  # Resultado: [0.34, -0.38]
  ```

### 5. Conjugado de un Número Complejo: `conjugado_complex(x)`
- ![image](https://github.com/user-attachments/assets/0841a0e1-9441-4f98-8297-34bfc128c5d8)

- **Ejemplo**:
   ```python
   x = [3, 2]
   resultado = conjugado_complex(x)  # Resultado: [3, -2]
   ```

### 6. Módulo de Número Complejo: `modulo_complex(x)`
- ![image](https://github.com/user-attachments/assets/cfa03979-0913-478f-826d-c374df636284)

- **Ejemplo**:
   ```python
   x = [3, 2]
   resultado = modulo_complex(x)  # Resultado: 3.605
   ```

### 7. Conversión de Cartesiano a Polar: `cartesiano_polar(x)`
- ![image](https://github.com/user-attachments/assets/b16d5e94-7002-41fa-8580-5707145cb4f2)

- **Ejemplo**:
  ```python
  x = [3, 2]
  resultado = cartesiano_polar(x)  # Resultado: [3.605, 0.588]

### 8. Conversión de Polar a Cartesiano: `polar_cartesiano(x)`
-![image](https://github.com/user-attachments/assets/0f565e6f-4998-4e17-9e36-2a2d942c0849)
- **Ejemplo**:
  ```python
  x = [3.605, 0.588]
  resultado = polar_cartesiano(x)  # Resultado: [3, 2]

 ### 9. fase de Polar : `fase_complex_polar(x)`
 -![image](https://github.com/user-attachments/assets/48d4df1a-fc96-42fc-94f4-d794975f599d)
 
- **Ejemplo**:
  ```python
  x = [3.605, 0.588]
  resultado = fase_complex_polar(x)  # Resultado: 0.588
  
 ### 10. fase de cartesiano : `fase_complex_cartesiano(x)`
 ![image](https://github.com/user-attachments/assets/5bbb12d8-83f8-4c5b-8a49-ac78ed0d74b4)

 - **Ejemplo**:
  ```python
x = [3, 2]
resultado = fase_complex_cartesiano(x)  # Resultado:  (33.69, 0.588)

# 📊 Experimento de la Doble Rendija - Simulación en Python

Este repositorio implementa y simula el experimento clásico de la **doble rendija**, propuesto por Thomas Young en 1801 para demostrar la naturaleza ondulatoria de la luz. El experimento ilustra cómo la luz puede interferir consigo misma, generando patrones de interferencia que solo pueden explicarse si la luz se comporta como una onda.

## 📚 Explicación Teórica del Experimento

### ¿Qué es el Experimento de la Doble Rendija?
El experimento de la doble rendija consiste en dirigir un haz de luz coherente (como un láser) hacia un material opaco que tiene dos rendijas estrechas y paralelas. Cuando la luz atraviesa las dos rendijas, se difracta y las ondas emergentes interfieren entre sí, formando un patrón de franjas brillantes y oscuras en una pantalla ubicada detrás de las rendijas.

### ¿Por qué Ocurre la Interferencia?
Las ondas de luz provenientes de cada rendija se superponen. Esto significa que, dependiendo de la diferencia de fase entre las ondas (determinado por la distancia recorrida por cada onda desde su rendija hasta un punto en la pantalla), pueden interferir **constructivamente** (cuando las crestas de ambas ondas se suman, generando una franja brillante) o **destructivamente** (cuando una cresta y un valle se cancelan, formando una franja oscura).

El patrón de interferencia observado en la pantalla se puede describir usando la ecuación:

\[
d \cdot \sin \theta = m \cdot \lambda
\]

Donde:

- **d**: Distancia entre las rendijas.
- **θ**: Ángulo de interferencia para cada franja observada.
- **λ**: Longitud de onda de la luz utilizada.
- **m**: Número de orden (m = 0, ±1, ±2, ...).

Las franjas claras corresponden a los máximos de interferencia (m = ±1, ±2...) y las franjas oscuras a los mínimos de interferencia.

### Relevancia del Experimento
El experimento de la doble rendija es crucial en la física porque demuestra la **dualidad onda-partícula** de la luz y ha sido replicado incluso con partículas como electrones, mostrando que no solo las ondas de luz, sino también las partículas, exhiben propiedades ondulatorias bajo ciertas condiciones.

## 🛠️ Simulación en Python

El propósito de este proyecto es simular este patrón de interferencia utilizando `numpy` para los cálculos y `matplotlib` para la visualización. El módulo permite visualizar cómo cambian las franjas de interferencia según se ajusten parámetros como la longitud de onda y la separación de las rendijas.

### 📋 Requisitos del Proyecto

- Python 3.x
- `numpy`
- `matplotlib`

fotos del experimento realizado :
![image](https://github.com/user-attachments/assets/a042c7ab-9eba-4fdb-a58a-b3c3ad1f0e5d)

![image](https://github.com/user-attachments/assets/a1d3378f-3757-4e48-a9f1-79b152b91caf)

### 📋 Patron de interferencia

![20240923_163755](https://github.com/user-attachments/assets/851fff3a-09df-4961-9e7d-9c6d2e877273)



  







