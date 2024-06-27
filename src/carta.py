from abc import ABC

class Carta(ABC):
    def __init__(self, cor_primaria):
        self.__cor_primaria = cor_primaria
    
    @property
    def cor_primaria(self):
        return self.__cor_primaria
    
    @cor_primaria.setter
    def cor_primaria(self, cor_primaria):
        self.__cor_primaria = cor_primaria

    def get_card_image(self):
        print("precisa ser sobrescrito")