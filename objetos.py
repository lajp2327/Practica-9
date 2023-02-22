from Personaje import *

#solicitar datos
print("")
print("Datos heroe")
espH=input("Escribe la especie del Héroe: ")
nomH=input("Escribe el nombre del Héroe: ")
altH=float(input("Escribe ela altura del Héroe: "))
recargaH=int(input("¿Cuántas balas recargas al Héroe? "))

print("")
print("Datos villano")
espV=input("Escribe la especie del Villano: ")
nomV=input("Escribe el nombre del Villano: ")
altV=float(input("Escribe ela altura del Villano: "))
recargaV=int(input("¿Cuántas balas recargas al Villano? "))

#Crear objeto de clase
heroe= personaje(espH,nomH,altH)
villano=personaje(espV,nomV,altV)

#Atributos
print("Objeto Heroe")
print("El personaje se llama: " + heroe.nombre)
print("El personaje es un: " + heroe.especie)
print("El personaje mide: " + str(heroe.altura))
heroe.correr(True)
heroe.lanzar_granadas()
heroe.recargar_arma(recargaH)

print("Objeto Villano")
print("El personaje se llama: " + villano.nombre)
print("El personaje es un: " + villano.especie)
print("El personaje mide: " + str(villano.altura))
villano.correr(True)
villano.lanzar_granadas()
villano.recargar_arma(recargaV)