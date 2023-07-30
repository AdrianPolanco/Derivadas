import tkinter as tk
from sympy import Derivative, diff, symbols, simplify, latex
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calcular_derivada():
    termino = entrada_derivada.get()
    x = symbols('x')
    derivada = Derivative(termino, x).doit()
    resultado = f"d/dx ({termino}) = {simplify(derivada)}"
    etiqueta_resultado.config(text=resultado)

    # Mostrar la derivada en un gráfico matplotlib
    plt.figure(figsize=(5, 3))
    plt.text(0.1, 0.5, f"$d/dx ({termino})$", fontsize=16, usetex=True)
    plt.axis('off')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Calculadora de Derivadas')

# Etiqueta y entrada para ingresar las derivadas
etiqueta_derivada = tk.Label(ventana, text='Ingresa la derivada:')
etiqueta_derivada.pack()
entrada_derivada = tk.Entry(ventana)
entrada_derivada.pack()

# Botón para calcular la derivada
boton_calcular = tk.Button(ventana, text='Calcular', command=calcular_derivada)
boton_calcular.pack()

# Marco para mostrar el gráfico matplotlib
frame_grafico = tk.Frame(ventana)
frame_grafico.pack()

# Etiqueta para mostrar el resultado en formato LaTeX
etiqueta_resultado = tk.Label(
    ventana, justify="left", font=("Times", 14), anchor="w")
etiqueta_resultado.pack()

# Bucle principal de la aplicación
ventana.mainloop()
