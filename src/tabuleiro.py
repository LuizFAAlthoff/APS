from jogador import Jogador
from carta_especial import CartaEspecial
from carta_normal import CartaNormal
import random


class Tabuleiro:
    def __init__(self):
        self.__ultima_carta = None
        self.__lista_cartas = []
        self.criar_baralho()
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
        return self.__joagadores
    
    @property
    def primeira_acao(self):
        return self.__primeira_acao
    
    @property
    def jogador_atual(self):
        return self.__jogador_atual

    @property
    def local_id(self):
        return self.__local_id
    
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
        self.__joagadores = jogadores
    
    @primeira_acao.setter
    def primeira_acao(self, primeira_acao):
        self.__primeira_acao = primeira_acao
    
    @jogador_atual.setter
    def jogador_atual(self, jogador_atual):
        self.__jogador_atual = jogador_atual

    @local_id.setter
    def local_id(self, local_id):
        self.__local_id = local_id

    def criar_baralho(self):
        cores_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
        cores_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
        lista_cartas_comuns = []
        lista_cartas_especiais = []

        for cor_primaria in cores_primaria:
            for cor_secundaria in cores_secundaria:
                for numero in range(1, 4):
                    if cor_primaria != cor_secundaria:
                        lista_cartas_comuns.append(CartaNormal(cor_primaria, cor_secundaria, numero))
                        #print("carta criada: ", cor_primaria, cor_secundaria, numero)
        for numero in range(7):
            lista_cartas_especiais.append(CartaEspecial('preto', 'mais-um'))
            lista_cartas_especiais.append(CartaEspecial('preto', 'block'))
        
        self.__lista_cartas.extend(lista_cartas_comuns)
        self.__lista_cartas.extend(lista_cartas_especiais)


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
            jogada["baralho"] = self.getMesa().getBaralho().to_json()
            jogada["jogador_1"] = self.__jogadores[0].to_json()
            jogada["jogador_2"] = self.__jogadores[1].to_json()
            jogada["jogador_3"] = self.__jogadores[2].to_json()
            jogada["jogador_atual"] = self.getJogadorAtual()
            jogada["mesa"] = self.getMesa().getUltimaCarta().to_json()

        return jogada
    
    def dar_cartas_iniciais(self) -> list:
        mao = []
        for _ in range(7):
            carta = random.choice(self.__lista_cartas)
            mao.append(carta)
        return mao
    
    def set_local_id(self, local_id):
        self.__local_id = local_id

    def get_random_card(self):
        return random.choice(self.__lista_cartas)