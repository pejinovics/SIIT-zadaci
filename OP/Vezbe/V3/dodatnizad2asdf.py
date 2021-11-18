# Proveri da li je godina prestupna. Godina je prestupna ako je deljiva sa 4 a nije deljiva sa 100 ili je deljiva sa 400.

def main():

    while True:

        unos = eval(input("Unesi godinu: "))

        if unos > 0:
            break
        print("Ponovite unos, unesite pozitivan broj")

    if (unos % 4 == 0 and unos % 100 != 0) or unos % 400 == 0:
        print("Uneta godina je prestupna")
    else:
        print("Nije prestupna")

if __name__ == "__main__":
    main()

    while True:

            unos = eval(input("Unesite 1 za kamen, 2 za makaze ili 3 za list")) 
            if unos == 1 or unos == 2 or unos == 3:
                break
            print("Niste dobar broj uneli, ponovite unos")