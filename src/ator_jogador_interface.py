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

    def receive_move(self, a_move: dict):
        if a_move["type"] == "init":
            pass
        elif a_move["type"] == "block":
            pass
        elif a_move["type"] == "draw":
            pass
        elif a_move["type"] == "pass":
            pass
        elif a_move["type"] == "end":
            pass

    def receive_start(self, start_status):
        self.tabuleiro.setLocalId(start_status.get_local_id())
    
    def receive_withdrawal_notification(self):
        self.showScreenDisconnect()
    
    def start_match(self):
        start_status = self.__dog_server_interface.start_match(1)
        message = start_status.get_message()
        messagebox.showinfo(message=message)


        if message == 'Partida iniciada':
            jogadores = start_status.get_players()
            id_jogador_local = start_status.get_local_id()
            
            dict_inicial = self.__jogo.comecarPartida(jogadores, id_jogador_local)
            self.__dog_server_interface.send_move(dict_inicial)

            self.__jogo.configurarJogadores()
            self.__mensagem = self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getNome()
            self.start_table()
    
    def set_canvas(self): #DEFINE UMA ÁREA RETANGULAR NA TELA PARA MOSTRAR OS COMPONENTES DA INTERFACE
        self.canvas = Canvas(
            self.window,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def create_menu_design(self): #MUDAR NOME DE FUNÇÃO
        self.background_img = PhotoImage(file = f"menu_images/background.png")
        background = self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
        self.button_menu = PhotoImage(file = f"menu_images/img0.png")
        button_start = self.canvas.create_image(270, 570, image=self.button_menu)
        self.canvas.tag_bind(button_start, "<Button-1>", lambda x: self.start_match())

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

    def load_cards(self):
        cor_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
        cor_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
        dict_of_cards = {}

        for cor_primaria in cor_primaria:
            for cor_secundaria in cor_secundaria:
                for numero in range(1, 3):
                    image = Image.open(f'cartas/{numero}-{cor_primaria}-{cor_secundaria}.jpeg')
                    img = image.resize((100, 150))
                    dict_of_cards[f"{numero}-{cor_primaria}-{cor_secundaria}.jpeg"] = ImageTk.PhotoImage(img)
                    x=1

