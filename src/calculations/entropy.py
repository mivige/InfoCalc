import math

def calcola_entropia(probabilita):
    if len(probabilita) == 1:
        p = probabilita[0]
        if p == 1.0 or p == 0.0:
            return 0.0
        return p * math.log2(1/p) + (1 - p) * math.log2(1/(1-p))
    return sum(p * math.log2(1/p) for p in probabilita if p > 0)
