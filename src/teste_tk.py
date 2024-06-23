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

# Mantém a janela aberta
root.mainloop()
