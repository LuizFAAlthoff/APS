from carta_normal import CartaNormal


class Jogador:
    def __init__(self, id: str, nome: str, mao: list):
        self.__id = id
        self.__nome = nome
        self.__mao = mao

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def mao(self):
        return self.__mao
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @mao.setter
    def mao(self, mao):
        self.__mao = mao
    
    ## fazer método Initialize
    
    def escolher_carta(self, indice_carta: bool):
        return self.mao[indice_carta]
    
    def add_cartas_na_mao(self, objeto_carta):
        self.mao.append(objeto_carta)
    
    def get_cartas_mao(self, index: int):
        return self.mao[index]
    
    def to_dict(self):
        jogador = {
                'id': self.id,
                'nome': self.nome,
                'mao': []
            }
        for carta in self.__mao:
            carta_dict = {}
            if isinstance(carta, CartaNormal): 
                carta_dict = {
                    'cor_primaria': carta.cor_primaria,
                    'cor_secundaria': carta.cor_secundaria,
                    'numero': carta.numero
                }
            else:
                carta_dict = {
                    'cor_primaria': carta.cor_primaria,
                    'tipo': carta.tipo,
                    'ja_satisfeita': carta.ja_satisfeita
                }
            jogador['mao'].append(carta_dict)

            
        return jogador
    
    def print_cartas(self):
        for carta in self.__mao:
            if isinstance(carta, CartaNormal):
                print(carta.cor_primaria, carta.cor_secundaria, carta.numero)
            else:
                print(carta.cor_primaria, carta.tipo)