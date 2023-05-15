import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, bg_color="gray20", width=200)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="top", fill="x")

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Navigation",
                                                    compound="left", font=ctk.CTkFont(size=15, weight="bold"), fg_color="white")
        self.navigation_frame_label.pack(side="left", padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                    fg_color="white", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w")
        self.home_button.pack(side="top", fill="x", pady=(20, 0))

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                        fg_color="white", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w")
        self.frame_2_button.pack(side="top", fill="x", pady=(5, 0))

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                        fg_color="white", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w")
        self.frame_3_button.pack(side="top", fill="x", pady=(5, 0))
