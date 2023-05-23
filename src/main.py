import tkinter as tk
import customtkinter as ctk
from Nav import Navbar
from socket import *
from threading import *
from tkinter import *

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))


def get_window_size():
    window.update()
    width = window.winfo_width()
    height = window.winfo_height()
    print("Window size: {} x {}".format(width, height))


window= ctk.CTk()
window.geometry("768x576")
window.wm_minsize(width=522, height=492)

window.after(100, get_window_size)




def play_music():
    print("Play")

def forward():
    get_window_size()
def backward():
    pass

def volume(value):
    print(value)

def fillWindow():
    # Ajout de la barre de play song
    play_song_frame = tk.Frame( bg="white", height=window.winfo_height()/2.5)
    play_song_frame.pack_propagate(0)
    play_song_frame.pack(fill=tk.X, pady=window.winfo_height()/10, padx=30)
    play_song_label = tk.Label(play_song_frame, bg="white")
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
    
    # tchat     
    chat_frame = tk.Frame(width= window.winfo_width(), height=400)
    chat_frame.pack(side=tk.RIGHT, anchor=tk.SE, padx=30, pady=10)
    chat_frame.pack_propagate(0)
    chat_label = tk.Label(chat_frame, text="Live Chat")
    
    chat_label.pack(padx=window.winfo_width()/100, pady=10)


    # Next songs
    upcoming_songs_frame = tk.Frame( bg="white", width=window.winfo_width(), height=400)
    upcoming_songs_frame.pack(side=tk.LEFT, anchor=tk.SW, padx=30, pady=10)
    upcoming_songs_frame.pack_propagate(0)
    upcoming_songs_frame = tk.Label(upcoming_songs_frame, text="Next sounds ")
    upcoming_songs_frame.pack(padx=window.winfo_width()/100, pady=10)

window.title('BeatEvent')

def tchat_area():
    chat_frame = tk.Frame(width= window.winfo_width(), height=400)
    chat_frame.pack(side=tk.RIGHT, anchor=tk.SE, padx=30, pady=10)
    chat_frame.pack_propagate(0)
    chat_label = tk.Label(chat_frame, text="Live Chat")
    txtMessages = Text(chat_frame, width=50)
    txtMessages.grid(row=0, column=0, padx=10, pady=10)

    txtYourMessage = Entry(chat_frame, width=50)
    txtYourMessage.insert(0,"Your message")
    txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

    def sendMessage():
        clientMessage = txtYourMessage.get()
        txtMessages.insert(END, "\n" + "You: "+ clientMessage)
        clientSocket.send(clientMessage.encode("utf-8"))

    btnSendMessage = Button(chat_frame, text="Send", width=20, command=sendMessage)
    btnSendMessage.grid(row=2, column=0, padx=10, pady=10)
    chat_label.pack(padx=window.winfo_width()/100, pady=10)
    
    def recvMessage():
        while True:
            serverMessage = clientSocket.recv(1024).decode("utf-8")
            print(serverMessage)
            txtMessages.insert(END, "\n"+serverMessage)
    
    recvThread = Thread(target=recvMessage)
    recvThread.daemon = True
    recvThread.start()
    

window.after(100, fillWindow())
# window.after(100, tchat_area())
window.mainloop()


