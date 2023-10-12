# scrieti un program care calculeaza solutiile unui sistem de ecuatii de grad 1 cu cel mult 4 necunoscute

for x in range(0, 1000):
    for y in range(0, 1000):
        if 4*x+y==7 and 2*x+5*y==17:
            print(x, y)
            exit