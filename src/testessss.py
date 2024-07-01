
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Button
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk
import random
from carta_normal import CartaNormal
from carta_especial import CartaEspecial
from jogada import Jogada

class AppTeste:
    def __init__(self, root):
        self.tabuleiro = TabuleiroTeste()
        self.root = root
        self.root.title("Interface de testes")
        self.root.geometry("1280x720")

        self.label = Label(root)
        self.label.pack(expand=True)

        self.button_carta_aleatoria = Button(root, text="Passar turno", command=self.passar_turno)
        self.button_carta_aleatoria.pack()

        self.button1 = Button(self.root, text="Ação Jogador 1", command=lambda: self.realizar_jogada(0))
        self.button1.pack(pady=5)
        
        self.button2 = Button(self.root, text="Ação Jogador 2", command=lambda: self.realizar_jogada(1))
        self.button2.pack(pady=5)
        
        self.button3 = Button(self.root, text="Ação Jogador 3", command=lambda: self.realizar_jogada(2))
        self.button3.pack(pady=5)

    def realizar_jogada(self, player_id):
        self.tabuleiro.jogada_atual = Jogada(self.tabuleiro.jogadores[player_id], self.tabuleiro.ultima_carta)
        if player_id == self.tabuleiro.get_jogador_da_vez():
            print(f"Jogador {player_id} realizou uma ação!")
            random_card = self.tabuleiro.get_random_card(self.tabuleiro.lista_cartas)
            if self.tabuleiro.jogada_atual.verificar_carta(random_card) == True:
                self.tabuleiro.ultima_carta = random_card
                self.show_card(self.tabuleiro.ultima_carta)
            else:
                print("Carta inválida!")
        else:
            print(f"Não é o turno do Jogador {player_id}.")

    def passar_turno(self):
        self.tabuleiro.mudar_turno(self.tabuleiro.jogada_atual)

    def show_card(self, carta):
        image_path = carta.get_card_image()

        image = Image.open(image_path)
        image = image.resize((256//2, 345//2), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.label.config(image=photo)
        self.label.image = photo

class JogadorTeste:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__id = ""
        self.__mao_cartas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id

    @property
    def mao_cartas(self):
        return self.__mao_cartas
    
    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @mao_cartas.setter
    def mao_cartas(self, mao_cartas):
        self.__mao_cartas = mao_cartas
    
    def add_cartas_na_mao(self, lista_carta):
        self.mao_cartas.extend(lista_carta)
    
    def get_cartas_mao(self, index: int):
        return self.mao_cartas[index]

class TabuleiroTeste:
    def __init__(self):
        self.__ultima_carta = None
        self.__lista_cartas = []
        self.criar_baralho()
        self.__contador_cartas_mais_um = 0
        self.__jogadores = [JogadorTeste("Maria1"), JogadorTeste("Pedro2"), JogadorTeste("Fabi3")]
        self.__primeira_acao = True
        self.__jogador_atual = None
        self.__local_id = ""
        self.__turno = 0
        self.__jogada_atual = None

        id = 0
        for player in self.__jogadores:
            player.id = id
            id += 1

        for player in self.__jogadores: #distribui 7 cartas para cada jogador
            player.add_cartas_na_mao(self.dar_cartas_iniciais())
    
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
        for numero in range(7):
            lista_cartas_especiais.append(CartaEspecial('preto', 'mais-um'))
            lista_cartas_especiais.append(CartaEspecial('preto', 'block'))
        
        self.__lista_cartas.extend(lista_cartas_comuns)
        self.__ultima_carta = self.get_random_card(lista_cartas_comuns)
        self.__lista_cartas.extend(lista_cartas_especiais)

    def dar_cartas_iniciais(self) -> list:
        mao_inicial = []
        for _ in range(7):
            carta_aleatoria = self.get_random_card(self.__lista_cartas)
            mao_inicial.append(carta_aleatoria)
        return mao_inicial

    def get_random_card(self, lista):
        return random.choice(lista)
    
    def mudar_turno(self, jogada_antiga):
        del jogada_antiga
        self.__turno = (self.__turno + 1) % len(self.__jogadores) #isso aqui garante que quando chegar no final da lista, ele volta pro começo
        print("Turno mudou para o jogador ", self.__jogadores[self.__turno].nome)
        return self.__jogadores[self.__turno]

    def get_jogador_da_vez(self):
        print("É a vez do jogador ", self.__jogadores[self.__turno].nome)
        return self.__jogadores[self.__turno].id
    
root = Tk()
app = AppTeste(root)
root.mainloop()

##teste branch nova