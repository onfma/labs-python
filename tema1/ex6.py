# Generati permutrea n pentru cuvinte cu p litre folosind un alfabet dat, n < len(alfabet)^p
from itertools import permutations

def generate_permutations(alphabet, p):
    if p > len(alphabet):
        raise ValueError("p trebuie să fie mai mic sau egal cu lungimea alfabetului.")
    
    perm_list = list(permutations(alphabet, p))
    return [''.join(perm) for perm in perm_list]

alfabet = "ABC"
lungime_permutare = 2
permutari = generate_permutations(alfabet, lungime_permutare)
for permutare in permutari:
    print(permutare)
