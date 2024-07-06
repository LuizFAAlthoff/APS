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
        return self.cartas_encadeamento[-1]
    
    def verificar_condicao_de_vitoria(self):
        if len(self.jogador.mao) == 0:
            self.jogada_vencedora = True
            return True
        else:
            return False
    
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
        carta_eh_valida = False
        encadeamento_eh_menor_que_tres = self.encadeamento_atual_menor_que_3()
        if encadeamento_eh_menor_que_tres:   
            tem_especial_no_encadeamento = self.verificar_existencia_especial_no_encadeamento()                     
            if tem_especial_no_encadeamento:    
                return carta_eh_valida
            eh_especial = isinstance(carta_para_jogar, CartaEspecial)
            if eh_especial:  
                eh_ultima_carta =  self.verificar_se_eh_ultima_carta()         
                if eh_ultima_carta:                     
                    return carta_eh_valida
                else:
                    lista_encadeamento_eh_vazia = self.verificar_se_lista_encadeamento_esta_vazia()                                                   
                    if lista_encadeamento_eh_vazia:
                        carta_eh_valida = True       
                        return carta_eh_valida                                             
                    else:                                                       
                        return carta_eh_valida
            else:   
                lista_encadeamento_eh_vazia = self.verificar_se_lista_encadeamento_esta_vazia()                                                
                if lista_encadeamento_eh_vazia:       
                    pode_numero = True
                    carta_mais_recente = self.carta_recente_tabuleiro   
                    eh_compativel = self.checar_compatibilidade(carta_para_jogar, carta_mais_recente, pode_numero)      
                    return eh_compativel
                        
                else:
                    carta_mais_recente = self.get_ultima_carta_encadeamento()          
                    pode_numero = False
                    eh_compativel = self.checar_compatibilidade(carta_para_jogar, carta_mais_recente, pode_numero)
                    if eh_compativel: 
                        carta_eh_valida = True
                        return carta_eh_valida                                             
        else:                                                       
            messagebox.showwarning("Atenção", "Encadeamento máximo atingido")
            return carta_eh_valida