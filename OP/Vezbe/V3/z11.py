# Rastojanje izmedju tacaka

from math import sqrt

tacka1x, tacka1y = eval(input("Unesite x i y koordinatu [, za odvajanje]: "))

tacka2x, tacka2y = eval(input("Unesite x i y koordinatu [, za odvajanje]: "))

resenje = (tacka2y - tacka1y) / (tacka2x - tacka1x)
razdaljina = sqrt(resenje)
print(f"Razdaljina je {razdaljina}")
