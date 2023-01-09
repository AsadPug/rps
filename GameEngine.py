import tkinter as tk

from Controller import MenuController

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.controller = MenuController(self)
