from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Marcos o Frames en Tkinter")
# ventana.resizable(False,False) # Esto hace que no pueda modificarse el tamaño de la ventana

marco1=Frame(ventana,width=400,height=200, bg="blue", relief=SOLID, border=2)
marco1.pack_propagate(False) # Evitar que se modifique el estilo del marco
marco1.pack(pady=200) # Es importante para que se dibuje o muestre el widget o el objeto dentro de la ventana
marco2=Frame(marco1,width=300,height=150,bg="silver", relief='groove', border=10).pack(pady=50)

ventana=mainloop()

