
from View import Interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view = Interfaz.Vistas(ventana)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
