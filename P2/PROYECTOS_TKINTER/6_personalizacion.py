
from tkinter import *

ventana=Tk()

ventana.title("Personalizar Widgets u Objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")#minimo, lo mas basico que debe llevar
etiqueta.config(
    
  bg="lightblue"
  fg="darkblue",
  width=50,
  height=4,
  font=("Helvetica",30,"italic"),
  relief=SOLID,
  border=2
    
    
)

etiqueta.pack(pady=25)

ventana.mainloop()