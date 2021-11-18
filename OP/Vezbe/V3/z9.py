# Program racuna cenu sa dostavom kafe

cena_kafe = 105
cena_porudzbina = 18
troskovi = 15

unos = eval(input("Unesite koliko kilogram zelite: "))

cena = cena_kafe * unos + cena_porudzbina * unos + troskovi

print(f"Vasa cena je: {cena}")