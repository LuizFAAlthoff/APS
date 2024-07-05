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
        self.tabuleiro  = Tabuleiro(Baralho())
        self.dict_cards = {}
        self.dict_frames = {}
        self.dict_btn_cartas = {}
        self.criar_tkinter_images()
        self.start_menu()


    def receive_start(self, start_status):
        self.tabuleiro.set_local_id(start_status.get_local_id())
        self.set_canvas()

    def receive_move(self, a_move: dict):
        if a_move["type"] == "init":
            self.tabuleiro.atualizar_jogadores(a_move) 
            self.tabuleiro.atualizar_cartas_tabuleiro(a_move)
            self.tela_partida_design()

        elif a_move["type"] == "bloquear":
            self.tabuleiro.jogador_atual = a_move["jogador_atual"]
            self.tabuleiro.atualizar_cartas_tabuleiro(a_move)
            self.tabuleiro.atualizar_jogadores(a_move) 
            self.tabuleiro.bloqueado = True
            self.tela_partida_design()
            if self.tabuleiro.jogador_atual == self.tabuleiro.jogador_local:
                messagebox.showwarning("Atenção", "Você foi bloqueado, passe o turno")

        elif a_move["type"] == "mais-um":
            self.tabuleiro.precisa_comprar_contador = True
            self.tabuleiro.jogador_atual = a_move["jogador_atual"]
            self.tabuleiro.atualizar_cartas_tabuleiro(a_move)
            self.tabuleiro.atualizar_jogadores(a_move) 
            self.tela_partida_design()
            
        elif a_move["type"] == "passar_turno":
            self.tabuleiro.precisa_comprar_contador = a_move["precisa_comprar_contador"]
            self.tabuleiro.bloqueado =  a_move["bloqueado"]
            self.tabuleiro.jogador_atual = a_move["jogador_atual"]
            self.tabuleiro.atualizar_cartas_tabuleiro(a_move)
            self.tabuleiro.atualizar_jogadores(a_move) 
            self.tela_partida_design()

        elif a_move["type"] == "vitoria":
            jogador_atual = a_move["jogador_atual"]
            msg = f"O Jogador {self.tabuleiro.jogadores[(jogador_atual -1) % 3].nome} ganhou"
            messagebox.showinfo("Vitória", msg)
            self.tela_partida_design()

 
    
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
            self.set_canvas()
            self.tela_partida_design()
            x=1


    def tela_partida_design(self):
        imagem_de_fundo = self.dict_cards['rainbow_bg']
        self.canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

        frame_jogador_local = customtkinter.CTkScrollableFrame(master=self.canvas, orientation="horizontal", label_text=f"{self.tabuleiro.jogadores[self.tabuleiro.jogador_local].nome}\n{len(self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao)} cartas",label_fg_color="#b5b942", label_text_color="white",label_font=("helvetica", 20, "bold"), fg_color="#b5b942")
        frame_jogador_local.place(relwidth=0.9, relheight=0.35, relx=0.05, rely=0.65)
        self.dict_frames["jogador_local"] = frame_jogador_local

        jogador_frame_2 = self.tabuleiro.jogadores[(self.tabuleiro.jogador_local +1) % 3]
        frame_jogador2 = customtkinter.CTkScrollableFrame(master=self.canvas, orientation="horizontal", label_text=f"{jogador_frame_2.nome}\n{len(jogador_frame_2.mao)} cartas", label_fg_color="#b5b942",label_text_color="black",label_font=("helvetica", 14, "bold"),fg_color="#b5b942")
        frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
        self.dict_frames["jogador2"] = frame_jogador2

        jogador_frame_3 = self.tabuleiro.jogadores[(self.tabuleiro.jogador_local +2) % 3]
        frame_jogador3 = customtkinter.CTkScrollableFrame(master=self.canvas, orientation="horizontal", label_text=f"{jogador_frame_3.nome}\n{len(jogador_frame_3.mao)} cartas", label_fg_color="#b5b942",label_text_color="black",label_font=("helvetica", 14, "bold"),fg_color="#b5b942")
        frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
        self.dict_frames["jogador3"] = frame_jogador3

        frame_contador = Frame(self.canvas, bg="#b5b942")
        frame_contador.place(relwidth=0.1, relheight=0.2, relx=0.05, rely=0.375)
        texto_contador = Label(frame_contador, text=f"Contador +1 \n {self.tabuleiro.contador_cartas_mais_um}", bg="#b5b942")
        texto_contador.pack(pady=10)
        self.dict_frames["frame_contador"] = frame_contador


        if self.tabuleiro.ultima_carta == None: # significa que é a primeira jogada
            self.tabuleiro.ultima_carta = self.tabuleiro.baralho.get_carta_normal_aleatoria()
        frame_central = customtkinter.CTkFrame(master=self.canvas, fg_color="#b5b942")
        frame_central.place(relwidth=0.2, relheight=0.25, relx=0.4, rely=0.35)
        label_carta = customtkinter.CTkLabel(master=frame_central, image=self.dict_cards[self.cria_chave_para_ultima_carta()], text="")
        label_carta.pack(expand=True)
        self.dict_frames["frame_central"] = frame_central
        
        frame_botoes = Frame(self.canvas, bg="#b5b942")
        frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.375)
        botao_comprar = Button(frame_botoes, text="Comprar Carta", command=self.comprar_carta) 
        botao_comprar.place(relx=0.5, rely=0.2, anchor="center")
        botao_passar_turno = Button(frame_botoes, text="Passar Turno", command=self.passar_turno)
        botao_passar_turno.place(relx=0.5, rely=0.5, anchor="center")
        self.dict_frames["frame_botoes"] = frame_botoes
        
        self.adiciona_cartas_iniciais_ao_jogador_design(self.tabuleiro.jogadores[self.tabuleiro.jogador_local], frame_jogador_local)
        self.adiciona_cartas_iniciais_ao_jogador_design(jogador_frame_2, frame_jogador2)
        self.adiciona_cartas_iniciais_ao_jogador_design(jogador_frame_3, frame_jogador3)

    
    def adiciona_cartas_iniciais_ao_jogador_design(self, jogador, frame):
        cartas_mao = jogador.mao 
        if jogador.id == self.tabuleiro.local_id:
            for carta in cartas_mao:
                if carta.cor_primaria == 'preto':
                    imagem = f'{carta.tipo}'
                    btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.realizar_jogada(c), fg_color="#b5b942", hover_color="#b5b942")   
                    btn.carta = carta
                    self.dict_btn_cartas[carta] = btn

                else:
                    imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                    btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.realizar_jogada(c), fg_color="#b5b942", hover_color="#b5b942")
                    btn.carta = carta
                    self.dict_btn_cartas[carta] = btn
                btn.pack(side="left", padx=10, anchor="center")
        else:
            for carta in jogador.mao:
                imagem = customtkinter.CTkLabel(master=frame, image=self.dict_cards['fundo_carta'], text="")
                imagem.pack(side="left", padx=10,anchor="center")


    def adiciona_cartas_compradas_ao_jogador_design(self, lista_cartas_compradas, frame):
        for carta in lista_cartas_compradas:
            if carta.cor_primaria == 'preto':
                imagem = f'{carta.tipo}'
                btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.realizar_jogada(c), fg_color="#b5b942", hover_color="#b5b942")  
                self.dict_btn_cartas[carta] = btn
                
            else:
                imagem = f'{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}'
                btn = customtkinter.CTkButton(master=frame, image=self.dict_cards[imagem], text="", command=lambda c=carta: self.realizar_jogada(c), fg_color="#b5b942", hover_color="#b5b942")
                self.dict_btn_cartas[carta] = btn

            btn.pack(side="left", padx=10, anchor="center")                    


    def comprar_carta(self):
        if self.tabuleiro.bloqueado == False and self.tabuleiro.eh_a_vez_do_jogador_local_jogar() :
            if isinstance(self.tabuleiro.ultima_carta, CartaEspecial):
                if self.tabuleiro.ultima_carta.tipo == 'mais-um':
                    if self.tabuleiro.precisa_comprar_contador:
                        cartas_compradas = []
                        for _ in range(self.tabuleiro.contador_cartas_mais_um):
                            carta_comprada = self.tabuleiro.baralho.get_carta_aleatoria()
                            self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao.append(carta_comprada)
                            cartas_compradas.append(carta_comprada)
                        self.tabuleiro.precisa_comprar_contador = False
                        self.adiciona_cartas_compradas_ao_jogador_design(cartas_compradas, self.dict_frames["jogador_local"])
                else:
                    cartas_compradas = []
                    carta_comprada = self.tabuleiro.baralho.get_carta_aleatoria()
                    self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao.append(carta_comprada)
                    cartas_compradas.append(carta_comprada)
                    self.adiciona_cartas_compradas_ao_jogador_design(cartas_compradas, self.dict_frames["jogador_local"])
            else:
                cartas_compradas = []
                carta_comprada = self.tabuleiro.baralho.get_carta_aleatoria()
                self.tabuleiro.jogadores[self.tabuleiro.jogador_local].mao.append(carta_comprada)
                cartas_compradas.append(carta_comprada)
                self.adiciona_cartas_compradas_ao_jogador_design(cartas_compradas, self.dict_frames["jogador_local"])

        elif self.tabuleiro.eh_a_vez_do_jogador_local_jogar():
            messagebox.showwarning("Atenção", "Você foi bloqueado, passe o turno")
        else:
            messagebox.showwarning("Atenção", "Não é sua vez de jogar")

            
    def passar_turno(self):
        titulo, mensagem = self.tabuleiro.passar_turno()
        if titulo == "":
            self.__dog_server_interface.send_move(mensagem)
            if self.tabuleiro.jogada != None and self.tabuleiro.jogada.jogada_vencedora:
                self.__dog_server_interface.send_move(mensagem)
                messagebox.showwarning("Vitória", "Você ganhou o jogo")
                return
            else:
                self.__dog_server_interface.send_move(mensagem)
                self.tela_partida_design()
                return
        messagebox.showwarning(titulo, mensagem)



    def realizar_jogada(self, carta):
        titulo, mensagem = self.tabuleiro.realizar_jogada(carta)
        if titulo == "":
            self.remove_botao_carta(carta)
            return
        messagebox.showwarning(titulo, mensagem)


    def remove_botao_carta(self, carta):
        self.tabuleiro.ultima_carta = carta
        btn = self.dict_btn_cartas[carta]
        btn.destroy()
        del self.dict_btn_cartas[carta]
        print(btn)


    def set_canvas(self): 
        self.canvas = Canvas(
            self.window,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def create_menu_design(self): #MUDAR NOME DE FUNÇÃO
        self.background_img = PhotoImage(file = f"src/menu_images/background.png")
        self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
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
        self.set_canvas()
        self.background_img = PhotoImage(file = f"src/menu_images/desconexao.png")
        self.canvas.create_image(0, 0,image=self.background_img,anchor="nw")
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

            self.dict_cards[f"fundo_carta"] = customtkinter.CTkImage(Image.open(f'src/menu_images/fundo_carta.png'), size=(100, 150))
    

    def cria_chave_para_ultima_carta(self):
        if isinstance(self.tabuleiro.ultima_carta, CartaNormal):
            return  f'{self.tabuleiro.ultima_carta.numero}-{self.tabuleiro.ultima_carta.cor_primaria}-{self.tabuleiro.ultima_carta.cor_secundaria}'
        return f'{self.tabuleiro.ultima_carta.tipo}'