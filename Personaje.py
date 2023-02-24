class personaje:
    #Constructor  de personaje
    def __init__(self,esp,nom,alt):
    #atributos personaje
        self.__especie=esp
        self.__nombre=nom
        self.__altura=alt
    
    #métodos personaje
    def correr(self, status):
        if (status):
            print("El personaje" + self.__nombre + " está corriendo")
        else:
            print("El personaje " + self.__nombre + " se detuvo")
    def lanzar_granadas(self):
        print("El personaje" + self.__nombre + " lanzó una granada")
    def recargar_arma(self, municiones):
        cargador=10
        cargador=cargador+municiones
        print("Tu arma tiene " + str(cargador) + " balas")
    def __pensar(self):
        print("Estoy pensando...")
        
    #Getters y Setters
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nom):
        self.__nombre=nom
    def getespecie(self):
        return self.__especie
    def setespecie(self,esp):
        self.__nombre=esp
    def getaltura(self):
        return self.__altura
    def setnombre(self,alt):
        self.__nombre=alt