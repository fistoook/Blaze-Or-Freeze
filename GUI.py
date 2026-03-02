import tkinter as tk
from tkinter.font import Font
from GameLogic import HotNCold

TITLE = "HOT&COLD"

class HotNColdApp(tk.Tk):
    def __init__(self):
        super().__init__() # create the main screen
        self._style_root()  # style main screen

        self.game = HotNCold() # an object of the game logic class

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.screens = {}

        for Screen in (StartScreen, GameScreen, ResultScreen):
            screen = Screen(self.container, self)
            self.screens[screen.__name__] = screen
            screen.grid(row=0, column=0, sticky="nsew")

    def run(self):
        self._show_screen("StartScreen")

    def _show_screen(self, name):
        screen = self.screens[name]
        screen.tkraise()

    def _style_root(self):
        self.update_idletasks()
        self.title("Main Menu")
        self._center_window()

    def _center_window(self, width=600, height=500):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{int(width)}x{int(height)}+{x}+{y}") 

class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # styling elements 
        self.Fonts = {
            "title": Font(family="Arial", size=20, weight="bold", slant="italic")
        }
        self.Font_colors = ["red", "black", "blue"]

        # create the GUI
        self._create_screen_widgets()
        self._layout_screen_widgets() 

        self.mainloop()

    def _create_screen_widgets(self):
        self.main_title = tk.Label(self, text=TITLE)
        self.name_input_grid = tk.Frame(self)
        self.name_label = tk.Label(self.name_input_grid, text="Enter your username:")
        self.name_input = tk.Entry(self.name_input_grid)
        self.send_button = tk.Button(self.name_input_grid, text="send", command=self._send_name)
        self.play_button = tk.Button(self, command=self._play_game)

    def _layout_screen_widgets(self):
        self.title_grid.pack()
        self.name_label.grid(row=0, column=0, columnspan=2)
        self.name_input.grid(row=1, column=0)
        self.send_button.grid(row=1,column=1)
        self.name_input_grid.pack()

    def _send_name(self):
        name = self.name_input.get()
        self.name_input.delete(0, tk.END)
        if not name:
            current_text = self.name_label["text"]
            self.name_label.after(3000, lambda: self._config_label(self.name_label, current_text))
            self.name_label.config(text="Invalid Name! enter a valid name:")
        else:
            self.name_label.config(text=F"Welcome {name}", fg="red", font=self.Fonts[0])

    def _config_label(self, label, text):
        label.config(text=text)

    def _play_game(self):
        # implement user data saving logic here ->
        self.controller._show_screen("GameScreen")

class GameScreen():
    def __init__(self, name, root, fonts):
        self.name = name
        self.root = root
        self.Fonts = fonts
        self.random_number = random.randint(1, 100)
        self._run_game()
    def _run_game(self):
        self._game_window(self.name)
        self._create_widgets()
        self._layout_widgets()
    def _check_guess(self, guess):
        if guess < self.random_number:
            return self.change_background("blaze")
        elif guess > self.random_number:
            return self.change_background("freeze")
        else:
            return self.change_background("correct")
    def change_background(self, current):
        self.welcome_label.destroy()
        if current == "blaze":
            self.game_window.configure(bg="red")
            self.guess_label.config(bg="red")
            #self.welcome_label.config(bg="red")
        if current == "freeze":
            self.game_window.configure(bg="blue")
            self.guess_label.config(bg="blue")
            #self.welcome_label.config(bg="blue")
        if current == "correct":
            self.game_window.configure(bg="green")
            #self.welcome_label.config(bg="green")
            self.guess_label.config(text="Congratulations! You guessed it!", fg="white", bg="green")
    def _create_widgets(self):
        self.game_frame = tk.Frame(self.game_window)
        self.guess_label = tk.Label(self.game_frame, text="Enter your guess (1-100):", font=self.Fonts[0], fg="black")
        self.guess_input = tk.Entry(self.game_frame)
        self.submit_button = tk.Button(self.game_frame, text="Submit", command=self._submit_guess)
    def _layout_widgets(self):
        self.game_frame.pack()
        self.guess_label.grid(row=0, column=0, columnspan=2)
        self.guess_input.grid(row=1, column=0)
        self.submit_button.grid(row=1, column=1)
    def _game_window(self, name):
        self.game_window = tk.Toplevel(self.root)
        self.game_window.title("Game Window")
        self.game_window.geometry("600x500")
        self.welcome_label = tk.Label(self.game_window, text=F"Welcome {name}", font=self.Fonts[0], fg="black")
        self.welcome_label.pack()
    
    def _submit_guess(self):
        value = self.guess_input.get()
        if not value.isdigit() or not (1 <= int(value) <= 100):
            self.guess_input.delete(0, tk.END)
            self.guess_label.config(text="Invalid input! Enter a number 1-100.", fg="red")
            self.guess_label.after(2000, lambda: self.guess_label.config(text="Enter your guess (1-100):", fg="black"))
        else:
            guess = int(value)
            self.guess_input.delete(0, tk.END)
            self._check_guess(guess)
        
class ResultScreen():
    def __init__(self, name, root, fonts):
        self.name = name
        self.root = root
        self.Fonts = fonts
        self.random_number = random.randint(1, 100)
        self._run_game()
    def _run_game(self):
        self._game_window(self.name)
        self._create_widgets()
        self._layout_widgets()
    def _check_guess(self, guess):
        if guess < self.random_number:
            return self.change_background("blaze")
        elif guess > self.random_number:
            return self.change_background("freeze")
        else:
            return self.change_background("correct")
    def change_background(self, current):
        self.welcome_label.destroy()
        if current == "blaze":
            self.game_window.configure(bg="red")
            self.guess_label.config(bg="red")
            #self.welcome_label.config(bg="red")
        if current == "freeze":
            self.game_window.configure(bg="blue")
            self.guess_label.config(bg="blue")
            #self.welcome_label.config(bg="blue")
        if current == "correct":
            self.game_window.configure(bg="green")
            #self.welcome_label.config(bg="green")
            self.guess_label.config(text="Congratulations! You guessed it!", fg="white", bg="green")
    def _create_widgets(self):
        self.game_frame = tk.Frame(self.game_window)
        self.guess_label = tk.Label(self.game_frame, text="Enter your guess (1-100):", font=self.Fonts[0], fg="black")
        self.guess_input = tk.Entry(self.game_frame)
        self.submit_button = tk.Button(self.game_frame, text="Submit", command=self._submit_guess)
    def _layout_widgets(self):
        self.game_frame.pack()
        self.guess_label.grid(row=0, column=0, columnspan=2)
        self.guess_input.grid(row=1, column=0)
        self.submit_button.grid(row=1, column=1)
    def _game_window(self, name):
        self.game_window = tk.Toplevel(self.root)
        self.game_window.title("Game Window")
        self.game_window.geometry("600x500")
        self.welcome_label = tk.Label(self.game_window, text=F"Welcome {name}", font=self.Fonts[0], fg="black")
        self.welcome_label.pack()
    
    def _submit_guess(self):
        value = self.guess_input.get()
        if not value.isdigit() or not (1 <= int(value) <= 100):
            self.guess_input.delete(0, tk.END)
            self.guess_label.config(text="Invalid input! Enter a number 1-100.", fg="red")
            self.guess_label.after(2000, lambda: self.guess_label.config(text="Enter your guess (1-100):", fg="black"))
        else:
            guess = int(value)
            self.guess_input.delete(0, tk.END)
            self._check_guess(guess)
            