# chaos.py
# Program ilustruje haoticno ponasanje :)

print("Ovaj program ilustruje haoticno ponasanje")
x = eval(input("Unesite broj izmedju 0 i 1: "))
y = eval(input("Unesite broj izmedju 0 i 1: "))
for i in range(20):
    x = 2.0 * x * (1 - x)
    y = 2.0 * x * (1 - x)
    print(f"{x:<20.10}   |   {y:>20.10}")

