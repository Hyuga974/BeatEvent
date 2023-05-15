import tkinter as tk

from Nav import Navbar

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Play song
        self.play_song_frame = tk.Frame(self, bg="white")
        self.play_song_frame.pack(fill=tk.X)

        # Ajout de la barre de play song
        self.play_song_label = tk.Label(self.play_song_frame, text="Nom de la musique", bg="white")
        self.play_song_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Tchat
        self.chat_frame = tk.Frame(self, bg="white", width=200, height=200)
        self.chat_frame.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)
        self.chat_frame.pack_propagate(0)
        self.chat_label = tk.Label(self.chat_frame, text="Live Chat")
        self.chat_label.pack(padx=10, pady=10)

        # Next songs
        self.upcoming_songs_frame = tk.Frame(self, bg="white", width=200, height=200)
        self.upcoming_songs_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)
        self.upcoming_songs_frame.pack_propagate(0)
        self.upcoming_songs_frame = tk.Label(self.upcoming_songs_frame, text="Next sounds ")
        self.upcoming_songs_frame.pack(padx=10, pady=10)


window=tk.Tk()
app = Application(master=window)


window.title('BeatEvent')

window.mainloop()


