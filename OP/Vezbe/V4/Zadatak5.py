# Napiši program koji kombinuje sadržaj dva fajla i snima ga u treći fajl. 
# U prvom fajlu se nalaze korisnička imena i lozinke prodavaca, 
# a u drugom fajlu se nalaze nizovi cena artikala koje su prodavci prodali.

def main():

    fajl1 = open("../V4/korisnici1.txt", "r")
    n = 0
    temp = ""

    for i in fajl1.readlines():
        n += 1

    fajl2 = open("../V4/racuni1.txt", "a")

    while n:

        unos = eval(input("Unesite broj prodatih artikala: "))

        while unos:

            cena = input("Unesite cenu: ")
            temp += cena + '|'

            unos -= 1

        fajl2.write(temp[:-1] + '\n')
        temp = ""
        n -= 1

    fajl1.close()
    fajl2.close()

if __name__ == "__main__":

    main()  

    