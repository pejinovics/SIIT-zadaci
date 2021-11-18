# Povrisna trougla

from math import sqrt

a = eval(input("Unesi stranicu: "))
b = eval(input("Unesi stranicu: "))
c = eval(input("Unesi stranicu: "))

s = (a + b + c) / 2

resenje = sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Resenje je: {resenje}")