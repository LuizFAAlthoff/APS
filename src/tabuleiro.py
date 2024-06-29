from jogador import Jogador
from baralho import Baralho
import random


class Tabuleiro:
    def __init__(self,  baralho: Baralho):
        self.__ultima_carta = None
        # self.__lista_cartas = []
        self.__baralho = baralho
        self.__contador_cartas_mais_um = 0
        self.__jogadores = [0, 0, 0]
        self.__primeira_acao = True
        self.__jogador_atual = None
        self.__local_id = ""
    
    @property
    def ultima_carta(self):
        return self.__ultima_carta
    
    @property
    def lista_cartas(self):
        return self.__lista_cartas
    
    @property
    def contador_cartas_mais_um(self):
        return self.__contador_cartas_mais_um
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def primeira_acao(self):
        return self.__primeira_acao
    
    @property
    def jogador_atual(self):
        return self.__jogador_atual

    @property
    def local_id(self):
        return self.__local_id
    
    @property
    def baralho(self):
        return self.__baralho
    
    @ultima_carta.setter
    def ultima_carta(self, ultima_carta):
        self.__ultima_carta = ultima_carta
        
    @lista_cartas.setter
    def lista_cartas(self, lista_cartas):
        self.__lista_cartas = lista_cartas
    
    @contador_cartas_mais_um.setter
    def contador_cartas_mais_um(self, contador_cartas_mais_um):
        self.__contador_cartas_mais_um = contador_cartas_mais_um
    
    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores
    
    @primeira_acao.setter
    def primeira_acao(self, primeira_acao):
        self.__primeira_acao = primeira_acao
    
    @jogador_atual.setter
    def jogador_atual(self, jogador_atual):
        self.__jogador_atual = jogador_atual

    @local_id.setter
    def local_id(self, local_id):
        self.__local_id = local_id

    @baralho.setter
    def baralho(self, baralho):
        self.baralho = baralho


    def comecar_partida(self, jogadores: list, id_jogador_local: int):
        self.set_local_id(id_jogador_local)
        self.criar_jogadores(jogadores)
        return self.transform_play_to_dict("init")

    def criar_jogadores(self, jogadores):
        for i, jogador in enumerate(jogadores):
            mao = self.dar_cartas_iniciais()
            self.__jogadores[i] = Jogador(id=jogador[1], nome=jogador[0], mao=mao)


    def transform_play_to_dict(self, tipo_jogada) -> dict:
        jogada = {}
        if tipo_jogada == "init":
            jogada["tipo"] = "init"
            jogada["match_status"] = "progress"
            jogada["baralho"] = self.__baralho.to_dict()
            jogada["jogador_atual"] = self.__jogador_atual #verificar se precisa usar to_dict()
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.__ultima_carta.to_dict()
            else:
                jogada["ultima_carta_tabuleiro"] = self.__ultima_carta
            jogada["contador_cartas_mais_um"] = self.__contador_cartas_mais_um
            jogada["primeira_acao"] = self.__primeira_acao
            jogada["jogador_1"] = self.__jogadores[0].to_dict()
            jogada["jogador_2"] = self.__jogadores[1].to_dict()
            # jogada["jogador_3"] = self.__jogadores[2].to_json() #adiconar o
            #  terceiro jogador, por enquanto ta com 2 pq é mais facil de debugar
            x=1
        return jogada
    
        self.__jogador_atual = None
        self.__local_id = ""
    
    def dar_cartas_iniciais(self) -> list:
        mao = []
        for _ in range(7):
            carta = random.choice(self.get_baralho().get_cartas())
            mao.append(carta)
        x=1
        return mao
    
    def set_local_id(self, local_id):
        self.__local_id = local_id

    def get_random_card(self):
        return random.choice(self.__lista_cartas)
    
    def get_baralho(self) -> Baralho:
        x = self.__baralho
        return self.__baralho