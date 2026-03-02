import tkinter as tk
from tkinter.font import Font
import random
class BlazeOrFreeze:
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
            
    