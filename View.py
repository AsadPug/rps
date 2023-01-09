from abc import ABC
import tkinter as tk
from Container import BetterButton,BetterCanvas,BetterFrame,BetterLabel
from PIL import ImageTk, Image

class View(ABC):
    def __init__(self, main_frame: BetterFrame):
        self.main_frame = main_frame

        self.background_width = 1200
        self.background_height = 1200

    def draw(self):
        """Méthode abstraite de lancement de la vue"""
        # Recursively place all the widgets in the frame
        self.place_children(self.main_frame)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

    def place_children(self, container):
        """Méthode abstraite de placement des widgets de la vue"""
        for widget in container.winfo_children():
            if isinstance(widget, (BetterButton, BetterLabel, BetterFrame, BetterCanvas)):
                if widget.winfo_children():
                    self.place_children(widget)
                widget.place(relx=widget.x, rely=widget.y, anchor="center")

    def destroy(self):
        """Méthode de destruction de la vue"""
        self.main_frame.forget()

    def forget(self):
        """Méthode d'oublie de la vue"""
        for content in self.main_frame.winfo_children():
            content.pack_forget()
        self.main_frame.pack_forget()

    def img_format(file: str, dimensions: tuple[int, int]) -> tk.PhotoImage:
        img = Image.open(file)
        img = img.resize(dimensions)
        img = img.convert('RGBA')
        data = img.getdata()
        
        new_data = []
        for item in data:
            if item[0] == 255 and item[1] == 255 and item[2] == 0:  # finding yellow colour
                # replacing it with a transparent value
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        return ImageTk.PhotoImage(img)

class MenuView(View):
    
    def __init__(self, main_frame: BetterFrame):
        super().__init__(main_frame)
    
        self.main_canvas = BetterCanvas(self.main_frame, 0.5, 0.5,
                                        width=self.background_width,
                                        height=self.background_height,
                                        highlightthickness=0)
        
        self.quit_button = self.main_canvas.create_rectangle(200,200,400,400,fill="red")

    def draw(self):
        """Méthode de lancement de la vue"""
        super(MenuView, self).draw()