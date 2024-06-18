from entities.carta import Carta


class CartaEspecial(Carta):
    def __init__(self, cor_primaria: str, tipo: str):
        super().__init__(cor_primaria)
        self.__tipo = tipo
        self.__ja_satisfeita = False

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def ja_satisfeita(self):
        return self.__ja_satisfeita
    
    ## não fiz setter do atributo tipo pois ele nunca será alterado
    
    @ja_satisfeita.setter
    def ja_satisfeita(self, ja_satisfeita):
        self.__ja_satisfeita = ja_satisfeita