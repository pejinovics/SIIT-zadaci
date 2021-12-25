# Napiši program koji kombinuje sadržaj dva fajla i snima ga u treći fajl. 
# U prvom fajlu se nalaze korisnička imena i lozinke prodavaca, 
# a u drugom fajlu se nalaze nizovi cena artikala koje su prodavci prodali.

def main():

    fajl1 = open("../V4/korisnici1.txt", "r")
    fajl2 = open("../V4/racuni1.txt", "r")

    suma = 0
    n = 0

    a = fajl1.readline()
    b = fajl2.readline()

    while a:

        ime = a.split("|")[0]
        for i in b.split("|"):
            n += 1
            suma += eval(i)
        prosek = suma / n
        print(f"{ime}   |   {suma:.2f}  | {prosek:.2f}") 
        prosek = 0
        suma = 0
        n = 0

        a = fajl1.readline()
        b = fajl2.readline()

    fajl1.close()
    fajl2.close()

if __name__ == "__main__":

    main()  