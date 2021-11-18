# Korisnik unosi broj zatim ga program pita da li zeli da nastavi i prilikom odabira za ne izbacuje prosek do tad unetih brojeva

def main():

    suma = 0
    i = 0
    noviunos = " "

    while noviunos !=  "Ne":

        unos = eval(input("Unesite broj: "))
        suma += unos
        i += 1

        noviunos = (input("Jos? Ne za izlaz enter za nastavak: "))

    prosek = suma / i
    print(f"Prosek elemenata je: {prosek}")

if __name__ == "__main__":
    main()