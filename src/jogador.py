

class Jogador:
    def __init__(self, nome, mao_cartas):
        self.__nome = nome
        self.__mao_cartas = mao_cartas

    @property
    def nome(self):
        return self.__nome
    
    @property
    def mao_cartas(self):
        return self.__mao_cartas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @mao_cartas.setter
    def mao_cartas(self, mao_cartas):
        self.__mao_cartas = mao_cartas
    
    ## fazer método Initialize
    
    def escolher_carta(self, indice_carta: bool):
        return self.mao_cartas[indice_carta]
    
    def add_cartas_na_mao(self, lista_carta):
        self.mao_cartas.append(lista_carta)
    
    def get_cartas_mao(self, index: int):
        return self.mao_cartas[index]