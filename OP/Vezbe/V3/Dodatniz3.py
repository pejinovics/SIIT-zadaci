# Napiši program koji od korisnika traži da unosi brojeve sve dok ne unese neparni broj.
# Kada korisnik unese neparni broj, izvršavanje programa se prekidai korisniku se ispisuje suma prethodno unetih (parnih) brojeva.

def main():

    suma = 0
    unos = eval(input("Unesite broj [neparni za izlaz]: "))

    while unos % 2 != 1:

        suma += unos
        unos = eval(input("Unesite broj [neparni za izlaz]: "))

    print(f"Suma unetih brojeva je: {suma}")

if __name__ == "__main__":
    main()
