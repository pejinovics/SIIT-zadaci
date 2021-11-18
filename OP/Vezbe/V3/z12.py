# Racunanje Epakta

year = eval(input("Unesite 4-cifrenu godinu: "))
c = year / 100
epakt = (8 + c/4 - c + ((8*c + 13)/25) + 11*(year%19))%30

print(f"Epakt je {epakt}")