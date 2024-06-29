from carta import Carta


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
    
    @property
    def cor_primaria(self):
        return super().cor_primaria
    ## não fiz setter do atributo tipo pois ele nunca será alterado
    
    @ja_satisfeita.setter
    def ja_satisfeita(self, ja_satisfeita):
        self.__ja_satisfeita = ja_satisfeita
    
    def get_card_image(self):
        return f"src/cartas/{self.tipo}.jpeg"
    
    def to_dict(self):
        return {'cor_primaria': self.cor_primaria,
                'tipo': self.tipo,
                'ja_satisfeita': self.ja_satisfeita}