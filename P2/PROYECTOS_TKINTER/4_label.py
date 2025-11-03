from tkinter import *

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso de etiquetas en Tkinter")

marco1=Frame(ventana,width=600,height=50,bg="#8F12B9",border=2,relief="flat")
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana,width=600,height=50,bg="#3612B9",border=2,relief="raised")
marco2.pack_propagate(False)
marco2.pack()
marco3=Frame(ventana,width=600,height=50,bg="#B92512",border=2,relief=GROOVE)
marco3.pack_propagate(False)
marco3.pack()
marco4=Frame(ventana,width=600,height=50,bg="#B91273",border=2,relief=SUNKEN)
marco4.pack_propagate(False)
marco4.pack()


# Etiqueta o label

etiqueta1=Label(marco1,text="Alex Reyes",bg="#8F12B9").pack(pady=10)
etiqueta2=Label(marco2,text="Universidad Tecnologica de Durango",bg="#3612B9").pack(pady=10)
etiqueta3=Label(marco3,text="Tecnologias de la informacion",bg="#B92512").pack(pady=10)
etiqueta4=Label(marco4,text="Desarrollo de Software Multiplataforma",bg="#B91273").pack(pady=10)

ventana=mainloop()

