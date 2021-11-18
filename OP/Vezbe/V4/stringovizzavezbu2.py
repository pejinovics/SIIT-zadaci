# Na osnovu 2 dobijena stringa kreirati novi tako da bude sastavljen od prvog,
# srednjeg i poslednjeg karaktera jednog i drugog stringa naizmenično.
# Pretpostaviti da stringovi imaju neparan broj karaktera i da su dužine veće od 2.
# Primer: string1: Lampica string2: Kokos izlaz: LKpkas

def main():

    while True:

        unos1 = input("Unesite string neparne duzine vece od 2: ")
        if len(unos1) > 2 and len(unos1) % 2 == 1:
            break
        print("Unesite ponovo string")

    while True:

        unos2 = input("Unesite string neparne duzine vece od 2: ")
        if len(unos2) > 2 and len(unos2) % 2 == 1:
            break
        print("Unesite ponovo string")

    rezstr = unos1[0] + unos2[0] + unos1[len(unos1) // 2] + unos2[len(unos2) // 2] + unos1[-1] + unos2[-1]

    print(rezstr)

if __name__ == "__main__":
    main()

    