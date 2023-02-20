class personaje:
    
    #atributos personaje
    especie="Humano"
    nombre="Master Chief"
    altura="2.70"
    
    #métodos personaje
    def correr(self, status):
        if (status):
            print("El personaje" + self.nombre + " está corriendo")
        else:
            print("El personaje " + self.nombre + " se detuvo")
    def lanzar_granadas(self):
        print("El personaje" + self.nombre + " lanzó una granada")
    def recargar_arma(self, municiones):
        cargador=10
        cargador=cargador+municiones
        print("Tu arma tiene " + str(cargador) + " balas")