import tkinter as tk
from sympy import Derivative, symbols, simplify, pretty, diff


def format_derivada(termino, derivada):
    # Formatear la derivada en el formato solicitado
    x = symbols('x')
    derivada_str = str(simplify(derivada)).replace('**0', '°').replace('**1', '').replace('**2', '²').replace('**3', '³').replace('**4', '⁴').replace('**5', '⁵').replace('**6', '⁶').replace('**7', '⁷').replace('**8', '⁸').replace('**9', '⁹').replace('*', '')
    termino_str = termino
    return f"d/dx ({pretty(termino_str).replace('**0', '°').replace('**1', '').replace('**2', '²').replace('**3', '³').replace('**4', '⁴').replace('**5', '⁵').replace('**6', '⁶').replace('**7', '⁷').replace('**8', '⁸').replace('**9', '⁹').replace('*', '')}) = {pretty(derivada_str)}"

def calcular_derivada():
    termino = entrada_derivada.get()
    
    # Reemplazar ** por ^ y ajustar notación de multiplicación
    x = symbols('x')
    derivada = diff(termino, x)
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
