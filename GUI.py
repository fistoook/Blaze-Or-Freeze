import tkinter as tk
from tkinter.font import Font
from GameLogic import BlazeOrFreeze as BOF

class BlazeOrFreezeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.GameLogic = BOF()
        
        self.Fonts = [Font(family="Arial", size=16, weight="bold", slant="italic")]
        self.Font_colors = ["red", "black", "blue"]

        self._create_widgets()
        self._layout_widgets()
        
    
    def run(self):
        self.root.mainloop()

    def _create_widgets(self):
        self.title_grid = tk.Frame(self.root)
        self.name_input_grid = tk.Frame(self.root)
        self.name_label = tk.Label(self.name_input_grid, text="Enter your username:")
        self.name_input = tk.Entry(self.name_input_grid)
        self.send_button = tk.Button(self.name_input_grid, text="send", command=self._send_name)

        self.play_button = tk.Button(self.root)

    def _layout_widgets(self):
        self._style_root()
        self.title_grid.pack()
        for i, word in enumerate(['BLAZE', 'OR', 'FREEZE']):
            lbl = tk.Label(self.title_grid, text=word, font=self.Fonts[0], fg=self.Font_colors[i])
            lbl.grid(row=i, column=i)

        self.name_label.grid(row=0, column=0, columnspan=2)
        self.name_input.grid(row=1, column=0)
        self.send_button.grid(row=1,column=1)
        self.name_input_grid.pack()

    def _style_root(self):
        self.root.update_idletasks()
        self.root.title("Main Menu")
        self._center_window()

    def _center_window(self, width=600, height=500):
        self.root.update_idletasks()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(f"{int(width)}x{int(height)}+{x}+{y}")

    def _send_name(self):
        name = self.name_input.get()
        self.name_input.delete(0, tk.END)
        if not name:
            current_text = self.name_label["text"]
            self.name_label.after(3000, lambda: self._config_label(self.name_label, current_text))
            self.name_label.config(text="Invalid Name! enter a valid name:")

    def _config_label(self, label, text):
        label.config(text=text)
        

if __name__ == "__main__":
    myApp = BlazeOrFreezeGUI()
    myApp.run()