# generati secventa de 8 biti pentru a reprezenta o succesiune de numere, si afisati si numarul de caractere 0 si 1
l = " ".join(bin(n)[2:].rjust(8, '0') for n in range(0,4))  #2
print(l)
l2=" ".join(hex(n)[2:] for n in range(ord('a'), ord('a')+26)) #1
print(l2)