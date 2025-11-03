from tkinter import *

ventana=Tk()
ventana.title("Uso del Main Loop")
ventana.geometry("600x400")

marco1=Frame(ventana,width=600,height=50,bg="#FB0808",border=2,relief=RAISED).pack()
marco2=Frame(ventana,width=600,height=50,bg="#FBAE08",border=2,relief=RAISED).pack()
marco3=Frame(ventana,width=600,height=50,bg="#FBFB08",border=2,relief=RAISED).pack()
marco4=Frame(ventana,width=600,height=50,bg="#31FB08",border=2,relief=RAISED).pack()
marco5=Frame(ventana,width=600,height=50,bg="#4508FB",border=2,relief=RAISED).pack()
marco6=Frame(ventana,width=600,height=50,bg="#7D08FB",border=2,relief=RAISED).pack()

ventana.mainloop()

