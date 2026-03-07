import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os

class GameScreen(ctk.CTkFrame):
    """ A class representing the game screen of the application """

    def __init__(self, parent, controller):
        # initialize the frame and set the parent and controller (main app) as attributes
        super().__init__(parent, fg_color="transparent")
        self.controller = controller

        # styling
        self.Fonts = {
            "title": ("Arial", 30, "bold", "italic"),
            "subtitle": ("Arial", 24, "bold", "italic"),
            "text": ("Arial", 20, "normal")
        }

        # create the GUI
        self._create_widgets()
        self._layout_widgets()

    def __name__(self):
        return "GameScreen"

    def _create_widgets(self):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        image_path = os.path.join(project_root, "assets", "Images", "game-background.png")
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(400, 600)
        )

        # container for everything
        self.game_area = ctk.CTkFrame(self, fg_color="transparent")
        
        # background
        self.bg_label = ctk.CTkLabel(self.game_area, image=self.bg_image, text="")

        # widgets
        self.main_title = ctk.CTkLabel(self.game_area, text="HOT&COLD", font=self.Fonts["title"])
        self.guess_label = ctk.CTkLabel(self.game_area, text="", font=self.Fonts["title"])
        self.guess_input = ctk.CTkEntry(self.game_area, font=self.Fonts["text"])
        self.submit_button = ctk.CTkButton(self.game_area, text="Guess", command=self._submit_guess)
        self.attempts_label = ctk.CTkLabel(self.game_area, text=f"Attempts:{self.controller.core.attempts}", font=self.Fonts["title"])

    def _layout_widgets(self):
        # make container fill screen
        self.game_area.pack(fill="both", expand=True)

        # allow stacking
        self.game_area.grid_rowconfigure(0, weight=1)
        self.game_area.grid_columnconfigure(0, weight=1)

        # background layer
        self.bg_label.grid(row=0, column=0, sticky="nsew")

        # widgets on top of background
        self.main_title.place(relx=0.5, rely=0.15, anchor="center")
        self.guess_input.place(relx=0.5, rely=0.45, anchor="center")
        self.submit_button.place(relx=0.5, rely=0.55, anchor="center")
        self.attempts_label.place(relx=0.5, rely=0.65, anchor="center")

    def _submit_guess(self):
        value = self.guess_input.get().strip()
        if not self.controller.core._check_guess_validity(value):
            self._error_message(
                f"Invalid input! Enter a number between 1 and {self.controller.core.max_number}."
            )
            self.guess_input.delete(0, tk.END)
            return

        guess = int(value)
        self.guess_input.delete(0, tk.END)
        self._treat_guess(guess)

    def _error_message(self, message):
        self.guess_label.config(text=message)
        self.guess_label.after(2000, self.refresh_prompt)

    def refresh_prompt(self):
        self.guess_label.config(text=f"Enter your guess (1-{self.controller.core.max_number}):")

    def _treat_guess(self, guess):
        guess_type = self.controller.core._check_guess(guess)
        self._update_ui(guess_type)

        if guess_type == "correct":
            self.controller._show_screen("ResultsScreen")

    def _update_ui(self, current):
        if current == "hot":
            self.configure(fg_color="red")
            self.result_label.config(bg="red", fg="white", text="Too low! Go higher!")
            self.game_frame.config(bg="red")
        elif current == "cold":
            self.configure(fg_color="blue")
            self.result_label.config(bg="blue", fg="white", text="Too high! Go lower!")
            self.game_frame.config(bg="blue")
        elif current == "correct":
            self.configure(fg_color="green")
            self.result_label.config(text="Congratulations! You guessed it!", fg="white", bg="green")
            self.game_frame.config(bg="green")
            self.guess_input.config(state="disabled")
            self.submit_button.config(state="disabled")