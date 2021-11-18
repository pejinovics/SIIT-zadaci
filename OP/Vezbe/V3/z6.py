# Program racuna cenu pice po kvadratnom centimetru za dati poluprecnik i cenu cele pice

from math import pi

unosR = eval(input("Unesi poluprecnik pizze: "))

cena50 = (25 ** 2 * pi) / 2
cena = (unosR ** 2 * pi) / 2
print(f"Cena vase pizze je: {cena}")