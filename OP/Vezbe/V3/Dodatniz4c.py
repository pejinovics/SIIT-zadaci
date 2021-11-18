# Korisnik unosi brojeve i bira x za izlaz i nakon toga se ispisuje prosek do tada unetih brojeva

def main():

    suma = 0
    i = 0
    unos = "0"
    a = 0

    while unos != "x":

        suma += eval(unos)
        unos = input("Unesite broj [x za izlaz]: ")
        i += 1
    
    prosek = suma / i
    print(f"Prosek elemenata je: {prosek}")

if __name__ == "__main__":
    main()