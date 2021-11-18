# Program racuna n-ti elemen Fibonacijevog niza

a = 1
b = 1
temp = 0

unos = -1

while unos <= 0:
    unos = eval(input("Unesi n-ti element: "))

    if unos < 0:
        print("Ne moze ovaj broj, mora pozitivan")


while unos != 2:
    temp = b
    b += a
    a = temp

    unos -= 1

print(f"Resenje je {b}") 
