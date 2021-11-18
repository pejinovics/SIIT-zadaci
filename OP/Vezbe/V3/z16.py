# Program racuna zbir kvadrata prvih n brojeva

unos = eval(input("Unesite broj: "))
a = unos
suma = 0

for i in range(unos):
    suma += unos ** 2
    unos -= 1

print(f"Zbir prvih {a} brojeva je {suma}")