import tkinter as tk
from tkinter import messagebox
import math

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self, lado1, lado2):
        # Utilizamos el teorema de Pitágoras para calcular el lado restante
        lado3 = math.sqrt(lado1**2 + lado2**2)
        return self.base + lado1 + lado2

    def dibujar(self, canvas):
        # Dibujar un triángulo
        canvas.create_polygon(100, 100, 
                              100 + self.base, 100, 
                              100 + (self.base / 2), 100 - self.altura, 
                              outline='black', fill='lightblue')

class App:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Triángulo")

        self.base_label = tk.Label(master, text="Base:")
        self.base_label.pack()
        self.base_entry = tk.Entry(master)
        self.base_entry.pack()

        self.altura_label = tk.Label(master, text="Altura:")
        self.altura_label.pack()
        self.altura_entry = tk.Entry(master)
        self.altura_entry.pack()

        self.lado1_label = tk.Label(master, text="Lado 1:")
        self.lado1_label.pack()
        self.lado1_entry = tk.Entry(master)
        self.lado1_entry.pack()

        self.lado2_label = tk.Label(master, text="Lado 2:")
        self.lado2_label.pack()
        self.lado2_entry = tk.Entry(master)
        self.lado2_entry.pack()

        self.calcular_button = tk.Button(master, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

    def calcular(self):
        base = float(self.base_entry.get())
        altura = float(self.altura_entry.get())
        lado1 = float(self.lado1_entry.get())
        lado2 = float(self.lado2_entry.get())

        triangulo = Triangulo(base, altura)

        area = triangulo.calcular_area()
        perimetro = triangulo.calcular_perimetro(lado1, lado2)

        messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")
        self.canvas.delete("all")  # Limpiar el lienzo antes de dibujar
        triangulo.dibujar(self.canvas)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
