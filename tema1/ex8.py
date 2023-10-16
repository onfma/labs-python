# scrieti un algoritm care calculeaza aria aproximativa a unei suprafete determinata de o secventa de valori y si axa OX

def calculeaza_aria_dreptunghiuri(y, dx):
    aria = 0
    for valoare in y:
        aria += valoare * dx
    return aria

# Exemplu de utilizare
y = [2, 4, 1, 3]  # Secvența de valori y
dx = 1  # Lățimea fiecărui dreptunghi (intervalul pe axa OX)
print(f"Aria aproximativă este: {calculeaza_aria_dreptunghiuri(y, dx)}")
