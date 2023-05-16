import tkinter as tk
import customtkinter as ctk
from Nav import Navbar

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


window= ctk.CTk()
window.geometry("768x576")
play_song_frame = tk.Frame( bg="white", height=500)
play_song_frame.pack(fill=tk.X, pady=10, padx=30)

# Ajout de la barre de play song
play_song_label = tk.Label(play_song_frame, bg="white")

def play_music():
    print("Play")

def forward():
    pass

def backward():
    pass

def volume(value):
    print(value)

# Buttons
skip_b = ctk.CTkButton(master=play_song_frame, text='|< ', width=1, command=backward)
skip_b.place(relx=0.07, rely=0.5, anchor=tk.CENTER)
play_button = ctk.CTkButton(master=play_song_frame, text=' > ', command=play_music, width=1)
play_button.place(relx=0.135, rely=0.5, anchor=tk.CENTER)
skip_f = ctk.CTkButton(master=play_song_frame, text=' >|', width=1, command=forward)
skip_f.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
slider = ctk.CTkSlider(master=play_song_frame, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.25, rely=0.7, anchor=tk.W)

play_song_label.pack(side=tk.LEFT, padx=10, pady=10)

# Tchat
chat_frame = tk.Frame( bg="white", width= window.winfo_width(), height=400)
chat_frame.pack(side=tk.RIGHT, anchor=tk.SE, padx=30, pady=10)
chat_frame.pack_propagate(0)
chat_label = tk.Label(chat_frame, text="Live Chat")
chat_label.pack(padx=10, pady=10)

# Next songs
upcoming_songs_frame = tk.Frame( bg="white", width=window.winfo_width(), height=400)
upcoming_songs_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=30, pady=10)
upcoming_songs_frame.pack_propagate(0)
upcoming_songs_frame = tk.Label(upcoming_songs_frame, text="Next sounds ")
upcoming_songs_frame.pack(padx=10, pady=10)
window.title('BeatEvent')

window.mainloop()


