
from View import (
    View,
    MenuView,
    GameView
)   
import tkinter as tk
from Container import BetterFrame

class Controller():
    def __init__(self, root: tk.Tk):
        self.root = root
        """En quelque sorte, il s'agit de la fenêtre principale du jeu
        qui est aussi responsable de sa boucle principale."""

        self.main_frame = BetterFrame(root, 0, 0)
        """Frame principale du jeu. Elle contient toutes les autres frames"""
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.view: View
        """Vue associée au controlleur"""

    def start(self):
        """Lancement du controlleur"""
        self.view.draw()

    def quit_game(self):
        """Fermeture du jeu"""
        self.root.destroy()

    def change_controller(self, change_to):
        """Changement de controlleur"""
        self.view.destroy()
        self.root.controller = change_to(self.root)
        self.root.controller.start()

class MenuController(Controller):
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.view = MenuView(self.main_frame)

    def start(self):
        self.view.main_canvas.tag_bind(self.view.quit_button,
                                       "<Button-1>",
                                       lambda _: self.quit_game())

        self.view.main_canvas.tag_bind(self.view.play_button,
                                       "<Button-1>",
                                       lambda _:
                                       self.change_controller(GameController))

        super().start()

class GameController(Controller):
    def __init__(self, root:tk.Tk):
         super().__init__(root)
         self.view: GameView = GameView(self.main_frame)