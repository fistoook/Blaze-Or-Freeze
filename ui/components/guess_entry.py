import customtkinter as ctk
import tkinter as tk

class CustomEntry(ctk.CTkEntry):
    def __init__(self, master=None, on_enter=None, **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder_text = kwargs.pop("placeholder_text", "Enter Guess...")
        #try:
        #    self.placeholder_text = kwargs["placeholder_text"]
        #except KeyError:
        #    self.placeholder_text = "Enter Guess..."
        
        # set initial placeholder
        self.insert(0, self.placeholder_text)
        self.configure(text_color='grey')
        self.on_enter = on_enter # callback

        # bind events
        self.bind("<FocusIn>", self._on_focus_in)
        #self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<Return>", self._on_enter)

    def _on_focus_in(self, event):
        if self.get() == self.placeholder_text:
            self._clear()
            self.configure(text_color="grey")

    def _on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder_text)
            self.configure(text_color="grey") 

    def _on_enter(self, event):
        guess = self._get()
        if guess and guess != self.placeholder_text and self.on_enter:
            self.on_enter(guess)
        self._clear()  # clear entry for next guess

    def _get(self):
        current_text = super().get().strip()
        if current_text == self.placeholder_text:
            return ""
        return current_text
    
    def _clear(self):
        self.delete(0, tk.END)
        self.configure(text_color='grey')

    def _error_message(self, message):
        self._clear()
        self.configure(text_color='red', font=("Segoe UI", 14, "bold"))
        self.insert(0, message)
        self.after(2000, self._clear)