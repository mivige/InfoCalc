import tkinter as tk
from tkinter import ttk
from calculations.entropy import calcola_entropia
from calculations.avg_length import calcola_lunghezza_media
from calculations.efficiency import calcola_efficienza
from utils.validators import validate_lengths_and_probabilities, validate_probabilities

def start_app():
    def esegui_calcolo():
        scelta = combo_scelta.get()

        if scelta == "Entropy":
            prob_input = entry_input.get()
            probabilita = [float(p) for p in prob_input.split(',')]
            if not validate_probabilities(probabilita):
                label_risultato.config(text="Error: Incorrect probabilities.")
                return
            risultato = calcola_entropia(probabilita)
            label_risultato.config(text=f"Entropy: {risultato:.6f} bits")
        
        elif scelta == "Average Length":
            lungh_input = entry_input.get()
            prob_input = entry_prob.get()
            lunghezze = [int(l) for l in lungh_input.split(',')]
            probabilita = [float(p) for p in prob_input.split(',')]
            if not validate_lengths_and_probabilities(lunghezze, probabilita):
                label_risultato.config(text="Error: Lengths or probabilities unvalid.")
                return
            risultato = calcola_lunghezza_media(lunghezze, probabilita)
            label_risultato.config(text=f"Average Length: {risultato:.6f}")
        
        elif scelta == "Efficiency":
            entropia = float(entry_input.get())
            lunghezza_media = float(entry_prob.get())
            risultato = calcola_efficienza(entropia, lunghezza_media)
            label_risultato.config(text=f"Efficiency: {risultato:.6f}")


    def aggiorna_etichette(*args):
        scelta = combo_scelta.get()
        if scelta == "Entropy":
            label_input.config(text="Insert probabilities:")
            label_prob.config(text="")
            entry_prob.grid_remove()
        elif scelta == "Average Length":
            label_input.config(text="Insert lengths:")
            label_prob.config(text="Insert probabilities:")
            entry_prob.grid()
        elif scelta == "Efficiency":
            label_input.config(text="Insert entropy:")
            label_prob.config(text="Insert average length:")
            entry_prob.grid()
    # Creazione della finestra principale e dei widget come nel file sorgente fornito

    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Calculator for Information Theory")
    root.geometry("600x400")
    root.resizable(False, False)

    # Creazione dei widget
    frame = ttk.Frame(root, padding="20")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(frame, text="Select operation:").grid(column=0, row=0, sticky=tk.W)
    combo_scelta = ttk.Combobox(frame, values=["Entropy", "Average Length", "Efficiency"])
    combo_scelta.grid(column=1, row=0)
    combo_scelta.set("Entropy")
    combo_scelta.bind("<<ComboboxSelected>>", aggiorna_etichette)

    label_input = ttk.Label(frame, text="Insert probabilities:")
    label_input.grid(column=0, row=1, sticky=tk.W)
    entry_input = ttk.Entry(frame, width=40)
    entry_input.grid(column=1, row=1)

    label_prob = ttk.Label(frame, text="")
    label_prob.grid(column=0, row=2, sticky=tk.W)
    entry_prob = ttk.Entry(frame, width=40)
    entry_prob.grid(column=1, row=2)
    entry_prob.grid_remove()

    ttk.Button(frame, text="Calculate", command=esegui_calcolo).grid(column=1, row=3)

    label_risultato = ttk.Label(frame, text="")
    label_risultato.grid(column=0, row=4, columnspan=2, pady=(20, 0))

    # Inizializza le etichette
    aggiorna_etichette()

    root.mainloop()
