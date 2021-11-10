# Ovaj program pita odmah na pocetku koristika da li zeli da unosi broj ili da izadje zatim racuna prosek unetih brojeva

suma = 0
brel = 0

unos = input("Unesite broj ['x'  za izlazak]: ")

while unos != "x":
    x = eval(unos)
    suma += x
    brel += 1
    unos = input("Unesite broj ['x'  za izlazak]: ")

if brel > 0:
    prosek = suma / brel
    print(f"Prosek unetih elemenata je: {prosek: 10.2f}")

print("Niste uneli nijedan broj")