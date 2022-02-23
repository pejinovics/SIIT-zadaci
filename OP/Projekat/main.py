import dodatna_oprema
import korisnici
import apartmani
import rezervacije


def izlaz():
    print("Izlazak iz aplikacije. ")


def submenu3(trenutni_korisnik):

    rezervacije.update_rez()
    while True:
        print("=" * 50)
        print("Meni aplikacije za administratora ")
        print("=" * 50)
        print("Ponuđene opcije:")
        print("1. Pregled aktivnih apartmana. ")
        print("2. Pretraga apartmana. ")
        print("3. Višekriterijumska pretraga apartmana. ")
        print("4. Prikaz 10 najpopularnijih gradova. ")
        print("5. Pretraga rezervacija. ")
        print("6. Registracija novih domaćina. ")
        print("7. Kreiranje dodatne opreme. ")
        print("8. Brisanje dodatne opreme. ")
        print("9. Blokiranje korisnika. ")
        print("10. Odblokiranje korisnika. ")
        print("11. Izveštavanje. ")
        print("12. Odjava sa sistema. ")
        print("x. Izlaz iz aplikacije. ")
        user_input = input(">> ")

        if user_input in ['1','2','3','4','5','6','7', '8','9', '10', '11', '12', 'x', 'X']:

            if user_input == '1':
                apartmani.pregled_aktivnih()
            elif user_input == '2':
                apartmani.pregled_apartmana()
            elif user_input == '3':
                apartmani.visestruka_pretraga()
            elif user_input == '4':
                apartmani.najpopularniji()
            elif user_input == '5':
                rezervacije.pretraga_admin_rezervacije()
            elif user_input == '6':
                korisnici.registruj("Domacin")
            elif user_input == '7':
                dodatna_oprema.dodaj_opremu()
            elif user_input == '8':
                apartmani.brisanje_dodatne_opreme()
            elif user_input == '9':
                korisnici.blokiraj_korisnika()
                pass
            elif user_input == '10':
                korisnici.odblokiraj_korisnika()
                pass
            elif user_input == '11':
                apartmani.izvestavanje()
                pass
            elif user_input == '12':
                submenux()
            else:
                izlaz()
                quit()
        else:
            print("Odabrali ste nepostojeću opciju")


def submenu1(trenutni_korisnik):

    rezervacije.update_rez()
    while True:
        print("=" * 50)
        print("Meni aplikacije za gosta ")
        print("=" * 50)
        print("Ponuđene opcije:")
        print("1. Pregled aktivnih apartmana. ")
        print("2. Pretraga apartmana. ")
        print("3. Višekriterijumska pretraga apartmana. ")
        print("4. Prikaz 10 najpopularnijih gradova. ")
        print("5. Rezervisanje apartmana. ")
        print("6. Pregled rezervacija. ")
        print("7. Poništavanje rezervacija. ")
        print("8. Odjava sa sistema. ")
        print("x. Izlaz iz aplikacije. ")
        user_input = input(">> ")

        if user_input in ['1','2','3','4','5','6','7', '8','x', 'X']:

            if user_input == '1':
                apartmani.pregled_aktivnih()
            elif user_input == '2':
                apartmani.pregled_apartmana()
            elif user_input == '3':
                apartmani.visestruka_pretraga()
            elif user_input == '4':
                apartmani.najpopularniji()
            elif user_input == '5':
                rezervacije.rezervisanje_apartmana(trenutni_korisnik)
            elif user_input == '6':
                rezervacije.pregled_rezervacija(trenutni_korisnik)
            elif user_input == '7':
                rezervacije.ponistavanje_rezervacija(trenutni_korisnik)
            elif user_input == '8':
                submenux()
            else:
                izlaz()
                quit()
        else:
            print("Odabrali ste nepostojeću opciju")


