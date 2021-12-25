# Napiši program za registrovanje korisnika. 
# Program teba da omogući korisniku da unese korisničko ime i lozinku. 
# Informacije o korisniku čuvaju se u tekstualnom fajlu.

def main():

    unos = eval(input("Unesite broj korisnika: "))
    fajl = open("../V4/korisnici1.txt", "a")

    while unos:

        korisnicko_ime = input("Unesite korisnicko ime: ")
        lozinka = input("Unesite lozinku: ")

        fajl.write(korisnicko_ime + '|' + lozinka + '\n')

        unos -= 1

    fajl.close()
    
if __name__ == "__main__":

    main()    
    
