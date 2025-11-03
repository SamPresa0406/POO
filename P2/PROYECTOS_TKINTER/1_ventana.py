"""
    Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones 
    en python para escritorio.

"""

from tkinter import *
# import tkinter as tk
# ventana=tk.Tk()

ventana=Tk()
ventana.title("Mi primer ventana con Tkinter")
ventana.geometry("800x600")
ventana.mainloop() # Metodo que permite tener la ventana todo el tiempo que dure la aplicacion activa
