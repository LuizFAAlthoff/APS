from entities.carta import Carta


class CartaNormal(Carta):
    def __init__(self, cor_primaria: str, cor_secundaria: str, numero: int):
        super().__init__(cor_primaria)
        self.__cor_secundaria = cor_secundaria
        self.__numero = numero
    
    @property
    def cor_secundaria(self):
        return self.__cor_secundaria
    
    @property
    def numero(self):
        return self.__numero
    
    @cor_secundaria.setter
    def cor_secundaria(self, cor_secundaria):
        self.__cor_secundaria = cor_secundaria
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero