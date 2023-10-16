# scrieti un algoritm care implementeaza radacina de ordin n dintr-un numar dat, 
# cu 50 de zecimale, utilizand doar calcule cu numere intregi, 
# dupa algorimtul prezentat aici: https://en.wikipedia.org/wiki/Nth_root
from decimal import Decimal, getcontext

def nth_root(n, x, precision=50):
    if n <= 0 or x < 0:
        raise ValueError("Radicalul trebuie să fie pozitiv și indicele trebuie să fie strict pozitiv.")
    
    x = Decimal(x)
    n = Decimal(n)
    precision = Decimal(10) ** (-precision)
    
    guess = x  # Alegem o valoare de pornire pentru rădăcină
    while True:
        next_guess = ((n - 1) * guess + x / (guess ** (n - 1))) / n
        if abs(next_guess - guess) < precision:
            return next_guess
        guess = next_guess


n = 3  # Indicele rădăcinii
x = 27  # Numărul din care se extrage rădăcina
print(nth_root(n, x, 50))
