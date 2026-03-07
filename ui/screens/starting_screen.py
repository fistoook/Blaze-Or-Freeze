import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from ui.components.level_slider import CustomLevelSlider
from core import HotNCold

class StartScreen(ctk.CTkFrame):
    """ A class representing the initial screen of the application """

    def __init__(self, parent, controller):
        # initialize the frame and set the parent and controller (main app) as attributes
        super().__init__(parent, fg_color="transparent")
        self.controller = controller 
        
        # styling
        self.Fonts = {
            "title": ("Arial", 42, "bold", "italic"),
            "subtitle": ("Arial", 20, "bold", "italic")
        }
        self.Font_colors = ["red", "black", "blue"]

        # default level settings
        self.selected_level = "Easy"
        self.selected_max_value = 10

        # create the GUI
        self._create_widgets()
        self._layout_widgets()

    def __name__(self):
        return "StartScreen"

    def _create_widgets(self):
        # method to create the widgets for the start screen
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        image_path =  os.path.join(project_root, "assets", "Images", "Thermometer.png")
        # Create a main content frame to hold all widgets
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=20)
        # Create all the qidgets
        self.main_title = ctk.CTkLabel(self.content_frame, text="HOT&COLD", font=self.Fonts["title"])
        self.image = ctk.CTkImage (light_image = Image.open(image_path), dark_image=Image.open(image_path), size=(150, 200))
        self.image_label = ctk.CTkLabel(self.content_frame, image=self.image, text="")
        self.level_slider = CustomLevelSlider(self.content_frame, command=self._on_level_change)
        self.play_button = ctk.CTkButton(self.content_frame, command=self._play_game, text="Start Game", cursor="hand2", width=220, height=60, font=self.Fonts["subtitle"])

    def _layout_widgets(self):
        # method to layout the widgets for the start screen
        self.content_frame.pack(fill="both", expand=True)
        
        self.main_title.pack(pady=30)
        self.image_label.pack(pady=0)
        self.level_slider.pack(pady=20)
        self.play_button.pack(pady=20)

    def _on_level_change(self, level_name, max_value):
        # Store the selected level in the controller
        self.selected_level = level_name
        self.selected_max_value = max_value

    def _play_game(self):
        # Initialize the game core
        self.controller.core._update_level(self.selected_level, self.selected_max_value)
        # initialize and show the game screen
        self.controller._show_screen("GameScreen")