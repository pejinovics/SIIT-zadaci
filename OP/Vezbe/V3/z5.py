# Program racuna P i V sfere za dati poluprecnik

from math import pi
unos = eval(input("Unesite poluprecnik: "))

zapremina = 4 / 3 * unos ** 3 * pi
povrsina = 4 * pi * unos ** 2

print(f"Povrsina je: {povrsina}")
print(f"Zapremina je: {zapremina}")

