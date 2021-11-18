# Program treba da predstavi aproksimaciju pi izraza

unos = eval(input("Unesite broj: "))

n = 1
f = 3
a = unos//2
b = unos % 2
c = a + b
resenje = 0

while c != 0:
    resenje += 4 / n
    n += 4
    c -= 1

while a != 0:
    resenje -= 4 / f
    f += 4
    a -= 1

print(f"Resenje je {resenje}")