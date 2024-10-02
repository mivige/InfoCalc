import tkinter as tk
from tkinter import ttk
import math

def calcola_entropia(probabilita):
    if len(probabilita) == 1:
        p = probabilita[0]
        return p * math.log2(1/p) + (1 - p) * math.log2(1/(1-p))
    return sum(p * math.log2(1/p) for p in probabilita if p > 0)

def calcola_lunghezza_media(lunghezze, probabilita):
    return sum(l * p for l, p in zip(lunghezze, probabilita))

def calcola_efficienza(entropia, lunghezza_media):
    return entropia / lunghezza_media

def esegui_calcolo():
    scelta = combo_scelta.get()
    
    if scelta == "Entropia":
        prob_input = entry_input.get()
        probabilita = [float(p) for p in prob_input.split(',')]
        risultato = calcola_entropia(probabilita)
        label_risultato.config(text=f"Entropia: {risultato:.6f} bit")
    
    elif scelta == "Lunghezza media":
        lungh_input = entry_input.get()
        prob_input = entry_prob.get()
        lunghezze = [int(l) for l in lungh_input.split(',')]
        probabilita = [float(p) for p in prob_input.split(',')]
        risultato = calcola_lunghezza_media(lunghezze, probabilita)
        label_risultato.config(text=f"Lunghezza media: {risultato:.6f}")
    
    elif scelta == "Efficienza":
        entropia = float(entry_input.get())
        lunghezza_media = float(entry_prob.get())
        risultato = calcola_efficienza(entropia, lunghezza_media)
        label_risultato.config(text=f"Efficienza: {risultato:.6f}")

def aggiorna_etichette(*args):
    scelta = combo_scelta.get()
    if scelta == "Entropia":
        label_input.config(text="Inserisci le probabilità:")
        label_prob.config(text="")
        entry_prob.grid_remove()
    elif scelta == "Lunghezza media":
        label_input.config(text="Inserisci le lunghezze:")
        label_prob.config(text="Inserisci le probabilità:")
        entry_prob.grid()
    elif scelta == "Efficienza":
        label_input.config(text="Inserisci l'entropia:")
        label_prob.config(text="Inserisci la lunghezza media:")
        entry_prob.grid()

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice Teoria dell'Informazione")
root.geometry("600x400")
root.resizable(False, False)

# Creazione dei widget
frame = ttk.Frame(root, padding="20")
frame.place(relx=0.5, rely=0.5, anchor="center")

ttk.Label(frame, text="Scegli l'operazione:").grid(column=0, row=0, sticky=tk.W)
combo_scelta = ttk.Combobox(frame, values=["Entropia", "Lunghezza media", "Efficienza"])
combo_scelta.grid(column=1, row=0)
combo_scelta.set("Entropia")
combo_scelta.bind("<<ComboboxSelected>>", aggiorna_etichette)

label_input = ttk.Label(frame, text="Inserisci le probabilità:")
label_input.grid(column=0, row=1, sticky=tk.W)
entry_input = ttk.Entry(frame, width=40)
entry_input.grid(column=1, row=1)

label_prob = ttk.Label(frame, text="")
label_prob.grid(column=0, row=2, sticky=tk.W)
entry_prob = ttk.Entry(frame, width=40)
entry_prob.grid(column=1, row=2)
entry_prob.grid_remove()

ttk.Button(frame, text="Calcola", command=esegui_calcolo).grid(column=1, row=3)

label_risultato = ttk.Label(frame, text="")
label_risultato.grid(column=0, row=4, columnspan=2, pady=(20, 0))

# Inizializza le etichette
aggiorna_etichette()

# Avvio del loop principale
root.mainloop()
