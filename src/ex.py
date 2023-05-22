import tkinter as tk

def configure_grid(event):
    # Répartir l'espace de manière égale dans les cellules de la grille
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(1, weight=1)

window = tk.Tk()

# Création des deux Frame
frame1 = tk.Frame(window, bg="red")
frame2 = tk.Frame(window, bg="blue")

# Positionnement des Frame dans la grille avec un espacement
frame1.grid(row=1, column=0, sticky="nsew", padx=10)
frame2.grid(row=1, column=2, sticky="nsew", padx=10)

# Configuration de la grille
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)

# Appel de la fonction de configuration lorsque la fenêtre est redimensionnée
window.bind("<Configure>", configure_grid)

window.mainloop()
