# futval.py
# Izracunava buduce stanje orocenog novca
# za rok od 10 godina

print("Ovaj program izracunava stanje stednog racuna", end =' ')
print("nakon isteka roka od n godina.")

godine = int(input("Unesite rok godina: "))

principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))

for i in range(godine):
    principal = principal * (1 + apr)

print(f"Stanje nakon {godine} godina:", principal)
