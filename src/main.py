import tkinter as tk
import customtkinter as ctk
from Nav import Navbar

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


window= ctk.CTk()
play_song_frame = tk.Frame( bg="white")
play_song_frame.pack(fill=tk.X, pady=10, padx=30)

# Ajout de la barre de play song
play_song_label = tk.Label(play_song_frame, text="Nom de la musique", bg="white")
play_song_label.pack(side=tk.LEFT, padx=10, pady=10)

# Tchat
chat_frame = tk.Frame( bg="white", width=200, height=200)
chat_frame.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)
chat_frame.pack_propagate(0)
chat_label = tk.Label(chat_frame, text="Live Chat")
chat_label.pack(padx=10, pady=10)

# Next songs
upcoming_songs_frame = tk.Frame( bg="white", width=200, height=200)
upcoming_songs_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)
upcoming_songs_frame.pack_propagate(0)
upcoming_songs_frame = tk.Label(upcoming_songs_frame, text="Next sounds ")
upcoming_songs_frame.pack(padx=10, pady=10)
window.title('BeatEvent')

window.mainloop()


