# Program racuna prosek brojeva koje on unosi

brbroj = eval(input("Koliko zelite brojeva?: "))
a = brbroj
suma = 0

while brbroj != 0:

    unos = eval(input("Unesite broj: "))
    suma += unos

    brbroj -= 1
    
prosek = suma / a
print(f"Resenje: {prosek}")