def validate_probabilities(probabilita):
    """
    Verifica che la lista di probabilità sia valida:
    - Tutti gli elementi devono essere numeri tra 0 e 1.
    - La somma delle probabilità deve essere 1 (con un piccolo margine per tollerare errori di arrotondamento).

    Args:
        probabilita (list of float): Lista di probabilità.

    Returns:
        bool: True se le probabilità sono valide, False altrimenti.
    """
    if not probabilita:
        return False
    
    # Verifica che ogni elemento sia un float tra 0 e 1
    if any(p < 0 or p > 1 for p in probabilita):
        return False

    # Verifica che la somma sia circa 1 (con tolleranza per errori di arrotondamento)
    return abs(sum(probabilita) - 1.0) < 1e-6


def validate_lengths_and_probabilities(lunghezze, probabilita):
    """
    Verifica che le liste di lunghezze e probabilità siano compatibili:
    - Devono avere la stessa lunghezza.
    - Le probabilità devono essere valide (usando validate_probabilities).

    Args:
        lunghezze (list of int): Lista di lunghezze.
        probabilita (list of float): Lista di probabilità.

    Returns:
        bool: True se le liste sono compatibili e valide, False altrimenti.
    """
    # Controlla che le liste abbiano la stessa lunghezza
    if len(lunghezze) != len(probabilita):
        return False
    
    # Controlla la validità delle probabilità
    return validate_probabilities(probabilita)
