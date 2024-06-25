
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Button
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk

cor_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
cor_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
dict_of_cards = {}

class Teste():
    def __init__(self):
        self.a = 1

    def criar_menu_inicial(self, largura_janela, altura_janela):
        janela = self.criar_janela_centralizada("Rainbow Cards", largura_janela, altura_janela)
        self.design_menu_inicial(janela, largura_janela, altura_janela)

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

    def design_menu_inicial(self, janela, largura_janela, altura_janela):
        imagem_de_fundo = ImageTk.PhotoImage(Image.open("menu_images/rainbow_bg.png"))
        canvas = Canvas(janela, width=largura_janela, height=altura_janela)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=imagem_de_fundo, anchor="nw")

        # Necessário para manter uma referência à imagem
        self.imagem_de_fundo = imagem_de_fundo

        frame_jogador2 = Frame(canvas, bg="#a5b942")
        frame_jogador2.place(relwidth=0.4, relheight=0.3, relx=0.05, rely=0.0)
        texto_jogador2 = Label(frame_jogador2, text="Jogador 2\n teste\n 3 cartas", bg="#a5b942")
        texto_jogador2.pack(pady=10)

        frame_jogador3 = Frame(canvas, bg="#a5b942")
        frame_jogador3.place(relwidth=0.4, relheight=0.3, relx=0.55, rely=0.0)
        texto_jogador3 = Label(frame_jogador3, text="Jogador 3\n teste\n 5 cartas", bg="#a5b942")
        texto_jogador3.pack(pady=10)

        frame_contador = Frame(canvas, bg="#b5b942")
        frame_contador.place(relwidth=0.1, relheight=0.2, relx=0.05, rely=0.4)
        texto_contador = Label(frame_contador, text="Contador +1\n 6", bg="#b5b942")
        texto_contador.pack(pady=10)

        #problemas aqui. Não consigo fazer a imagem aparecer não importa o que eu faça. O melhor que ocorre é um quadrado branco
        frame_central = Frame(canvas, bg="#b5b942")
        frame_central.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.35)
        #import da imagem
        image_original_carta = Image.open("cartas/1-amarelo-anil.jpeg").resize((100, 100))
        image_tk_carta = ImageTk.PhotoImage(image_original_carta)
        #widget
        label_carta = Label(frame_central, image=image_tk_carta)
        label_carta.pack()

        frame_botoes = Frame(canvas, bg="#b5b942")
        frame_botoes.place(relwidth=0.1, relheight=0.2, relx=0.85, rely=0.4)
        botao_comprar = Button(frame_botoes, text="Comprar Carta")
        botao_comprar.place(relx=0.5, rely=0.3, anchor="center")
        botao_passar_turno = Button(frame_botoes, text="Passar Turno")
        botao_passar_turno.place(relx=0.5, rely=0.7, anchor="center")



        frame_cartas = Frame(canvas, bg="#c5b942")
        frame_cartas.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.7)

        canvas_cartas = Canvas(frame_cartas, width=largura_janela, height=altura_janela//3)
        canvas.create_image(0, 0, image=ImageTk.PhotoImage(Image.open("menu_images/canvas_cartas.png")), anchor="e")
        canvas_cartas.pack(side = LEFT, fill="both", expand=True)

        scrollbar = Scrollbar(canvas_cartas, orient="horizontal", command=canvas_cartas.xview)
        scrollbar.pack(anchor= "s", fill="x")
        canvas_cartas.configure(xscrollcommand=scrollbar.set)

janelateste = Teste()

janelateste.criar_menu_inicial(1280, 720)