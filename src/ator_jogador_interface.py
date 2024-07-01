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


class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self, window: Window):
        self.dog_server_interface = DogActor()
        self.window = window.getWindow()
        self.window.title("Rainbow Cards")
        self.bloqueado = False
        self.tabuleiro  = Tabuleiro(Baralho())
        self.dict_cards = {}
        self.criar_tkinter_images()
        self.start_menu()
        self.valor_contador = 0
        print(self.valor_contador)

    def receive_start(self, start_status):
        self.tabuleiro.set_local_id(start_status.get_local_id())
        self.set_canvas()
        # self.tela_partida_design()

    def receive_move(self, a_move: dict):
        if a_move["type"] == "init":
            print(a_move)
            self.tabuleiro.atualizar_jogadores(a_move)
            self.tela_partida_design()
            # regra para atualizar o tabuleiro dos jogadores 
        elif a_move["type"] == "block":
            pass
        elif a_move["type"] == "draw":
            pass
        elif a_move["type"] == "pass":
            pass
        elif a_move["type"] == "end":
            pass
    
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

    def add_contador_cartas_mais_um(self):
        self.valor_contador += 1
        # self.canvas.delete("all")
        # self.tela_partida_design()

    def tela_partida_design(self):
        imagem_de_fundo = self.dict_cards['rainbow_bg']
        self.canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

        frame_jogador2 = Frame(self.canvas, bg="#a5b942")
        frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
        texto_jogador2 = Label(frame_jogador2, text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_dois].nome}", bg="#a5b942")
        texto_jogador2.pack(pady=10)

        frame_jogador_local = Frame(self.canvas, bg="#a5b942")
        frame_jogador_local.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.7)
        label_jogador_local = Label(frame_jogador_local, text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_local].nome}", bg="#a5b942")
        label_jogador_local.pack(pady=10)

        frame_jogador3 = Frame(self.canvas, bg="#a5b942")
        frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
        texto_jogador3 = Label(frame_jogador3, text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_tres].nome}", bg="#a5b942")
        texto_jogador3.pack(pady=10)

        frame_contador = Frame(self.canvas, bg="#b5b942")
        frame_contador.place(relwidth=0.1, relheight=0.2, relx=0.05, rely=0.4)
        texto_contador = Label(frame_contador, text="Contador +1", bg="#b5b942")
        texto_contador.pack(pady=10)
        botao_add_contador = Button(frame_contador, text=f"{self.tabuleiro.contador_cartas_mais_um}", command=self.tabuleiro.contador_cartas_mais_um)
        botao_add_contador.pack(pady=10)

        frame_central = Frame(self.canvas, bg="#b5b942")
        frame_central.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.35)

        label_carta = Label(frame_central, image=self.dict_cards['1-amarelo-anil'])
        label_carta.pack(expand=True)

        frame_botoes = Frame(self.canvas, bg="#b5b942")
        frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.4)
        botao_comprar = Button(frame_botoes, text="Comprar Carta", command=self.comprar_carta)
        botao_comprar.place(relx=0.5, rely=0.2, anchor="center")
        botao_passar_turno = Button(frame_botoes, text="Passar Turno", command=self.passar_turno)
        botao_passar_turno.place(relx=0.5, rely=0.5, anchor="center")
        botao_carta_aleatoria = Button(frame_botoes, text="Carta Aleatória")
        botao_carta_aleatoria.place(relx=0.5, rely=0.8, anchor="center")

        self.adiciona_carta_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_local], frame_jogador_local)
        self.adiciona_carta_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_dois], frame_jogador2)
        self.adiciona_carta_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_tres], frame_jogador3)

    # def add_contador_cartas_mais_um(self):
    #     self.tabuleiro.add_contador_cartas_mais_um()
    #     self.valor_contador = self.tabuleiro.contador_cartas_mais_um
    
    def adiciona_carta_ao_jogador_design(self, jogador, frame):
        cartas_mao = jogador.mao 
        x=1
        #verificar se jogador.id é o jogador local para colocar imagem das costas da carta para J2 e J3
        if jogador.id == self.tabuleiro.local_id:
            for carta in cartas_mao:
                if carta.cor_primaria == 'preto':
                    imagem = f'{carta.tipo}'
                    btn = Button(frame, image=self.dict_cards[imagem], padx=50, pady=80)    #sugestão: adicionar 'command = self.realizar_jogada(CartaEspecial(carta.cor_primaria, carta.tipo))'
                else:
                    imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                    btn = Button(frame, image=self.dict_cards[imagem], padx=50, pady=80)    #sugestão: adicionar 'command = self.realizar_jogada(CartaNormal(carta.cor_primaria, carta.cor_secundaria, carta.numero))'
                btn.pack(side="left", padx=10, pady=10, anchor="center")                    #dessa forma, ao clicar na carta, a função realizar_jogada é chamada com a carta correspondente, levando um objeto do tipo carta correspondente como parâmetro
        else:
            imagem = Label(frame, image=self.dict_cards['fundo_carta'], padx=50, pady=80)
            imagem.pack(side="left", padx=10, pady=10, anchor="center") 

    

    def comprar_carta(self):
        messagebox.showinfo("está no metodo comprar_carta", "Olhe o terminal")
        if isinstance(self.tabuleiro.ultima_carta, CartaNormal):
            objeto_cartas_aleatoria = self.tabuleiro.baralho.get_carta_aleatoria()
            self.tabuleiro.jogadores[self.tabuleiro.jogador_local].add_cartas_na_mao(objeto_cartas_aleatoria)
            #não sei muito bem como adicionar a carta visualmente?? pensei em invocar o adicionar_carta_ao_jogador_design, mas teria que
            # passar como parâmetro o frame_jogador_local, mas acho que ele só existe localmente dentro do método tela_partida_design, então acho que
            #  não daria certo. Por isso ainda estou usando prints no console para ver se a carta foi adicionada ao jogador local

            # as duas linhas abaixo são para ajudar a debugar
            self.tabuleiro.jogadores[self.tabuleiro.jogador_local].print_cartas()
            print("comprou carta: ", objeto_cartas_aleatoria.cor_primaria, objeto_cartas_aleatoria.cor_secundaria, objeto_cartas_aleatoria.numero)
        elif isinstance(self.tabuleiro.ultima_carta, CartaEspecial) and self.tabuleiro.ultima_carta.tipo == 'mais-um':
                self.tabuleiro.jogadores[self.tabuleiro.jogador_local].print_cartas()
                messagebox.showinfo(" ", f"Comprou {self.tabuleiro.contador_cartas_mais_um} cartas")
                for _ in range(self.tabuleiro.contador_cartas_mais_um):
                    objeto_cartas_aleatoria = self.tabuleiro.baralho.get_carta_aleatoria()
                    self.tabuleiro.jogadores[self.tabuleiro.jogador_local].add_cartas_na_mao(objeto_cartas_aleatoria)
                    print("comprou carta: ", objeto_cartas_aleatoria.cor_primaria, objeto_cartas_aleatoria.cor_secundaria, objeto_cartas_aleatoria.numero)

    def passar_turno(self):
        messagebox.showinfo("está no metodo passar_turno", "Passou o turno")

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
            else:
                nome_imagem = f'{carta.tipo}'
            image = Image.open(f'src/cartas/{nome_imagem}.jpeg')
            img = image.resize((100, 150))
            self.dict_cards[f"{nome_imagem}"] = ImageTk.PhotoImage(img)
            image_background = Image.open(f'src/menu_images/rainbow_bg.png')
            self.dict_cards[f"rainbow_bg"] = ImageTk.PhotoImage(image_background)
            fundo_carta = Image.open(f'src/menu_images/fundo_carta.jpeg')
            self.dict_cards[f"fundo_carta"] = ImageTk.PhotoImage(fundo_carta)