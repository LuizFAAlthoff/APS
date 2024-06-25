from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk

class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self, window: Window):
        self.dog_server_interface = DogActor()
        self.window = window.getWindow()
        self.window.title("Rainbow Cards")
        self.bloqueado = False
        self.start_menu()

    def start_menu(self) -> None:
        self.set_canvas() 
        x=1
        self.create_menu_design()
        self.window.resizable(False, False)
        player_name = simpledialog.askstring(title='player indentification', prompt= 'Qual seu nome?')
        self.__dog_server_interface = DogActor()
        message = self.__dog_server_interface.initialize(player_name,self)
        messagebox.showinfo(message=message)
        self.window.mainloop()

    def set_canvas(self): #DEFINE UMA ÁREA RETANGULAR NA TELA PARA MOSTRAR OS COMPONENTES DA INTERFACE
        self.canvas = Canvas(self.window,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(relx=0.5,rely=0.5,anchor=CENTER)

    def create_menu_design(self): #MUDAR NOME DE FUNÇÃO
        self.background_img = PhotoImage(file = f"menu_images/background.png")
        self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
        self.button_menu = PhotoImage(file = f"menu_images/img0.png")
        button_start = self.canvas.create_image(270, 570, image=self.button_menu)
        self.canvas.tag_bind(button_start, "<Button-1>", lambda x: self.start_match())

    def start_match(self):
        start_status = self.__dog_server_interface.start_match(1)
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        if message == 'Partida iniciada':
            self.tela_principal()

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

    # def receive_start(self, start_status):
    #     self.tabuleiro.setLocalId(start_status.get_local_id())
    
    # def receive_withdrawal_notification(self):
    #     self.showScreenDisconnect()
    
    #     if message == 'Partida iniciada':
    #         jogadores = start_status.get_players()
    #         id_jogador_local = start_status.get_local_id()
            
    #         dict_inicial = self.__jogo.comecarPartida(jogadores, id_jogador_local)
    #         self.__dog_server_interface.send_move(dict_inicial)

    #         self.__jogo.configurarJogadores()
    #         self.__mensagem = self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getNome()
    #         self.start_table()

    # def load_cards(self):
    #     cor_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
    #     cor_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
    #     dict_of_cards = {}

    #     for cor_primaria in cor_primaria:
    #         for cor_secundaria in cor_secundaria:
    #             for numero in range(1, 3):
    #                 image = Image.open(f'cartas/{numero}-{cor_primaria}-{cor_secundaria}.jpeg')
    #                 img = image.resize((100, 150))
    #                 dict_of_cards[f"{numero}-{cor_primaria}-{cor_secundaria}.jpeg"] = ImageTk.PhotoImage(img)
    #                 x=1

    def tela_principal(self):
        def centralizar_janela(root, largura_janela, altura_janela):
            # Obtém a largura e a altura do monitor/tela
            largura_tela = root.winfo_screenwidth()
            altura_tela = root.winfo_screenheight()

            # Calcula a posição x e y para centralizar a janela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            # Define a geometria da janela (largura x altura + posição x + posição y)
            root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        def comprar_carta():
            messagebox.showinfo("Ação", "Carta comprada")

        def realizar_jogada():
            messagebox.showinfo("Ação", "Jogada realizada")

        # Função para configurar a barra de rolagem horizontal
        def configurar_scrollbar(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Cria a instância da janela principal
        root = Tk()

        # Define o título da janela
        root.title("Rainbow Cards Partida")

        # Define o tamanho da janela
        largura_janela = 1280
        altura_janela = 720

        # Centraliza a janela na tela
        centralizar_janela(root, largura_janela, altura_janela)

        # Calcula a altura de cada frame
        altura_frame = altura_janela // 3

        # Cria os três frames
        frame1 = Frame(root, bg="#f5b942", width=largura_janela, height=altura_frame)
        frame2 = Frame(root, bg="#a5b942", width=largura_janela, height=altura_frame)
        frame3 = Frame(root, bg="#d5b942", width=largura_janela, height=altura_frame)

        # Posiciona os frames na janela usando pack
        frame1.pack(fill="both")
        frame2.pack(fill="both")
        frame3.pack(fill="both")

        # Calcula a largura de cada subframe no frame do meio
        largura_subframe = largura_janela // 3

        # Cria os três subframes dentro do frame do meio
        subframe1 = Frame(frame2, bg="#f5c942", width=largura_subframe*1/5, height=altura_frame)
        subframe2 = Frame(frame2, bg="#a5b942", width=largura_subframe*3/5, height=altura_frame)
        subframe3 = Frame(frame2, bg="#f5a942", width=largura_subframe*1/5, height=altura_frame)

        # Posiciona os subframes no frame do meio usando pack com side="left"
        subframe1.pack(side="left", fill="both", expand=True)
        subframe2.pack(side="left", fill="both", expand=True)
        subframe3.pack(side="left", fill="both", expand=True)

        # Adiciona a palavra "contador" e o número 1 abaixo dela no subframe1
        label_contador = Label(subframe1, text="contador", bg="#f5c942")
        label_contador.pack(pady=10)
        label_numero = Label(subframe1, text="1", bg="#f5c942")
        label_numero.pack()

        # Adiciona uma imagem no subframe2
        # Carrega a imagem (substitua 'caminho_para_imagem.png' pelo caminho da sua imagem)
        imagem = Image.open("cartas/1-amarelo-anil.jpeg")
        imagem = imagem.resize((largura_subframe, altura_frame), Image.ANTIALIAS)
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem = Label(subframe2, image=imagem_tk, bg="#a5b942")
        label_imagem.pack(expand=True)

        # Adiciona os botões no subframe3
        btn_comprar = Button(subframe3, text="Comprar Carta", command=comprar_carta)
        btn_comprar.pack(pady=10)
        btn_jogada = Button(subframe3, text="Realizar Jogada", command=realizar_jogada)
        btn_jogada.pack(pady=10)

        # Lista de cartas do jogador
        cartas = ["Carta 1", "Carta 2", "Carta 3", "Carta 4", "Carta 5", "Carta 6", "Carta 7", "Carta 8", "Carta 9", "Carta 10"]

        # Cria um canvas no frame de baixo
        canvas = Canvas(frame3, bg="#0000FF", width=largura_janela, height=altura_frame)
        canvas.pack(side="left", fill="both", expand=True)

        # Frame interno para adicionar widgets ao canvas
        buttons_frame = Frame(canvas)
        buttons_frame.pack(side="bottom")

        # Adiciona botões para cada carta no frame interno, com espaçamento entre eles
        x_position = 10  # Posição inicial dos botões no eixo x

        for carta in cartas:
            btn = Button(canvas, text=carta, padx=50, pady=80)
            btn.pack(side="left", padx=10, pady=10, anchor="center")
            x_position += 100

        # Adiciona uma barra de rolagem horizontal ao canvas
        scrollbar = Scrollbar(frame3, orient="horizontal", command=canvas.xview)
        scrollbar.pack(side="bottom", fill="x")

        # Configura o canvas para usar a barra de rolagem
        canvas.configure(xscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda event, canvas=canvas: configurar_scrollbar())

        # Mantém a janela aberta
        root.mainloop()