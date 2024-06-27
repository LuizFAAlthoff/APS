from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk
from time import sleep
from tabuleiro import Tabuleiro


class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self, window: Window):
        self.dog_server_interface = DogActor()
        self.window = window.getWindow()
        self.window.title("Rainbow Cards")
        self.bloqueado = False
        self.start_menu()
        self.tabuleiro = Tabuleiro()

    def criar_tela_principal(self):
        largura_janela = 1280
        altura_janela = 720
        janela = self.criar_janela_centralizada("Rainbow Cards", largura_janela, altura_janela)
        self.design_tela_principal(janela, largura_janela, altura_janela)

        janela.mainloop()

    def criar_janela_centralizada(self, title, largura_janela, altura_janela):
        janela = Tk()
        janela.title(title)
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)
        janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        return janela

    def design_tela_principal(self, janela, largura_janela, altura_janela):
        imagem_de_fundo = ImageTk.PhotoImage(Image.open("menu_images/rainbow_bg.png"))
    #     canvas = Canvas(janela, width=largura_janela, height=altura_janela)
    #     canvas.pack(fill="both", expand=True)
    #     canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

    #     # Necessário para manter uma referência à imagem
    #     self.imagem_de_fundo = imagem_de_fundo

    #     frame_jogador2 = Frame(canvas, bg="#a5b942")
    #     frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
    #     texto_jogador2 = Label(frame_jogador2, text="Jogador 2\n teste\n 3 cartas", bg="#a5b942")
    #     texto_jogador2.pack(pady=10)

    #     frame_jogador3 = Frame(canvas, bg="#a5b942")
    #     frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
    #     texto_jogador3 = Label(frame_jogador3, text="Jogador 3\n teste\n 5 cartas", bg="#a5b942")
    #     texto_jogador3.pack(pady=10)

    #     frame_contador = Frame(canvas, bg="#b5b942")
    #     frame_contador.place(relwidth=0.2, relheight=0.3, relx=0.05, rely=0.35)
    #     texto_contador = Label(frame_contador, text="Contador +1\n 6", bg="#b5b942")
    #     texto_contador.pack(pady=10)

    #     #problemas aqui. Não consigo fazer a imagem aparecer não importa o que eu faça. O melhor que ocorre é um quadrado branco
    #     frame_central = Frame(canvas, bg="#b5b942")
    #     frame_central.place(relwidth=0.5, relheight=0.3, relx=0.3, rely=0.35)
    #     #import da imagem
    #     image_original_carta = Image.open("cartas/1-amarelo-anil.jpeg").resize((100, 100))
    #     image_tk_carta = ImageTk.PhotoImage(image_original_carta)
    #     #widget
    #     label_carta = Label(frame_central, image=image_tk_carta)
    #     label_carta.pack()

    #     frame_botoes = Frame(canvas, bg="#b5b942")
    #     frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.4)
    #     botao_comprar = Button(frame_botoes, text="Comprar Carta")
    #     botao_comprar.place(relx=0.5, rely=0.3, anchor="center")
    #     botao_passar_turno = Button(frame_botoes, text="Passar Turno")
    #     botao_passar_turno.place(relx=0.5, rely=0.7, anchor="center")

    #     frame_cartas = Frame(canvas, bg="#c5b942")
    #     frame_cartas.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.7)

    #     canvas_cartas = Canvas(frame_cartas, width=largura_janela, height=altura_janela//3)
    #     canvas.create_image(0, 0, image=ImageTk.PhotoImage(Image.open("menu_images/canvas_cartas.png")), anchor="e")
    #     canvas_cartas.pack(side = LEFT, fill="both", expand=True)

    #     scrollbar = Scrollbar(canvas_cartas, orient="horizontal", command=canvas_cartas.xview)
    #     scrollbar.pack(anchor= "s", fill="x")
    #     canvas_cartas.configure(xscrollcommand=scrollbar.set)

    # def comprar_carta():
    #     messagebox.showinfo("Ação", "Carta comprada")

    # def realizar_jogada():
    #     messagebox.showinfo("Ação", "Jogada realizada")








    # def receive_move(self, a_move: dict):
    #     if a_move["type"] == "init":
    #         pass
    #     elif a_move["type"] == "block":
    #         pass
    #     elif a_move["type"] == "draw":
    #         pass
    #     elif a_move["type"] == "pass":
    #         pass
    #     elif a_move["type"] == "end":
    #         pass

    def receive_start(self, start_status):
        #self.tabuleiro.set_local_id(start_status.get_local_id())
        self.set_canvas()
        self.tela_partida_design()
    
    def receive_withdrawal_notification(self):
        self.show_screen_disconnect()
    
    def start_match(self):
        start_status = self.__dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

        if message == 'Partida iniciada':
            jogadores = start_status.get_players()
            id_jogador_local = start_status.get_local_id()
            messagebox.showinfo('esta dentro da funcao start match')
            dict_inicial = self.tabuleiro.comecar_partida(jogadores, id_jogador_local)
            
            self.set_canvas()
            self.tela_partida_design()

    def tela_partida_design(self):
        imagem_de_fundo = ImageTk.PhotoImage(Image.open("src/menu_images/rainbow_bg.png"))
        self.canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

        frame_jogador2 = Frame(self.canvas, bg="#a5b942")
        frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
        texto_jogador2 = Label(frame_jogador2, text="Jogador 2\n teste\n 3 cartas", bg="#a5b942")
        texto_jogador2.pack(pady=10)

        frame_jogador3 = Frame(self.canvas, bg="#a5b942")
        frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
        texto_jogador3 = Label(frame_jogador3, text="Jogador 3\n teste\n 5 cartas", bg="#a5b942")
        texto_jogador3.pack(pady=10)

        frame_contador = Frame(self.canvas, bg="#b5b942")
        frame_contador.place(relwidth=0.1, relheight=0.2, relx=0.05, rely=0.4)
        texto_contador = Label(frame_contador, text="Contador +1\n 6", bg="#b5b942")
        texto_contador.pack(pady=10)

        frame_central = Frame(self.canvas, bg="#b5b942")
        frame_central.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.35)
        label_carta = Label(frame_central)
        label_carta.pack(expand=True)

        frame_botoes = Frame(self.canvas, bg="#b5b942")
        frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.4)
        botao_comprar = Button(frame_botoes, text="Comprar Carta", command=self.comprar_carta)
        botao_comprar.place(relx=0.5, rely=0.2, anchor="center")
        botao_passar_turno = Button(frame_botoes, text="Passar Turno", command=self.passar_turno)
        botao_passar_turno.place(relx=0.5, rely=0.5, anchor="center")
        botao_carta_aleatoria = Button(frame_botoes, text="Carta Aleatória", command=self.show_random_card(label_carta))
        botao_carta_aleatoria.place(relx=0.5, rely=0.8, anchor="center")

        frame_cartas = Frame(self.canvas, bg="#c5b942")
        frame_cartas.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.7)

    def show_random_card(self, label_carta: Label):
        carta = self.tabuleiro.get_random_card()
        image_path = carta.get_card_image()
        image = Image.open(image_path)
        image = image.resize((256//3, 345//3), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label_carta.config(image=photo)
        label_carta.image = photo



            # dict_inicial = self.__jogo.comecarPartida(jogadores, id_jogador_local)
            # self.__dog_server_interface.send_move(dict_inicial)

            # self.__jogo.configurarJogadores()
            # self.__mensagem = self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getNome()
            # self.start_table()
    
    def comprar_carta(self):
        messagebox.showinfo("está no metodo comprar_carta", "Comprou X carta(s)")

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

    # def load_cards(self):
    #     cor_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
    #     cor_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
    #     dict_of_cards = {}

        # for cor_primaria in cor_primaria:
        #     for cor_secundaria in cor_secundaria:
        #         for numero in range(1, 3):
        #             image = Image.open(f'src/cartas/{numero}-{cor_primaria}-{cor_secundaria}.jpeg')
        #             img = image.resize((100, 150))
        #             dict_of_cards[f"{numero}-{cor_primaria}-{cor_secundaria}.jpeg"] = ImageTk.PhotoImage(img)
        #             x=1
