
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Button
from window import Window
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from PIL import Image, ImageTk
from tabuleiro import Tabuleiro

class App:
    def __init__(self, root):
        self.tabuleiro = Tabuleiro()
        self.root = root
        self.root.title("Carta Aleatória")
        self.root.geometry("1280x720")

        self.label = Label(root)
        self.label.pack(expand=True)

        self.button = Button(root, text="Mostrar Carta Aleatória", command=self.show_random_card)
        self.button.pack()

    def show_random_card(self):
        carta = self.tabuleiro.get_random_card()
        image_path = carta.get_card_image()

        image = Image.open(image_path)
        image = image.resize((256//2, 345//2), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.label.config(image=photo)
        self.label.image = photo

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()