#Instanciar los Objetos para posteriormente implementarlos.
from coches import Coches,Camines, Camionetas
import os
os.system("cls")

def borrarPantalla():
    os.system("cls")
    
def esperarTecla():
    input("\n\t..Oprima una tecla para continuar...")    

#oche=Coches("VW","Blanco","202",220,200,5)
#rint(coche.marca, coche.acelerar())
#
#amioneta=Camionetas("Chevrolet","Rojo","2020",180,150,7,"Tracera",True)
#rint(camioneta.marca, camioneta.acelerar())
#
#amion=Camines("Ford","Azul","2019",160,120,3,2,5000)
#rint(camion.marca, camion.acelerar())

# num_coches=int(input("¿Cuantos coches deseas?: "))

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t...Ingresar datos del vehiculo tipo: {tipo}...")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad:  "))
    caballaje=int(input("Caballaje: "))
    plazas=int(input("Numero de plazas: "))
    return marca,color,modelo,velocidad,caballaje,plazas #para que autos, camiones y camionetas puedan utilizar esto


def imprimir_datos_vehiculo(marca,color,modelo,velocidad,caballaje,plazas):
        print(f"Datos del Vehiculo \n Marca: {marca()} \n Color: {color()} \n Modelo: {modelo()} \n Velocidad Maxima: {velocidad()} \n Caballaje: {caballaje()} \n Numero de Plazas: {plazas()}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

def camiones():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camiones")
    
    eje=int(input("Ingrese el numero de ejes del camion: "))
    capacidadCarga=int(input("Ingrese la capacidad de carga del camion (Kg): "))

    #Crea un objeto o instancia de la clase Coches
    coche=Camines(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga)

    
def camionetas():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camionetas")
    traccion=input("Ingrese el tipo de eje de la camioneta: ").upper()
    cerrada=bool(input("¿Cerrada SI o No?: "))
    
    #if cerrada=="SI":
    #     cerrada=True
    # else:
    #     cerrada=False   

    #Crea un objeto o instancia de la clase Coches

    coche=Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada)

def main():
    opcion=True
    while opcion:
        os.system("cls")
        opcion=input("\n\t\t .::Menu Principal::.\n\t 1.-Autos\n\t 2.-Camionetas\n\t 3.-Camiones\n\t 4.-Salir\n\n\t Elige una opcion:")
        match opcion:
            case "1":
                autos()
                esperarTecla()
            case "2":
                camionetas()
                esperarTecla()
            case "3":
                camiones()
                esperarTecla()
            case "4":
                input("\n\t\t...Gracias por su visita...")
                esperarTecla()
                opcion=False
            case _:
                #no espere tecla porque ya tengo un input
                input("\n\t...Opcion no valida, vuelva a itentarlo...Oprima una tecla para continuar...") 
                
if __name__=="__main__":
    main()                