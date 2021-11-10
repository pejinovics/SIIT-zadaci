# Ovaj program prilikom svakog unosa korisnika pita za nastavak i ukoliko izabere izlaz ispisuje prosek unetih brojeva

suma = 0
brel = 0
pitanje = "Da"

while pitanje != "Ne":
    unos = eval(input("Unesite broj: "))
    suma += unos 
    brel += 1
    pitanje = input("Jos? [Enter za nastavak, Ne za izlaz]: ")

prosek = suma / brel

print(f"Prosek unetih elemenata je: {prosek: 10.2f}")
