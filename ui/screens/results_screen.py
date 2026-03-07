import tkinter as tk
import customtkinter as ctk

class ResultsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=20, fg_color="transparent", border_width=0)
        self.controller = controller

        # font dectionary
        self.Fonts = {
            "title": ("Arial", 32, "bold", "italic"),
            "number": ("Arial", 56, "bold", "italic"),
            "subtitle": ("Arial", 26, "bold", "italic"),
            "text": ("Arial", 18, "normal"),
        }
        self.attempts = self.controller.core.attempts

        self._create_widgets()
        self._layout_widgets()

    def __name__(self):
        return "ResultsScreen"
    
    def _create_widgets(self):
        self.main_title = ctk.CTkLabel(self, text="👏Congratulations!👏", font=self.Fonts["title"], fg_color="transparent")
        self.number_text_label = ctk.CTkLabel(self, text="The number was:", font=self.Fonts["subtitle"], fg_color="transparent", text_color="#FF5722")
        self.number_label = ctk.CTkLabel(self, text=f"", font=self.Fonts["number"], fg_color="transparent", text_color="#FF5722")
        self.context_label = ctk.CTkLabel(self, text="🎉You guessed it!🎉", font=self.Fonts["subtitle"], fg_color="transparent")
        self.attempts_label = ctk.CTkLabel(self, text=f"", font=self.Fonts["text"], fg_color="transparent")
        self.play_again_button = ctk.CTkButton(self, text="Play Again", command=self._play_again, width=120, height=40)
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.controller.destroy, width=120, height=40)
        self.contributers_label = ctk.CTkLabel(self, text="Made with ❤️ by shmer and fistook", font=self.Fonts["text"], fg_color="transparent")

    def _layout_widgets(self):
        self.main_title.place(relx=0.5, rely=0.1, anchor="center")
        self.number_text_label.place(relx=0.5, rely=0.25, anchor="center")
        self.number_label.place(relx=0.5, rely=0.35, anchor="center")
        self.context_label.place(relx=0.5, rely=0.5, anchor="center")
        self.attempts_label.place(relx=0.5, rely=0.65, anchor="center")
        self.play_again_button.place(relx=0.5, rely=0.75, anchor="center", x=-70)
        self.exit_button.place(relx=0.5, rely=0.75, anchor="center", x=70)
        self.contributers_label.place(relx=0.5, rely=0.99, anchor="center")

    def tkraise(self, aboveThis=None):
        # refresh labels with current values every time screen is shown
        self.number_label.configure(text=f"{self.controller.core.random_number}")
        self.attempts_label.configure(text=f"Attempts: {self.controller.core.attempts}😎👌🔥")
        super().tkraise(aboveThis)
    
    def _play_again(self):
        self.controller.core.reset_round() # reset the game state for a new round
        self.controller.screens["GameScreen"]._new_round() # reset the game screen for a new round
        self.controller._show_screen("GameScreen") # show the game screen to start a new round