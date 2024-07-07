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
                    'tipo': carta.tipo
                }
            jogador['mao'].append(carta_dict)
        return jogador
    