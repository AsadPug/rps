import tkinter as tk

from Controller import MenuController

class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.controller = MenuController(self)
        self.resizable(False,False)
        self.geometry("1200x1200")

def main()->None:
    root = Root()
    root.controller.start()
    root.mainloop()

if __name__ == "__main__":
    main()