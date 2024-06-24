import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
root = tk.Tk()

# Define o título da janela
root.title("Minha Janela Centralizada")

# Define o tamanho da janela
largura_janela = 800
altura_janela = 600

# Centraliza a janela na tela
centralizar_janela(root, largura_janela, altura_janela)

# Calcula a altura de cada frame
altura_frame = altura_janela // 3

# Cria os três frames
frame1 = tk.Frame(root, bg="#f5b942", width=largura_janela, height=altura_frame)
frame2 = tk.Frame(root, bg="#a5b942", width=largura_janela, height=altura_frame)
frame3 = tk.Frame(root, bg="#d5b942", width=largura_janela, height=altura_frame)

# Posiciona os frames na janela usando pack
frame1.pack(fill="both")
frame2.pack(fill="both")
frame3.pack(fill="both")

# Calcula a largura de cada subframe no frame do meio
largura_subframe = largura_janela // 3

# Cria os três subframes dentro do frame do meio
subframe1 = tk.Frame(frame2, bg="#f5c942", width=largura_subframe*1/5, height=altura_frame)
subframe2 = tk.Frame(frame2, bg="#a5b942", width=largura_subframe*3/5, height=altura_frame)
subframe3 = tk.Frame(frame2, bg="#f5a942", width=largura_subframe*1/5, height=altura_frame)

# Posiciona os subframes no frame do meio usando pack com side="left"
subframe1.pack(side="left", fill="both", expand=True)
subframe2.pack(side="left", fill="both", expand=True)
subframe3.pack(side="left", fill="both", expand=True)

# Adiciona a palavra "contador" e o número 1 abaixo dela no subframe1
label_contador = tk.Label(subframe1, text="contador", bg="#f5c942")
label_contador.pack(pady=10)
label_numero = tk.Label(subframe1, text="1", bg="#f5c942")
label_numero.pack()

# Adiciona uma imagem no subframe2
# Carrega a imagem (substitua 'caminho_para_imagem.png' pelo caminho da sua imagem)
imagem = Image.open("cartas/1-amarelo-anil.jpeg")
imagem = imagem.resize((largura_subframe, altura_frame), Image.ANTIALIAS)
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(subframe2, image=imagem_tk, bg="#a5b942")
label_imagem.pack(expand=True)

# Adiciona os botões no subframe3
btn_comprar = tk.Button(subframe3, text="Comprar Carta", command=comprar_carta)
btn_comprar.pack(pady=10)
btn_jogada = tk.Button(subframe3, text="Realizar Jogada", command=realizar_jogada)
btn_jogada.pack(pady=10)

# Lista de cartas do jogador
cartas = ["Carta 1", "Carta 2", "Carta 3", "Carta 4", "Carta 5", "Carta 6", "Carta 7", "Carta 8", "Carta 9", "Carta 10"]

# Cria um canvas no frame de baixo
canvas = tk.Canvas(frame3, bg="#0000FF", width=largura_janela, height=altura_frame)
canvas.pack(side="left", fill="both", expand=True)

# Adiciona botões para cada carta no frame interno, com espaçamento entre eles
x_position = 10  # Posição inicial dos botões no eixo x

for carta in cartas:
    btn = tk.Button(canvas, text=carta, padx=50, pady=80)
    btn.pack(side="left", padx=10, pady=10, anchor="center")
    x_position += 100

# Adiciona uma barra de rolagem horizontal ao canvas
scrollbar = tk.Scrollbar(frame3, orient="horizontal", command=canvas.xview)
scrollbar.pack(side="bottom", fill="x")

# Configura o canvas para usar a barra de rolagem
canvas.configure(xscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda event, canvas=canvas: configurar_scrollbar())

# Mantém a janela aberta
root.mainloop()
