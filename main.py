import tkinter as tk
from sympy import Derivative, symbols, simplify


def format_derivada(termino, derivada):
    # Formatear la derivada en el formato solicitado
    x = symbols('x')
    derivada_str = str(simplify(derivada))
    derivada_str = derivada_str.replace("**", "^")
    derivada_str = derivada_str.replace("*", "")
    termino_str = str(simplify(termino))
    termino_str = termino_str.replace("**", "^")
    termino_str = termino_str.replace("*", "")
    return f"d/dx ({termino_str}) = {derivada_str}"


def calcular_derivada():
    termino = entrada_derivada.get()
    x = symbols('x')
    derivada = Derivative(termino, x).doit()
    resultado = format_derivada(termino, derivada)
    etiqueta_resultado.config(text=resultado)


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

# Etiqueta para mostrar el resultado en formato deseado
etiqueta_resultado = tk.Label(
    ventana, justify="left", font=("Times", 14))
etiqueta_resultado.pack()

# Bucle principal de la aplicación
ventana.mainloop()
