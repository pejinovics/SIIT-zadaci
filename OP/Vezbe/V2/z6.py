

print("Ovaj program izracunava stanje stednog racuna")
print("nakon isteka roka od n godina.")

year = eval(input("Unesite broj godina: "))
principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))
inflation = eval(input("Unesite godisnju inflaciju: "))

for i in range(10):
    principal = principal * (1 + apr)
    principal = principal/(1 + inflation)

print(f"Stanje nakon {year} godina:", principal)
