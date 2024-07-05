from jogador import Jogador
from baralho import Baralho
import random
from carta_especial import CartaEspecial
from carta_normal import CartaNormal


class Tabuleiro:
    def __init__(self,  baralho: Baralho):
        self.__baralho = baralho
        self.__contador_cartas_mais_um = 0 #se quiser testar comprar cartas do contador, adicione um valor para o contador aqui
        self.__jogadores = [0, 0, 0]
        self.__jogador_local = 0
        self.__primeira_acao = True
        self.__jogador_atual = 0
        self.__local_id = ""
        self.__ultima_carta = self.__baralho.get_carta_normal_aleatoria()
        self.cartas_encadeadas = []
        self.bloqueado = False
        self.precisa_comprar_contador = False
        # self.__ultima_carta = self.__baralho.get_carta_especial_aleatoria() se quiser testar o contador descomente essa função
    
    @property
    def ultima_carta(self):
        return self.__ultima_carta
    
    @property
    def ultima_carta(self):
        return self.__ultima_carta
    
    @property
    def jogador_local(self):
        return self.__jogador_local
    
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
        self.jogador_atual = self.jogador_local

    def atualizar_posicoes_jogadores(self, jogador_atual):
        for i, jogador in enumerate(self.jogadores):
            if jogador.id == self.local_id:
                self.jogador_local = i
        self.jogador_atual = jogador_atual

    def atualizar_jogadores(self, a_move):
        print(a_move)
        for i, jogador in enumerate(a_move["jogadores"]):
            cartas_jogador = []
            for carta in jogador['mao']:
                if carta['cor_primaria'] == 'preto':
                    carta_epecial = CartaEspecial(carta['cor_primaria'], carta['tipo'])
                    cartas_jogador.append(carta_epecial)
                else:
                    carta_normal = CartaNormal(carta['cor_primaria'],carta['cor_secundaria'], carta['numero'])
                    cartas_jogador.append(carta_normal)
            self.jogadores[i] = (Jogador(jogador['id'], jogador['nome'], cartas_jogador))
        self.atualizar_posicoes_jogadores(a_move["jogador_atual"])

    def atualizar_cartas_tabuleiro(self, a_move):
        self.ultima_carta = self.transforma_move_para_carta(a_move["ultima_carta_tabuleiro"])
        self.contador_cartas_mais_um = a_move["contador_cartas_mais_um"]


    def transforma_jogada_para_move(self, tipo_jogada) -> dict:
        jogada = {}
        if tipo_jogada == "init":
            jogada["type"] = tipo_jogada
            jogada["match_status"] = "progress"
            jogada["baralho"] = self.__baralho.to_dict()
            jogada["jogador_atual"] = self.jogador_atual # indice do jogador atual na lista de jogadores
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.ultima_carta.to_dict()
            jogada["contador_cartas_mais_um"] = self.contador_cartas_mais_um
            jogada["primeira_acao"] = self.__primeira_acao # talvez remover, nao esta sendo usado
            jogada["jogadores"] = self.jogadores_to_dict() 

        elif tipo_jogada == "passar_turno":
            jogada["type"] = tipo_jogada
            jogada["match_status"] = "progress"
            jogada["jogador_atual"] = self.jogador_atual
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.ultima_carta.to_dict()
            jogada["contador_cartas_mais_um"] = self.contador_cartas_mais_um
            jogada["jogadores"] = self.jogadores_to_dict() 
            jogada["bloqueado"] = self.bloqueado
            jogada["precisa_comprar_contador"] = self.precisa_comprar_contador


        elif tipo_jogada == "bloquear":
            jogada["type"] = tipo_jogada
            jogada["match_status"] = "progress"
            jogada["jogador_atual"] = self.jogador_atual
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.ultima_carta.to_dict()
            jogada["contador_cartas_mais_um"] = self.contador_cartas_mais_um
            jogada["jogadores"] = self.jogadores_to_dict() 

        elif tipo_jogada == "mais-um":
            jogada["type"] = tipo_jogada
            jogada["match_status"] = "progress"
            jogada["jogador_atual"] = self.jogador_atual
            if self.ultima_carta is not None:
                jogada["ultima_carta_tabuleiro"] = self.ultima_carta.to_dict()
            jogada["contador_cartas_mais_um"] = self.contador_cartas_mais_um
            jogada["jogadores"] = self.jogadores_to_dict() 
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
        return mao
    
    def transforma_move_para_carta(self, move_carta):
        if move_carta["cor_primaria"] == 'preto':
            carta = CartaEspecial(move_carta["cor_primaria"], move_carta["tipo"])
            return carta
        return CartaNormal(move_carta["cor_primaria"], move_carta["cor_secundaria"], move_carta["numero"])

    
    def set_local_id(self, local_id):
        self.__local_id = local_id
    
    def get_baralho(self) -> Baralho:
        return self.__baralho
    
    def get__valordocontador__maisum(self):
        return self.__contador_cartas_mais_um + 1
    
    def add_contador_cartas_mais_um(self):
        self.__contador_cartas_mais_um += 1

    def eh_a_vez_do_jogador_local_jogar(self):
        return self.local_id == self.jogadores[self.jogador_atual].id
