import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import os

class customTitleBar(tk.Frame):
    def __init__(self, parent, controller, title="HOT&COLD"):
        # initialize the frame and set the parent and controller (main app) as attributes
        super().__init__(parent, bg="#2b2b2b", height=35)

        self.controller = controller
        self.title = title

        self.pack(fill="x")
        self.pack_propagate(False)  # Maintain fixed height

        self._create_widgets()
        self._bind_drag_events()


    def _create_widgets(self):
        # designing the left side of the title bar with the icon and title
        left_frame = tk.Frame(self, bg="#2b2b2b")
        left_frame.pack(side="left", padx=8)

        # Load and keep a reference to the icon
        try:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            icon_path = os.path.join(project_root, "assets", "images", "Hot&Cold-icon.png")
            self.icon_image = ImageTk.PhotoImage(Image.open(icon_path).resize((20, 20)))
            icon_label = tk.Label(left_frame, image=self.icon_image, bg="#2b2b2b")
            icon_label.pack(side="left", padx=4)
        except FileNotFoundError:
            self.icon_image = None

        self.title_label = tk.Label(
            left_frame,
            text=self.title,
            bg="#2b2b2b",
            fg="white",
            font=Font(family="Segoe UI", size=10)
        )
        self.title_label.pack(side="left", padx=4)
        
        # designing the right side of the title bar with the minimize and close buttons
        button_frame = tk.Frame(self, bg="#2b2b2b")
        button_frame.pack(side="right")

        # Minimize Button
        self.minimize_button = tk.Button(
            button_frame,
            text="—",
            bg="#2b2b2b",
            fg="white",
            font=Font(family="Segoe UI", size=12, weight="bold"),
            bd=0,
            padx=15,
            pady=2,
            relief="flat",
            cursor="hand2",
            command=self._minimize_window
        )
        self.minimize_button.pack(side="left")
        self._add_hover(self.minimize_button, "#3f3f3f")

        # Close Button
        self.close_button = tk.Button(
            button_frame,
            text="✕",
            bg="#2b2b2b",
            fg="white",
            font=Font(family="Segoe UI", size=10),
            bd=0,
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
            command=self.controller.destroy  # FIXED
        )
        self.close_button.pack(side="left")
        self._add_hover(self.close_button, "#e81123")

    def _add_hover(self, widget, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg="#2b2b2b"))

    def _minimize_window(self):
        self.controller.overrideredirect(False)
        self.controller.update_idletasks()
        self.controller.iconify()
        self.controller.bind("<Map>", self._restore_override)

    def _restore_override(self, event=None):
        if self.controller.state() == "normal":
            self.controller.overrideredirect(True)
            self.controller.unbind("<Map>")
    
    def _bind_drag_events(self):
        self.bind("<Button-1>", self._start_move)
        self.bind("<B1-Motion>", self._move_window)

        # Also bind to title label for smooth dragging
        self.title_label.bind("<Button-1>", self._start_move)
        self.title_label.bind("<B1-Motion>", self._move_window)
        
    def _start_move(self, event):
        self._x = event.x
        self._y = event.y

    def _move_window(self, event):
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.controller.geometry(f"+{x}+{y}")