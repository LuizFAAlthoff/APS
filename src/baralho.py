from carta_normal import CartaNormal
from carta_especial import CartaEspecial
import random


class Baralho():
    
    def __init__(self) -> None:
        self.__cartas = []
        self.criar_baralho()

    @property
    def cartas(self):
        return self.__cartas
    
    @cartas.setter
    def ultima_carta(self, cartas):
        self.__cartas = cartas


    def darCarta(self):
        return random.choice(self.__cartas)
    
    def get_cartas(self):
        return self.__cartas
    
    
    def criar_baralho(self):
        cores_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
        cores_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
        lista_cartas_comuns = []
        lista_cartas_especiais = []

        for cor_primaria in cores_primaria:         #cria as 126 cartas normais e as adiciona numa lista de cartas comuns
            for cor_secundaria in cores_secundaria:
                for numero in range(1, 4):
                    if cor_primaria != cor_secundaria:
                        lista_cartas_comuns.append(CartaNormal(cor_primaria, cor_secundaria, numero))

        for numero in range(7):                     #cria as 14 cartas especiais e as adiciona numa lista de cartas especiais
            lista_cartas_especiais.append(CartaEspecial('preto', 'mais-um'))
            lista_cartas_especiais.append(CartaEspecial('preto', 'bloquear'))
        
        self.__cartas.extend(lista_cartas_comuns)  #adiciona as cartas comuns e especiais ao baralho via extend. É importante usar extend para evitar termos duas sublistas
        self.__cartas.extend(lista_cartas_especiais)    #as primeiras cartas do baralho são as comuns e as últimas são as especiais, 

    def to_dict(self):
        baralho = {'cartas': []}
        for carta in self.__cartas:
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
            baralho['cartas'].append(carta_dict)
        return
    
    def get_carta_aleatoria(self):
        return random.choice(self.__cartas)
    
    def get_carta_normal_aleatoria(self):
        index_aleatorio = random.randint(0, 125) #gera um número aleatório entre 0 e 125, pois as cartas normais são os primeiros 126 elementos da lista de cartas
        return self.__cartas[index_aleatorio]
    
    def get_carta_especial_aleatoria(self):
        index = random.randint(126, 127)
        return self.__cartas[index]