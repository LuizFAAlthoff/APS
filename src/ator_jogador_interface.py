from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk
from time import sleep
from tabuleiro import Tabuleiro
from baralho import Baralho
from carta_especial import CartaEspecial
from carta_normal import CartaNormal
from jogada import Jogada
import customtkinter


class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self, window: Window):
        self.dog_server_interface = DogActor()
        self.window = window.getWindow()
        self.window.title("Rainbow Cards")
        self.bloqueado = False
        self.tabuleiro  = Tabuleiro(Baralho())
        self.dict_cards = {}
        self.dict_frames = {}
        self.dict_btn_cartas = []
        self.criar_tkinter_images()
        self.start_menu()


    def receive_start(self, start_status):
        self.tabuleiro.set_local_id(start_status.get_local_id())
        self.set_canvas()
        # self.tela_partida_design()

    def receive_move(self, a_move: dict):
        if a_move["type"] == "init":
            print(a_move)
            self.tabuleiro.atualizar_jogadores(a_move) 
            self.tabuleiro.atualizar_tabuleiro(a_move)
            self.tela_partida_design()
        elif a_move["type"] == "block":
            pass
        elif a_move["type"] == "draw":
            pass
        elif a_move["type"] == "pass":
            pass
        elif a_move["type"] == "end":
            pass
        # elif a_move["type"] == "+1": ===> CRIAR UM TIPO DE JOGADA MAIS UM PARA CRIAR VERIFICACAO DE QUANDO JOGADOR TEM QUE COMPRAR O CONTADOR
        #     pass
    
    def receive_withdrawal_notification(self):
        self.show_screen_disconnect()
    
    def start_match(self):
        start_status = self.__dog_server_interface.start_match(3)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

        if message == 'Partida iniciada':
            jogadores = start_status.get_players()
            id_jogador_local = start_status.get_local_id()
            dict_inicial =  self.tabuleiro.comecar_partida(jogadores, id_jogador_local)
            self.__dog_server_interface.send_move(dict_inicial)
            # self.__jogo.configurarJogadores()
            # self.__mensagem = self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getNome()
            self.set_canvas()
            self.tela_partida_design()
            x=1

    # def add_contador_cartas_mais_um(self):
    #     self.valor_contador += 1
    #     # self.canvas.delete("all")
    #     # self.tela_partida_design()

    def tela_partida_design(self): # algumas coisas nesse metodo so devem ocorrer caso seja inicio do jogo
        imagem_de_fundo = self.dict_cards['rainbow_bg']
        self.canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

        frame_jogador2 = Frame(self.canvas, bg="#a5b942")
        frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
        texto_jogador2 = Label(frame_jogador2, text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_dois].nome} \n {len(self.tabuleiro.jogadores[self.tabuleiro.jogador_dois].mao)} cartas", bg="#a5b942")
        texto_jogador2.pack(pady=10)
        self.dict_frames["jogador2"] = frame_jogador2
        
        frame_jogador_local = customtkinter.CTkScrollableFrame(master=self.canvas, orientation="horizontal", label_text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_local].nome} \n {len(self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao)} cartas", fg_color="#a5b942")
        frame_jogador_local.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.7)

        self.dict_frames["jogador_local"] = frame_jogador_local

        frame_jogador3 = Frame(self.canvas, bg="#a5b942")
        frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
        texto_jogador3 = Label(frame_jogador3, text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_tres].nome} \n {len(self.tabuleiro.jogadores[self.tabuleiro.jogador_tres].mao)} cartas", bg="#a5b942")
        texto_jogador3.pack(pady=10)
        self.dict_frames["jogador3"] = frame_jogador3

        frame_contador = Frame(self.canvas, bg="#b5b942")
        frame_contador.place(relwidth=0.1, relheight=0.2, relx=0.05, rely=0.4)
        texto_contador = Label(frame_contador, text=f"Contador +1 \n {self.tabuleiro.contador_cartas_mais_um}", bg="#b5b942")
        texto_contador.pack(pady=10)
        self.dict_frames["frame_contador"] = frame_contador


        if self.tabuleiro.ultima_carta == None: # significa que é a primeira jogada
            self.tabuleiro.ultima_carta = self.tabuleiro.baralho.get_carta_normal_aleatoria()
        frame_central = customtkinter.CTkFrame(master=self.canvas, fg_color="#b5b942")
        frame_central.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.35)
        label_carta = customtkinter.CTkLabel(master=frame_central, image=self.dict_cards[self.cria_chave_para_ultima_carta()], text="")
        label_carta.pack(expand=True)
        self.dict_frames["frame_central"] = frame_central
        

        frame_botoes = Frame(self.canvas, bg="#b5b942")
        frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.4)
        botao_comprar = Button(frame_botoes, text="Comprar Carta", command=self.comprar_carta) 
        botao_comprar.place(relx=0.5, rely=0.2, anchor="center")
        botao_passar_turno = Button(frame_botoes, text="Passar Turno") #command=self.passar_turno()) -> adicionar so quando tiver realmente a funcionalidade 
        botao_passar_turno.place(relx=0.5, rely=0.5, anchor="center")
        self.dict_frames["frame_botoes"] = frame_botoes
        
        self.adiciona_cartas_iniciais_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_local], frame_jogador_local)
        self.adiciona_cartas_iniciais_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_dois], frame_jogador2)
        self.adiciona_cartas_iniciais_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_tres], frame_jogador3)

    # def add_contador_cartas_mais_um(self):
    #     self.tabuleiro.add_contador_cartas_mais_um()
    #     self.valor_contador = self.tabuleiro.contador_cartas_mais_um
    
    def adiciona_cartas_iniciais_ao_jogador_design(self, jogador, frame):
        cartas_mao = jogador.mao 
        if jogador.id == self.tabuleiro.local_id:
            for carta in cartas_mao:
                if carta.cor_primaria == 'preto':
                    imagem = f'{carta.tipo}'
                    btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.jogar(c))   
                    btn.carta = carta
                    self.dict_btn_cartas.append(btn)

                else:
                    imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                    btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.jogar(c))
                    btn.carta = carta
                    self.dict_btn_cartas.append(btn)
                btn.pack(side="left", padx=10, pady=5, anchor="center")
        else:
            imagem = Label(frame, image=self.dict_cards['fundo_carta'], padx=50)
            imagem.pack(side="left", padx=10, pady=5,anchor="center") 


    def adiciona_cartas_compradas_ao_jogador_design(self, lista_cartas_compradas, frame):
        for carta in lista_cartas_compradas:
            if carta.cor_primaria == 'preto':
                imagem = f'{carta.tipo}'
                btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.jogar(c))  
            else:
                imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.jogar(c))  
            btn.pack(side="left", padx=10, pady=5, anchor="center")                    


    def comprar_carta(self):
        if isinstance(self.tabuleiro.ultima_carta, CartaEspecial):
            if self.tabuleiro.ultima_carta.tipo == 'mais-um':
                if self.tabuleiro.ultima_carta.ja_satisfeita == False:
                    cartas_compradas = []
                    for _ in range(self.tabuleiro.contador_cartas_mais_um):
                        carta_comprada = self.tabuleiro.baralho.get_carta_aleatoria()
                        self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao.append(carta_comprada)
                        cartas_compradas.append(carta_comprada)
                    self.tabuleiro.ultima_carta.ja_satisfeita = True
                    self.adiciona_cartas_compradas_ao_jogador_design(cartas_compradas, self.dict_frames["jogador_local"])
        else:
            cartas_compradas = []
            carta_comprada = self.tabuleiro.baralho.get_carta_aleatoria()
            self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao.append(carta_comprada)
            cartas_compradas.append(carta_comprada)
            self.adiciona_cartas_compradas_ao_jogador_design(cartas_compradas, self.dict_frames["jogador_local"])


    def passar_turno(self):
       self.tabuleiro.jogadores[self.tabuleiro.jogador_atual + 1]

    def jogar(self, carta):
        # ao entrar nessa função, carta é a carta que foi clicada pelo usuario na interface
        #precisa implementar logica para encadeamento de cartas
        print(carta)


    def set_canvas(self): #DEFINE UMA ÁREA RETANGULAR NA TELA PARA MOSTRAR OS COMPONENTES DA INTERFACE
        self.canvas = Canvas(
            self.window,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def create_menu_design(self): #MUDAR NOME DE FUNÇÃO
        self.background_img = PhotoImage(file = f"src/menu_images/background.png")
        background = self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
        self.button_menu = PhotoImage(file = f"src/menu_images/img0.png")
        button_start = self.canvas.create_image(270, 570, image=self.button_menu)
        self.canvas.tag_bind(button_start, "<Button-1>", lambda x: self.start_match())
        x=1

    def start_menu(self) -> None:
        self.set_canvas() 
        self.create_menu_design()
        self.window.resizable(False, False)
        player_name = simpledialog.askstring(title='player indentification', prompt= 'Qual seu nome?')
        self.__dog_server_interface = DogActor()
        message = self.__dog_server_interface.initialize(player_name,self)
        messagebox.showinfo(message=message)
        self.window.mainloop()

    def show_screen_disconnect(self):
        # self.__jogo.setFimJogo(True) setter de atributos da classe jogo do flip
        # self.__jogo.setJogoAbandonado(True) setter de atributos da classe jogo do flip
        self.set_canvas()
        self.background_img = PhotoImage(file = f"src/menu_images/desconexao.png")
        background = self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
        sleep(3)
        self.window.destroy()

    def criar_tkinter_images(self):
        for carta in self.tabuleiro.baralho.cartas:
            nome_imagem = ''
            if isinstance(carta, CartaNormal): 
                nome_imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                imagem = customtkinter.CTkImage(Image.open(f'src/cartas/{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}.png'), size=(100, 150))
            else:
                nome_imagem = f'{carta.tipo}'
                imagem = customtkinter.CTkImage(Image.open(f'src/cartas/{carta.tipo}.png'), size=(100, 150))
            self.dict_cards[f"{nome_imagem}"] = imagem

            image_background = Image.open(f'src/menu_images/rainbow_bg.png')
            self.dict_cards[f"rainbow_bg"] = ImageTk.PhotoImage(image_background)

            fundo_carta = Image.open(f'src/menu_images/fundo_carta.jpeg')
            self.dict_cards[f"fundo_carta"] = ImageTk.PhotoImage(fundo_carta)
    
    def cria_chave_para_ultima_carta(self):
        if isinstance(self.tabuleiro.ultima_carta, CartaNormal):
            return  f'{self.tabuleiro.ultima_carta.numero}-{self.tabuleiro.ultima_carta.cor_primaria}-{self.tabuleiro.ultima_carta.cor_secundaria}'
        return f'{self.tabuleiro.ultima_carta.tipo}'