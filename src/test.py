import os
import time
from tinytag import TinyTag
import tkinter as tk
from tkinter import filedialog, ttk
from customtkinter import CTkButton
import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.music_file = None
        self.music_length = None  # in seconds
        self.is_paused = False
        self.play_button = CTkButton(master=root, text="Play", command=self.play_pause_music)
        self.browse_button = CTkButton(master=root, text="Browse", command=self.browse_files)
        self.song_label = tk.Label(master=root, text="No song selected")
        self.volume_slider = ttk.Scale(master=root, from_=0, to=1, length=500, orient="horizontal", command=self.set_volume)
        self.volume_slider.set(1)  # default volume
        self.progress_bar = ttk.Progressbar(master=root, length=500, mode='determinate')
        self.time_label = tk.Label(master=root, text="00:00 / 00:00")
        self.play_button.pack()
        self.browse_button.pack()
        self.song_label.pack()
        self.volume_slider.pack()
        self.progress_bar.pack()
        self.time_label.pack()
        self.update_progress()  # start the update loop

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def pause_music(self):
        if self.music_file:
            pygame.mixer.music.pause()

    def unpause_music(self):
        if self.music_file:
            pygame.mixer.music.unpause()

    def play_pause_music(self):
        if self.music_file:
            if self.is_paused:
                self.unpause_music()
                self.play_button.configure(text="Pause")
                self.is_paused = False
            else:
                self.pause_music()
                self.play_button.configure(text="Play")
                self.is_paused = True

    def browse_files(self):
        self.music_file = filedialog.askopenfilename(filetypes=[('Audio Files', '*.mp3')])
        if self.music_file:
            tag = TinyTag.get(self.music_file)
            song_title = tag.title if tag.title else os.path.basename(self.music_file)
            self.music_length = tag.duration
            self.progress_bar["maximum"] = self.music_length
            self.song_label.config(text=f"Playing: {song_title}")
            self.play_button.configure(text="Pause")
            self.play_music()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def update_progress(self):
        if pygame.mixer.music.get_busy():
            # music is playing, update the progress bar to the current music position
            self.progress_bar["value"] = pygame.mixer.music.get_pos() / 1000  # convert milliseconds to seconds
            current_time = time.strftime('%M:%S', time.gmtime(pygame.mixer.music.get_pos() / 1000))
            total_time = time.strftime('%M:%S', time.gmtime(self.music_length))
            self.time_label.config(text=f"{current_time} / {total_time}")
        self.root.after(1000, self.update_progress)  # update progress every second

root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()
