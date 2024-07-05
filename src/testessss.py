
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
import customtkinter

cartas = [CartaEspecial("preto", "mais-um"), CartaEspecial("preto", "bloquear"), CartaNormal("vermelho", "laranja", 1), CartaNormal("azul", "laranja", 2), CartaNormal("roxo", "verde", 3)]
root = customtkinter.CTk()

root.geometry("600x400")

frame = customtkinter.CTkScrollableFrame(root, orientation="horizontal", label_text="Nome do jogador\nQuantidade de cartas")
frame.pack(fill=BOTH, expand=True)
for carta in cartas:
    if carta.cor_primaria == "preto":
        imagem = customtkinter.CTkImage(Image.open(f'src/cartas/{carta.tipo}.png'), size=(100, 150))
        botao = customtkinter.CTkButton(master=frame, image=imagem, text="")
    else:
        imagem = customtkinter.CTkImage(Image.open(f'src/cartas/{carta.numero}-{carta.cor_primaria}-{carta.cor_secundaria}.png'), size=(100, 150))
        botao = customtkinter.CTkButton(master=frame, image=imagem, text="")
    botao.pack(side=LEFT, padx = 60, pady = 90, anchor = CENTER)

root.mainloop()