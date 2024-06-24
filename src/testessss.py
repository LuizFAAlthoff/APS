
import tkinter as tk
from PIL import Image, ImageTk

cor_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
cor_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
dict_of_cards = {}

# Inicialize a janela principal do Tkinter
root = tk.Tk()

# Função para carregar e redimensionar as imagens
def carregar_imagens():
    for cor_prim in cor_primaria:
        for cor_sec in cor_secundaria:
            for numero in range(1, 3):
                if cor_prim != cor_sec:
                    image = Image.open(f'cartas/{numero}-{cor_prim}-{cor_sec}.jpeg')
                    img = image.resize((100, 150))
                    dict_of_cards[f"{numero}-{cor_prim}-{cor_sec}.jpeg"] = ImageTk.PhotoImage(img)
    x=1

# Chame a função para carregar as imagens
carregar_imagens()

# A parte x=1 parece ser desnecessária no contexto do seu código
# x = 1

# Comece o loop principal do Tkinter
root.mainloop()