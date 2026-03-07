import customtkinter as ctk
from PIL import Image
from ui.components.guess_entry import CustomEntry
import os


class GameScreen(ctk.CTkFrame):
    """A class representing the game screen of the application."""

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent", border_width=0) # initialize the frame
        self.controller = controller # main application

        # font dectionary
        self.Fonts = {
            "title": ("Arial", 42, "bold", "italic"),
            "subtitle": ("Arial", 26, "bold", "italic"),
            "text": ("Arial", 20, "normal"),
        }

        # define color schemes for hot and cold feedback
        self.hot_colors = {
            1: "#FDECEC",
            2: "#FCDDDD",
            3: "#FBCBCB",
            4: "#F9B8B8",
            5: "#F7A3A3",
            6: "#F58D8D",
            7: "#F27777",
            8: "#EF6161",
            9: "#EB4B4B",
            10: "#E33636",
        }
        self.cold_colors = {
            1: "#EAF3FF",
            2: "#DAEAFF",
            3: "#C8E0FF",
            4: "#B5D5FF",
            5: "#A1CAFF",
            6: "#8CBEFF",
            7: "#76B1FF",
            8: "#60A4FF",
            9: "#4A96FF",
            10: "#2F85F6",
        }

        # define prompts for hot and cold feedback
        self.hot_prompts = {
            1: "Ice age low — go lower!",
            2: "Very low — push the guess down.",
            3: "Low and chilly — drop lower!",
            4: "Warming up — a bit lower.",
            5: "Mild heat — keep going lower.",
            6: "Pretty warm — lower...",
            7: "Hot zone — edge downward.",
            8: "Very hot — tiny step lower.",
            9: "Burning close — just a touch lower.",
            10: "Inferno close — go slightly lower.",
        }
        self.cold_prompts = {
            1: "Arctic high — go higher!",
            2: "Very high — bring the guess up.",
            3: "High and chilly — climb higher.",
            4: "Cooling down — a bit higher.",
            5: "Mild cold — keep going higher.",
            6: "Pretty close — higher...",
            7: "Hot trail — edge upward.",
            8: "Very close — tiny step higher.",
            9: "Almost there — just a touch higher.",
            10: "Needle-close — go slightly higher.",
        }

        # create the GUI
        self._create_widgets()
        self._layout_widgets()

    def __name__(self):
        return "GameScreen"

    def _create_widgets(self):
        # create the widgets for the game screen
        self.main_title = ctk.CTkLabel(self, text="HOT&COLD", font=self.Fonts["title"], fg_color="transparent")

        self.guess_label = ctk.CTkLabel(self, text="", font=self.Fonts["subtitle"], fg_color="transparent")
        self.guess_input = CustomEntry(
            self,
            font=self.Fonts["text"],
            on_enter=self._submit_guess,
            width=280,
            height=50,
            placeholder_text="Enter your guess...",
            justify="center",
            corner_radius=20,
        )
        self.submit_button = ctk.CTkButton(self, text="Guess", command=self._submit_guess, width=100, height=50)

        self.attempts_label = ctk.CTkLabel(
            self,
            text=f"Attempts: {self.controller.core.attempts}",
            font=self.Fonts["text"],
            fg_color="transparent",
        )
        self.result_label = ctk.CTkLabel(self, text="", font=self.Fonts["text"], fg_color="transparent")

        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        image_path = os.path.join(project_root, "assets", "Images", "Thermometer.png")
        self.image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(120, 160))
        self.image_label = ctk.CTkLabel(self, image=self.image, text="", fg_color="transparent")

    def _layout_widgets(self):
        # configure the grid to allow for proper placement of widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # place the widgets in the grid
        self.main_title.place(relx=0.5, rely=0.10, anchor="center")
        self.guess_label.place(relx=0.5, rely=0.2, anchor="center")
        self.guess_input.place(relx=0.5, rely=0.3, anchor="center")
        self.submit_button.place(relx=0.5, rely=0.4, anchor="center")
        self.attempts_label.place(relx=0.5, rely=0.5, anchor="center")
        self.image_label.place(relx=0.5, rely=0.7, anchor="center")
        self.result_label.place(relx=0.5, rely=0.95, anchor="center")

    def _submit_guess(self, _event=None):
        # get the guess from the input field and validate it
        value = self.guess_input._get()
        self.guess_input._clear()
        self._treat_guess(value) # pass the guess for processing and UI update

    def _error_message(self, message):
        # display an error message for invalid input and reset the prompt after a short delay
        self.guess_label.configure(text=message)
        self.guess_label.after(2000, self._update_prompt)

    def _update_prompt(self):
        # update the prompt back to the default stater
        self.guess_label.configure(text=f"Enter your guess (1-{self.controller.core.max_number}):")

    def _treat_guess(self, guess):
        if not self.controller.core._check_guess_validity(guess):
            self.guess_input._error_message(f"Enter a number between 1 and {self.controller.core.max_number}.")
            return
        
        guess = int(guess) # convert the guess to an integer for processing
        self.controller.core.attempts += 1

        # check the guess against the random number and get the result for UI update
        result = self.controller.core._check_guess(guess) 
        self._update_ui(result) # update the UI based on the result of the guess

        if result["direction"] == "correct":
            # after a short delay, show the results screen
            self.controller.after(2000, lambda: self.controller._show_screen("ResultsScreen"))

    def _update_ui(self, result):
        direction = result["direction"] # get the direction (hot, cold, correct) from the result
        case = result["case"] # get the case (1-10) from the result to determine the intensity of the feedback

        # update the UI based on the direction and case of the guess
        if direction == "correct":
            self.controller.container.configure(fg_color="#2ECC71")
            self.result_label.configure(text="Perfect guess! You nailed it.")
            self.guess_input.configure(state="disabled")
            self.submit_button.configure(state="disabled")
        elif direction == "hot":
            self.controller.container.configure(fg_color=self.hot_colors[case])
            self.result_label.configure(text=self.hot_prompts[case])
        elif direction == "cold":
            self.controller.container.configure(fg_color=self.cold_colors[case])
            self.result_label.configure(text=self.cold_prompts[case])

        # update the attempts label to reflect the new number of attempts
        self.attempts_label.configure(text=f"Attempts: {self.controller.core.attempts}")

    def _new_round(self):
        # reset the UI for a new round
        self.guess_input.configure(state="normal")
        self.submit_button.configure(state="normal")
        self.result_label.configure(text="")
        self.controller.container.configure(fg_color="#212121")
        self.attempts_label.configure(text=f"Attempts: {self.controller.core.attempts}")
        self._update_prompt()