def submenu2(trenutni_korisnik):

    rezervacije.update_rez()
    while True:
        print("=" * 50)
        print("Meni aplikacije za domaćina ")
        print("=" * 50)
        print("Ponuđene opcije:")
        print("1. Pregled aktivnih apartmana. ")
        print("2. Pretraga apartmana. ")
        print("3. Višekriterijumska pretraga apartmana. ")
        print("4. Prikaz 10 najpopularnijih gradova. ")
        print("5. Dodavanje apartmana. ")
        print("6. Izmena podataka o apartmanu. ")
        print("7. Brisanje apartmana. ")
        print("8. Pregled rezervacija. ")
        print("9. Potvrda ili odbijanje rezervacija. ")
        print("10. Odjava sa sistema. ")
        print("x. Izlaz iz aplikacije. ")
        user_input = input(">> ")

        if user_input in ['1','2','3','4','5','6','7', '8','9','10','x', 'X']:

            if user_input == '1':
                apartmani.pregled_aktivnih()
            elif user_input == '2':
                apartmani.pregled_apartmana()
            elif user_input == '3':
                apartmani.visestruka_pretraga()
            elif user_input == '4':
                apartmani.najpopularniji()
            elif user_input == '5':
                apartmani.dodaj_apartman(trenutni_korisnik)
            elif user_input == '6':
                apartmani.izmena_apartman(trenutni_korisnik)
            elif user_input == '7':
                apartmani.brisi_apartman(trenutni_korisnik)
            elif user_input == '8':
                rezervacije.pregled_nepotvrdjene(trenutni_korisnik)
            elif user_input == '9':
                rezervacije.potvrda_odbijanje()
            elif user_input == '10':
                submenux()
            else:
                izlaz()
                quit()
        else:
            print("Odabrali ste nepostojeću opciju")


def submenux():

    while True:
        print("=" * 50)
        print("Glavni meni aplikacije")
        print("=" * 50)
        print("Ponuđene opcije:")
        print("1. Prijava na sistem. ")
        print("2. Pregled aktivnih apartmana. ")
        print("3. Pretraga apartmana. ")
        print("4. Višekriterijumska pretraga apartmana. ")
        print("5. Prikaz 10 najpopularnijih gradova. ")
        print("x. Izlaz iz aplikacije. ")
        user_input = input(">> ")

        if user_input in ['1','2','3','4','5','x', 'X']:
            if user_input == '1':
                uloga, trenutni_korisnik = korisnici.login()
                if uloga:
                    if uloga == "Gost":
                        print("Gost")
                        uloga == "Gost"
                        submenu1(trenutni_korisnik)
                    elif uloga == "Domacin":
                        print("Domacin")
                        uloga == "Domacin"
                        submenu2(trenutni_korisnik)
                    else:
                        print("Admin")
                        uloga == "Admin"
                        submenu3(trenutni_korisnik)

            elif user_input == '2':
                apartmani.pregled_aktivnih()
            elif user_input == '3':
                apartmani.pregled_apartmana()
            elif user_input == '4':
                apartmani.visestruka_pretraga()
            elif user_input == '5':
                apartmani.najpopularniji()
            else:
                izlaz()
                quit()
        else:
            print("Odabrali ste nepostojeću opciju")


def menu():

    while True:
        print("=" * 50)
        print("Glavni meni aplikacije")
        print("=" * 50)
        print("Ponuđene opcije:")
        print("1. Prijava na sistem. ")
        print("2. Pregled aktivnih apartmana. ")
        print("3. Pretraga apartmana. ")
        print("4. Višekriterijumska pretraga apartmana. ")
        print("5. Prikaz 10 najpopularnijih gradova. ")
        print("6. Registracija. ")
        print("x. Izlaz iz aplikacije. ")
        user_input = input(">> ")

        if user_input in ['1','2','3','4','5','6','x', 'X']:

            if user_input == '1':

                uloga,trenutni_korisnik = korisnici.login()
                if uloga:
                    if uloga == "Gost":
                        print("Gost")
                        uloga == "Gost"
                        submenu1(trenutni_korisnik)
                    elif uloga == "Domacin":
                        print("Domacin")
                        uloga == "Domacin"
                        submenu2(trenutni_korisnik)
                    else:
                        print("Admin")
                        uloga == "Admin"
                        submenu3(trenutni_korisnik)
            elif user_input == '2':
                apartmani.pregled_aktivnih()
            elif user_input == '3':
                apartmani.pregled_apartmana()
            elif user_input == '4':
                apartmani.visestruka_pretraga()
            elif user_input == '5':
                apartmani.najpopularniji()
            elif user_input == '6':
                korisnici.registruj("Gost")
                submenux()
            else:
                izlaz()
                quit()

        else:
            print("Odabrali ste nepostojeću opciju")


if __name__ == '__main__':
    menu()
