#Buscar archivos
import os 
import sys 
#Funcion:
def buscarArchivos(ruta, extension):
    extension = extension.lower()
    if not os.path.exists(ruta):
        print ("La ruta especificada no existe")
        sys.exit()
    else:
        if not extension.startswith("."):
            extension = "."+extension 
        lista = os.listdir(ruta)
        for l in lista:
            if l.endswith(extension):
                print(l)
                
#Main:
print("Bienvenidx a la busqueda de archivos by Cande :)")
ruta = input("\nIngrese ruta donde buscar: ")
nombre = input("Ingrese extension de archivo a buscar: ")
buscarArchivos(ruta,nombre)


        
                
        