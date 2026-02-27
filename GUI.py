import tkinter as tk
from GameLogic import BlazeOrFreeze as BOF
class BlazeOrFreezeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.GameLogic = BOF()
        
    
    def run(self):
        self.root.mainloop()