# Program racuna zbir brojeva koje on unosi

brbroj = eval(input("Koliko zelite brojeva?: "))
suma = 0

while brbroj != 0:

    unos = eval(input("Unesite broj: "))
    suma += unos

    brbroj -= 1

print(f"Resenje: {suma}")