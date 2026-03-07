import tkinter as tk
import customtkinter as ctk
from core import HotNCold
from ui.screens.starting_screen import StartScreen
from ui.screens.game_screen import GameScreen
from ui.screens.results_screen import ResultsScreen
from ui.components.title_bar import customTitleBar
from ui.components.level_slider import CustomLevelSlider
import os

class HotNColdApp(tk.Tk):
    # main application class that inherits from tk.Tk
    def __init__(self):
        super().__init__() # create the main screen
        self._style_root()  # style main screen

        self.core = HotNCold() # initialize the game core

        # create a container to hold the different screens
        self.container = ctk.CTkFrame(self, width=300, height=350, fg_color="#212121", corner_radius=20)
        self.container.place(relx=0.5, rely=0.5, anchor="center")  # center and size the container

        # add custom theme
        project_root = os.getcwd()
        theme_path = os.path.join(project_root, "assets", "themes", "hot_cold_theme.json")
        ctk.set_default_color_theme(theme_path)
        ctk.set_appearance_mode("system")
        
        # Configure container grid to allow screens to expand
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.screens = {} # screen dictionary to hold the different screens

        # fill in the screen dictionary with the different screens
        for Screen in (StartScreen, GameScreen, ResultsScreen):
            screen = Screen(self.container, self) # create an instance of the screen and pass the container and the controller (main app) as arguments
            self.screens[screen.__name__()] = screen # add the screen to the screen dictionary with its name as the key
            screen.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self._show_screen("StartScreen") # show the start screen

    def run(self):
        self.mainloop() # start the main loop of the application
    
    def _show_screen(self, name):
        try:
            screen = self.screens[name] # get the screen from the screen dictionary by name
            if name == "GameScreen":
                screen._update_prompt() # update the prompt on the game screen to reflect the current max number
            screen.tkraise() # raise the screen to the top of the stacking order to make it visible
        except KeyError:
            print(f"Error: Screen '{name}' not found.")
            return

    def _style_root(self):
        self._center_window() # center the main screen on the user's display
        self.overrideredirect(True) # remove the default title bar
        self.titlebar = customTitleBar(self, self) # create an instance of the custom title bar
        self.titlebar.pack(fill="x")
        self.resizable(False, False) # make the main screen non-resizable

    def _center_window(self, width=600, height=800):
        self.update_idletasks() # update the main screen to get the correct dimensions
        # method to center the main screen on the user's display
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2) # calculate the x coordinate to center the wndow
        y = (screen_height // 2) - (height // 2) # caculate the y coordinate to center the window

        # setthe geometry of the main screen to the calculated coordinatesand the specified width and height
        self.geometry(f"{int(width)}x{int(height)}+{x}+{y}") 