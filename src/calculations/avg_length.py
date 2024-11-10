def calcola_lunghezza_media(lunghezze, probabilita):
    return sum(l * p for l, p in zip(lunghezze, probabilita))