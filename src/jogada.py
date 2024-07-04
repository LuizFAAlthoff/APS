from carta_especial import CartaEspecial
from tkinter import messagebox

class Jogada():
    def __init__(self, jogador, carta_recente_tabuleiro):
        self.__carta_recente_tabuleiro = carta_recente_tabuleiro
        self.__jogador = jogador
        self.__cartas_encadeamento = []
        self.__jogada_vencedora = False
    
    @property
    def carta_recente_tabuleiro(self):
        return self.__carta_recente_tabuleiro

    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def cartas_encadeamento(self):
        return self.__cartas_encadeamento
    
    @property
    def jogada_vencedora(self):
        return self.__jogada_vencedora
    
    @carta_recente_tabuleiro.setter
    def carta_recente_tabuleiro(self, carta_recente_tabuleiro):
        self.__carta_recente_tabuleiro = carta_recente_tabuleiro

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
    
    @cartas_encadeamento.setter
    def cartas_encadeamento(self, cartas_encadeamento):
        self.__cartas_encadeamento = cartas_encadeamento
    
    @jogada_vencedora.setter
    def jogada_vencedora(self, jogada_vencedora):
        self.__jogada_vencedora = jogada_vencedora

    def __del__(self):
        print(f"Jogada do jogador {self.__jogador.nome} foi deletada")

    def encadeamento_atual_menor_que_3(self):
        return len(self.__cartas_encadeamento) < 3
        
    def ainda_nao_jogou(self):
        if len(self.__cartas_encadeamento) == 0:
            return True
        else:
            return False
    
    def get_ultima_carta_encadeamento(self):
        return self.__cartas_encadeamento[-1]
    
    def verificar_condicao_de_vitoria(self):
        if len(self.__jogador.mao) - len(self.__cartas_encadeamento) == 0:
            self.__jogada_vencedora = True
            return True
    
    def verificar_existencia_especial_no_encadeamento(self):
        for carta in self.__cartas_encadeamento:
            if isinstance(carta, CartaEspecial):
                return True
        return False

    def add_carta_encadeamento(self, carta):
        self.__jogador.mao.remove(carta)
        self.__cartas_encadeamento.append(carta)

    def verificar_se_eh_ultima_carta(self):
        if len(self.__jogador.mao) == 1:
            return True
        else:
            return False

    def verificar_se_lista_encadeamento_esta_vazia(self):
        if len(self.__cartas_encadeamento) == 0:
            return True
        else:
            return

    def checar_compatibilidade(self, carta_para_jogar, carta_mais_recente, pode_numero):
        carta_eh_valida = False
        if isinstance(carta_mais_recente, CartaEspecial):
            print("Carta compatível porque a carta anterior é especial")
            carta_eh_valida = True
        elif pode_numero and carta_para_jogar.numero == carta_mais_recente.numero:
            print("Carta compatível com a anterior porque é a primeira carta e números são iguais")
            carta_eh_valida = True
        elif carta_mais_recente.cor_primaria == carta_para_jogar.cor_primaria:
            print("Carta compatível com a anterior porque cores primárias são iguais")
            carta_eh_valida = True
        elif carta_mais_recente.cor_primaria == carta_para_jogar.cor_secundaria:
            print("Carta compatível com a anterior porque cores primária e secundária são iguais")
            carta_eh_valida = True
        elif carta_mais_recente.cor_secundaria == carta_para_jogar.cor_primaria:
            print("Carta compatível com a anterior porque cores secundária e primária são iguais")
            carta_eh_valida = True
        elif carta_mais_recente.cor_secundaria == carta_para_jogar.cor_secundaria:
            print("Carta compatível com a anterior porque cores secundárias são iguais")
            carta_eh_valida = True
        else:
            print("Carta incompatível com a anterior")
            carta_eh_valida = False

        return carta_eh_valida
            


    def verificar_carta(self, carta_para_jogar):
        if self.encadeamento_atual_menor_que_3():                        #verifica se seq max ainda não foi atingida
            if self.verificar_existencia_especial_no_encadeamento():    #caso exista carta especial no encadeamento, retorna False
                print("Carta especial não pode ser jogada no meio de uma sequência")
                return False
            if isinstance(carta_para_jogar, CartaEspecial):             #verifica se a carta a ser jogada é especial
                if self.verificar_se_eh_ultima_carta():                     #caso a carta especial a ser jogada seja a última, retorna False
                    print("Carta especial não pode ser jogada como última carta")
                    return False
                else:                                                       #caso não seja a última, verifica se a lista de encadeamento está vazia
                    if self.verificar_se_lista_encadeamento_esta_vazia():       
                        return True                                             #caso esteja vazia, retorna True
                    else:                                                       #caso não esteja vazia, retorna False
                        print("Carta especial não pode ser jogada no meio de uma sequência")
                        return False
            else:                                                       #caso a carta a ser jogada não seja especial, ela é normal
                if self.verificar_se_lista_encadeamento_esta_vazia():       #verifica se a lista de encadeamento está vazia
                    print("Pegou carta mais recente do tabuleiro")
                    pode_numero = True
                    carta_mais_recente = self.carta_recente_tabuleiro           #pega a carta mais recente a partir do parametro recebido pelo tabuleiro
                    return self.checar_compatibilidade(carta_para_jogar, carta_mais_recente, pode_numero) #checa se a carta a ser jogada é compatível com a carta mais recente
                        
                else:
                    print("Pegou carta mais recente da lista de encadeamento")
                    carta_mais_recente = self.get_ultima_carta_encadeamento()          #pega a carta mais recente a partir da lista de encadeamento
                    pode_numero = False
                    if self.checar_compatibilidade(carta_para_jogar, carta_mais_recente, pode_numero): #checa se a carta a ser jogada é compatível com a carta mais recente
                        return True                                             #caso seja compatível, retorna True
        else:                                                       #caso a seq max tenha sido atingida, retorna False
            messagebox.showwarning("Atenção", "Encadeamento máximo atingido")
            return False