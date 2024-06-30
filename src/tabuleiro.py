from jogador import Jogador
from baralho import Baralho
import random

from carta_especial import CartaEspecial
from carta_normal import CartaNormal


class Tabuleiro:
    def __init__(self,  baralho: Baralho):
        self.__ultima_carta = None
        # self.__lista_cartas = []
        self.__baralho = baralho
        self.__contador_cartas_mais_um = 0
        self.__jogadores = [0, 0] # adicionar mais um 0 
        self.__jogador_local = 0
        self.__jogador_dois = 0
        self.__jogador_tres = 0
        self.__primeira_acao = True
        self.__jogador_atual = None
        self.__local_id = ""
    
    @property
    def ultima_carta(self):
        return self.__ultima_carta
    
    @property
    def jogador_local(self):
        return self.__jogador_local
    
    @property
    def jogador_dois(self):
        return self.__jogador_dois
    
    @property
    def jogador_tres(self):
        return self.__jogador_tres
    
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

    @jogador_local.setter
    def jogador_local(self, jogador_local):
        self.__jogador_local = jogador_local

    @jogador_dois.setter
    def jogador_dois(self, jogador_dois):
        self.__jogador_dois = jogador_dois  

    @jogador_tres.setter
    def jogador_tres(self, jogador_tres):
        self.__jogador_tres = jogador_tres                
    
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
        return self.transforma_jogada_para_move("init")

    def criar_jogadores(self, jogadores):
        for i, jogador in enumerate(jogadores):
            mao = self.dar_cartas_iniciais()
            jogador_criado = Jogador(id=jogador[1], nome=jogador[0], mao=mao)
            self.jogadores[i] = jogador_criado
            if jogador_criado.id == self.local_id:
                self.jogador_local = i
            else:
                if self.jogador_dois == 0:
                    self.jogador_dois = i
                else:
                    self.jogador_tres = i
        self.jogador_atual = self.local_id

    def atualizar_jogadores(self, jogadores):
        self.jogadores = jogadores
        for i, jogador in enumerate(jogadores):
            if jogador.id == self.local_id:
                self.jogador_local = i
            else:
                if self.jogador_dois == 0:
                    self.jogador_dois = i
                else:
                    self.jogador_tres = i
        self.jogador_atual = self.local_id

    def transforma_move_para_jogada(self, a_move):
        x = 0
        print(a_move)
        for jogador in a_move["jogadores"]:
            cartas_jogador = []
            for carta in jogador.mao:
                if carta['cor_primaria'] == 'preto':
                    carta_epecial = CartaEspecial(carta['cor_primaria'], carta['tipo'])
                    carta_epecial.ja_satisfeita = carta['ja_satisfeita']
                    cartas_jogador.append(carta_epecial)
                else:
                    carta_normal = CartaNormal(carta['cor_primaria'],carta['cor_secundaria'], carta['numero'])
                    carta_normal.ja_satisfeita = carta['ja_satisfeita']
                    cartas_jogador.append(carta_normal)
            self.jogadores.append(Jogador(jogador.id, jogador.nome, cartas_jogador))


    def transforma_jogada_para_move(self, tipo_jogada) -> dict:
        jogada = {}
        if tipo_jogada == "init":
            jogada["tipo"] = "init"
            jogada["match_status"] = "progress"
            jogada["baralho"] = self.__baralho.to_dict()
            jogada["jogador_atual"] = self.__jogador_atual
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.__ultima_carta.to_dict()
            else:
                jogada["ultima_carta_tabuleiro"] = self.__ultima_carta
            jogada["contador_cartas_mais_um"] = self.__contador_cartas_mais_um
            jogada["primeira_acao"] = self.__primeira_acao
            jogada["jogadores"] = self.jogadores_to_dict() 
            
            #adiconar o
            #  terceiro jogador, por enquanto ta com 2 pq é mais facil de debugar
        return jogada
    
    def jogadores_to_dict(self):
        print(self.jogadores)
        if 0 not in self.jogadores:
            jogadores_dict = []
            for jogador in self.jogadores:
                jogadores_dict.append(jogador.to_dict())
            return jogadores_dict
        else:
            return self.jogadores


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
    