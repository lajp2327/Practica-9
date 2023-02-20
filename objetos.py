from Personaje import *
heroe= personaje()

print("El personaje se llama: " + heroe.nombre)
print("El personaje es un: " + heroe.especie)
print("El personaje mide: " + heroe.altura)

heroe.correr(True)
heroe.lanzar_granadas()
heroe.recargar_arma(87)