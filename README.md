# CNYT
# operaciones_complex

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

### 2. Resta de Números Complejos: `resta_complex(x, y)`
- **Descripción**: Realiza la resta de dos números complejos representados como listas `[a, b]` donde `a` es la parte real y `b` es la parte imaginaria.
- **Ejemplo**:
   ```python
   x = [3, 2]
  y = [1, 7]
  resultado = resta_complex(x, y)  # Resultado: [2, -5]

### 3. Producto de Números Complejos: `mult_complex(x, y)`
- **Descripción**:Multiplica dos números complejos utilizando la fórmula:

  \[
  (a + bi) \times (c + di) = (ac - bd) + (ad + bc)i
  \]

  Donde \(a + bi\) y \(c + di\) son los números complejos a multiplicar. El resultado es otro número complejo cuya parte real es \(ac - bd\) y cuya parte imaginaria es \(ad + bc\).
- **Ejemplo**:
  ```python
  x = [3, 2]
  y = [1, 7]
  resultado = mult_complex(x, y)  # Resultado: [-11, 23]

### 4. Division de Números Complejos: `division_complex(x, y)`
- **Descripción**:  Divide dos números complejos usando la fórmula:

  \[
  \frac{a + bi}{c + di} = \frac{(a + bi) \times (c - di)}{(c + di) \times (c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
  \]

  Donde \(a + bi\) y \(c + di\) son los números complejos a dividir, y \(c - di\) es el conjugado del denominador.
- **Ejemplo**:
  ```python
  x = [3, 2]
  y = [1, 7]
  resultado = division_complex(x, y)  # Resultado: [0.34, -0.38]

### 5. Conjugado de un  Número Complejo: `conjugado_complex(x, y)`
- **Descripción**:Calcula el conjugado de un número complejo. El conjugado de un número complejo \(a + bi\) se obtiene cambiando el signo de la parte imaginaria, resultando en \(a - bi\).

  \[
  \text{Conjugado}(a + bi) = a - bi
  \]
- **Ejemplo**:
   ```python
   x = [3, 2]
  resultado = conjugado_complex(x)  # Resultado: [3, -2]
   
### 6. Modulo de Número Complejo: `conjugado_complex(x, y)`
- **Descripción**:Calcula el módulo o magnitud de un número complejo, usando la fórmula: |z| = \(\sqrt{a^2 + b^2}\)
- **Ejemplo**:
   ```python
   x = [3, 2]
  resultado = modulo_complex(x)  # Resultado: 3.605
  ### Conversión de Cartesiano a Polar: `cartesiano_polar(x)`

-### 7.Conversión de Cartesiano a Polar: `cartesiano_polar(x)`
- **Descripción**: Convierte un número complejo de su forma cartesiana \(a + bi\) a su forma polar \(r \angle \theta\). La magnitud \(r\) y el ángulo \(\theta\) se calculan utilizando las siguientes fórmulas:

  \[
  r = \sqrt{a^2 + b^2}
  \]
  \[
  \theta = \tan^{-1}\left(\frac{b}{a}\right)
  \]

  Donde \(r\) es la magnitud del número complejo y \(\theta\) es el ángulo en radianes.

- **Ejemplo**:
  ```python
  x = [3, 2]
  resultado = cartesiano_polar(x)  # Resultado: [3.605, 0.588]

  







