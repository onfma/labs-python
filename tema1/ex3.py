# scrieti un algoritm care calculeaza rezultatul unei impartiri cu virgula, folosind doar numere intregi
# rezultatul se va afisa cu 100 de zecimale
from decimal import Decimal, getcontext

def divide_with_precision(a, b):
    getcontext().prec = 100
    result = Decimal(a) / Decimal(b)
    return result

a = 1
b = 13

print(divide_with_precision(a, b))
