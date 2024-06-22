from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from window import Window
from dog.dog_actor import DogActor

class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self, window: Window):
        self.dog_server_interface = DogActor()
        self.window = window.getWindow()
        self.window.title("Rainbow Cards")
        self.bloqueado = False

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
        start_status = self.dog_server_interface.start_match(3)
        message = start_status.get_message()
        messagebox.showinfo(message)

        if message == 'Partida iniciada':
           players = start_status.get_players()
           id_jogador_local = start_status.get_local_id()
           
           dict_initial = self.__jogo.comecarPartida(players, id_jogador_local)
           self.__dog_server_interface.send_move(dict_initial)

           self.__jogo.configurarJogadores()
           self.__mensagem = self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getNome()
           self.start_table()
    
    def set_canvas(self): #DEFINE UMA ÁREA RETANGULAR NA TELA PARA MOSTRAR OS COMPONENTES DA INTERFACE
        self.canvas = Canvas(self.window, width=1280, height=720, bg="#ffffff")
        self.canvas.place(x=0, y=0, anchor=CENTER)
    
    def create_menu_design(self): #MUDAR NOME DE FUNÇÃO
        self.__background_img = PhotoImage(file = f"src/menu_images/background.png")
        background = self.__canvas.create_image(0, 0,image=self.__background_img,anchor="nw")
        self.__button_menu = PhotoImage(file = f"src/menu_images/img0.png")
        button_start = self.__canvas.create_image(270, 570, image=self.__button_menu)
        self.__canvas.tag_bind(button_start, "<Button-1>", lambda x: self.start_match())

    def start_menu(self) -> None:
        self.setCanvas() 
        self.createMenuDesign()
        self.__window.resizable(False, False)
        player_name = simpledialog.askstring(title='player indentification', prompt= 'Qual seu nome?')
        self.__dog_server_interface = DogActor()
        message = self.__dog_server_interface.initialize(player_name,self)
        messagebox.showinfo(message=message)
        self.__window.mainloop()