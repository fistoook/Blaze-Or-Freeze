import customtkinter as ctk

class CustomLevelSlider(ctk.CTkFrame):
    def __init__(self, parent, command=None, **kwargs):
        super().__init__(parent, fg_color="transparent", border_width=0, **kwargs)
        self.command = command
        self.levels = [
            {"name": "Easy", "max_value": 10, "color": "#16A34A"},
            {"name": "Medium", "max_value": 100, "color": "#2563EB"},
            {"name": "Epic", "max_value": 1000, "color": "#6E00B3"},
        ]
        self.current_index = 0

        self._create_widgets()
        self._layout_widgets()
        self._apply_level(0, notify=False)

    def _create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="LEVEL", font=("Segoe UI", 14, "bold"))
        self.level_label = ctk.CTkLabel(self, text="", font=("Segoe UI", 18, "bold"))

        # Container frame to hold slider and level display
        self.container_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)

        self.track_frame = ctk.CTkFrame(self.container_frame, corner_radius=14, fg_color="transparent")

        self.slider = ctk.CTkSlider(
            self.track_frame,
            from_=0,
            to=2,
            number_of_steps=100,  # Smooth slider movement
            orientation="horizontal",
            command=self._on_slide,
            height=22,
            width=300,
            button_length=16,
        )

    def _layout_widgets(self):
        self.title_label.pack(pady=(0, 10))
        self.level_label.pack(pady=(0, 10), ipadx=10,ipady=10)
        self.container_frame.pack()

        # Track frame with horizontal slider
        self.track_frame.pack(fill="x", padx=10)

        # Only show the slider
        self.slider.pack(padx=8, pady=6)

    def _on_slide(self, value):
        snapped_index = int(round(float(value)))
        self._apply_level(snapped_index, notify=True)

    def _apply_level(self, index, notify):
        self.current_index = max(0, min(index, len(self.levels) - 1))
        self.slider.set(self.current_index)

        level = self.levels[self.current_index]
        self.slider.configure(
            progress_color=level["color"],
            button_color=level["color"],
            button_hover_color=self._darken(level["color"]),
        )

        self.level_label.configure(text_color=level["color"], text=f"{level["name"]}, 1-{level["max_value"]}")

        if notify and self.command:
            self.command(level["name"], level["max_value"])

    def _darken(self, hex_color, factor=0.8):
        hex_color = hex_color.lstrip("#")
        red, green, blue = [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]
        red = int(red * factor)
        green = int(green * factor)
        blue = int(blue * factor)
        return f"#{red:02x}{green:02x}{blue:02x}"

    def get_level(self):
        level = self.levels[self.current_index]
        return level["name"], level["max_value"]