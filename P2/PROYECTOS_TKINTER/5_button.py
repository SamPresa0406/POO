from tkinter import *

def cambiarTexto():
    label_nombre.config(text="Samantha Presa")
    label_password.config(text="1234")
    
def regresarTexto():
        

ventana=Tk()

ventana.title("Uso de Botones, Marcos, Etiquetas")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    width=800,
    height=100,
    border=2,
    relief=SOLID,
    bg="silver",
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulo=Label(frame_principal,text="Inicio de Sesion")
label_titulo.config(
    bg="silver",
    height=50,
    font="Arial",   
)
label_titulo.pack()

label_nombre=Label(ventana,text="Nombre...").pack(pady=10)
label_nombre.pack(pady=10)
label_password=Label(ventana,text="Contraseña: ...").pack(pady=10)
label_password.pack(pady=10)

boton_aceptar=Button(ventana,text="Aceptar",command=cambiarTexto).pack(pady=10)
boton_regresar=Button(ventana,text="Regresar",command=regresarTexto).pack(pady=10)


ventana.mainloop()

