import tkinter as tk

def centralizar_janela(root, largura_janela, altura_janela):
    # Obtém a largura e a altura do monitor/tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula a posição x e y para centralizar a janela
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    # Define a geometria da janela (largura x altura + posição x + posição y)
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

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

# Lista de cartas do jogador
cartas = ["Carta 1", "Carta 2", "Carta 3", "Carta 4", "Carta 5", "Carta 6", "Carta 7", "Carta 8", "Carta 9", "Carta 10"]

# Cria um canvas no frame de baixo
canvas = tk.Canvas(frame3, bg="#0000FF", width=largura_janela, height=altura_frame)
canvas.pack(side="left", fill="both", expand=True)

# Adiciona uma barra de rolagem horizontal ao frame de baixo
scrollbar = tk.Scrollbar(frame3, orient="horizontal", command=canvas.xview)
scrollbar.pack(side="bottom", fill="x")

# Configura o canvas para usar a barra de rolagem
canvas.configure(xscrollcommand=scrollbar.set)

# Cria um frame interno dentro do canvas para conter os botões das cartas
frame_cartas = tk.Frame(canvas, bg="#0000FF")
canvas.create_window((0, 0), window=frame_cartas, anchor="nw")

# Adiciona botões para cada carta no frame interno, com espaçamento entre eles
for carta in cartas:
    btn = tk.Button(frame_cartas, text=carta, padx=50, pady=80)
    btn.pack(side="left", padx=20, pady=10, anchor="center")

# Atualiza o tamanho do frame interno para ajustar os botões
frame_cartas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Mantém a janela aberta
root.mainloop()
