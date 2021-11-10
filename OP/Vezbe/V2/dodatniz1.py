#Ovaj program pita korisnika za broj brojeva koliko ce unositi pa racuna njihov prosek

suma = 0
brbroj = eval(input("Unesite za koliko brojeva zelite da izracunate prosek: "))

for i in range(brbroj):
    unos = eval(input("Unesite broj: "))
    suma += unos

prosek = suma / brbroj
print(f"Prosek unetih brojeva je: {prosek: 10.2f}")