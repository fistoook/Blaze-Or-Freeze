import tkinter as tk
from tkinter.font import Font
import customtkinter as ctk

class ResultsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=20, fg_color=("white", "#212121"))
        self.controller = controller

        self.Fonts = {
            "title": Font(family="Arial", size=20, weight="bold"),
            "text": Font(family="Arial", size=12)
        }

        self._create_widgets()
        self._layout_widgets()

    def __name__(self):
        return "ResultsScreen"
    
    def _create_widgets(self):
        pass

    def _layout_widgets(self):
        pass