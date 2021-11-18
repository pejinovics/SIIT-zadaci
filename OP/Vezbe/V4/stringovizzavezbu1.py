# Na osnovu stringa neparne dužine veće od 7, ispiši srednja 3 karaktera: Primer: ulaz: “NekiPrimeri“, izlaz: “Pri“

def main():

    while True:

        unos = input("Unesite string neparne duzine vece od 7: ")
        if len(unos) > 7 and len(unos) % 2 == 1:
            break
        print("Unesite ponovo string")

    resenje = unos[len(unos) // 2 - 1] + unos[len(unos) // 2] + unos[len(unos) // 2 + 1]
    print(resenje)

if __name__ == "__main__":
    main()