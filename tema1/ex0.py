# scrieti un algoritm care calculeaza suma primelor n numere naturale

def suma_primele_n_numere(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

n = int(input("Introduceți n: "))
print(f"Suma primelor {n} numere naturale este: {suma_primele_n_numere(n)}")
