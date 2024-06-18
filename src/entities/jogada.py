

class Jogada():
    def __init__(self, jogador):
        self.__jogador = jogador
        self.__cartas_encadeamento = []
        self.__jogada_vencedora = False
    
    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def cartas_encadeamento(self):
        return self.__cartas_encadeamento
    
    @property
    def jogada_vencedora(self):
        return self.__jogada_vencedora
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
    
    @cartas_encadeamento.setter
    def cartas_encadeamento(self, cartas_encadeamento):
        self.__cartas_encadeamento = cartas_encadeamento
    
    @jogada_vencedora.setter
    def jogada_vencedora(self, jogada_vencedora):
        self.__jogada_vencedora = jogada_vencedora