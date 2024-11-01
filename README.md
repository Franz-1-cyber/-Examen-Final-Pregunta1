# Calculadora de Triángulo

Este proyecto es una calculadora de triángulos que permite calcular el área y el perímetro de un triángulo dado su base, altura y dos lados. Además, visualiza el triángulo en una interfaz gráfica utilizando Tkinter.

## Requisitos

- Python 3.x
- Tkinter (incluido en las instalaciones estándar de Python)

## Cómo usar

1. **Ejecuta el programa**:
   Asegúrate de tener Python instalado en tu sistema. Luego, ejecuta el archivo de Python.

   ```bash
   python nombre_del_archivo.py
Ingresa los valores:

Base: Introduce la longitud de la base del triángulo.
Altura: Introduce la altura del triángulo.
Lado 1: Introduce la longitud del primer lado.
Lado 2: Introduce la longitud del segundo lado.
Calcular: Haz clic en el botón "Calcular" para obtener el área y el perímetro del triángulo. Los resultados se mostrarán en una ventana emergente y el triángulo se dibujará en el lienzo.

Clases
Triangulo: Clase que representa un triángulo. Tiene métodos para calcular el área, el perímetro y dibujar el triángulo.

__init__(base, altura): Inicializa un triángulo con base y altura.
calcular_area(): Calcula el área del triángulo.
calcular_perimetro(lado1, lado2): Calcula el perímetro del triángulo utilizando el teorema de Pitágoras.
dibujar(canvas): Dibuja el triángulo en el lienzo proporcionado.
App: Clase que maneja la interfaz gráfica.

__init__(master): Inicializa la ventana y los elementos de la interfaz.
calcular(): Método que se llama al presionar el botón "Calcular". Calcula el área y el perímetro y muestra los resultados.
Ejemplo de uso
Supongamos que deseas calcular el área y el perímetro de un triángulo con las siguientes medidas:

Base: 10
Altura: 5
Lado 1: 7
Lado 2: 8
Pasos:
Ejecuta el programa:

bash
Copiar código
python nombre_del_archivo.py
En la interfaz gráfica, ingresa los valores:

Base: 10
Altura: 5
Lado 1: 7
Lado 2: 8
