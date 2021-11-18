# Korisnik bira broj brojeva koliko unosi zatim program racuna prosek unetih brojeva

def main():

    suma = 0
    unos = eval(input("Unesite koliko zelite brojeva da unesete: "))
    b = unos

    while unos:

        a = eval(input("Unesite broj: "))
        suma += a
        unos -= 1

    prosek = suma / b
    print(f"Prosek elemenata je: {prosek}")

if __name__ == "__main__":
    main()