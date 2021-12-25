# Formatiranje teksta

from os import replace


def main():

    fajl1 = open("../V4/tekst.txt", "r")
    fajl2 = open("../V4/formatiranTekst.txt", "w")

    a = fajl1.readline()

    while a:

        a.replace("  ", " ")
        a = fajl1.readline()

    naslov = fajl1.read().split("\n")[0].lower().capitalize()
    naslov.center(100)
    
    fajl1.close()
    fajl2.close()

if __name__ == "__main__":

    main() 




