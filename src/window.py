from tkinter import *
import customtkinter

class Window():

    def __init__(self) -> None:
        self.__window = customtkinter.CTk()
        self.createWindow()
        
    def getWindow(self):
        return self.__window

    def createWindow(self) -> None:
        self.__window.geometry("1280x720")
        self.__window.configure(bg = "#ffffff")