# Program pomocu Njutnovog metoda pogadja koren

from math import sqrt

unos = eval(input("Unesite broj: "))
resenje = unos / 2
n = 0

while resenje != sqrt(unos):

    resenje = ((resenje + unos) / resenje) / 2
    resenje = eval(input("Probaj pogoditi koren broja: "))
    n += 1

print(f"Uspeli ste iz {n} pokusaja")