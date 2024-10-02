# InfoCalc: Calcolatrice per la Teoria dell'Informazione 

InfoCalc è una calcolatrice interattiva basata su Python che ti permette di calcolare facilmente l'entropia, la lunghezza media e l'efficienza secondo i principi della teoria dell'informazione. Sfrutta una semplice interfaccia grafica creata con `Tkinter`, ideale per studenti, ricercatori o appassionati di teoria dell'informazione.

---

## Funzionalità

- **Calcolo dell'entropia**: Fornisce l'entropia di una distribuzione di probabilità.
- **Calcolo della lunghezza media**: Determina la lunghezza media di un codice dato un insieme di lunghezze e probabilità.
- **Calcolo dell'efficienza**: Calcola l'efficienza di un codice in base all'entropia e alla lunghezza media.

## Come usare InfoCalc

1. Seleziona l'operazione che desideri eseguire (Entropia, Lunghezza media o Efficienza) dal menu a tendina.
2. Inserisci i valori richiesti:
   - Per l'entropia: inserisci una lista di probabilità separate da virgola (es. `0.2, 0.3, 0.5`).
   - Per la lunghezza media: inserisci una lista di lunghezze e una lista di probabilità corrispondenti (es. lunghezze: `1, 2, 3`, probabilità: `0.2, 0.3, 0.5`).
   - Per l'efficienza: inserisci il valore dell'entropia e la lunghezza media.
3. Premi **Calcola** per visualizzare il risultato.

## Installazione

1. Scarica il file .exe da questo repository.

2. Esegui il file .exe facendo doppio clic. Non è necessario installare Python.

---

## Esempi di utilizzo

### Entropia

Inserisci le probabilità:  
```
0.35, 0.15, 0.50
```

Risultato:  
```
Entropia: 1.440645 bit
```

### Lunghezza media

Inserisci le lunghezze:  
```
2, 3, 4, 4, 1
```

Inserisci le probabilità:  
```
0.20, 0.15, 0.05, 0.15, 0.45
```

Risultato:  
```
Lunghezza media: 2.100000
```

### Efficienza

Inserisci l'entropia:  
```
2.01997
```

Inserisci la lunghezza media:  
```
2.1
```

Risultato:  
```
Efficienza: 0.961890
```

---

## Contribuire
Le pull request sono benvenute! Se hai suggerimenti o idee su come migliorare il progetto, sentiti libero di aprire un'issue o contribuire direttamente.
