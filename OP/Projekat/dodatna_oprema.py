from tabulate import tabulate
import korisnici

def load(file_name="dodatna_oprema.txt"):

    with open(file_name, "r", encoding = "utf-8") as file:

        lines = file.readlines()
        global dodatna_oprema
        dodatna_oprema = {}
        for line in lines:
            user_data = line.replace("\n", "").split("|")
            user_dict = {
                    "sifra": user_data[0],
                    "naziv": user_data[1]
            }
            dodatna_oprema[user_dict["sifra"]] = user_dict


def int_provera(unos):

    try:
        unos = int(unos)
        return True

    except ValueError:
        print("Pretraga zahteva broj kao unos, ponovite unos")
        return False


def proveri(naziv):

    load("dodatna_oprema.txt")
    for i in dodatna_oprema.values():
        if naziv == i["naziv"]:
            print("Ovaj naziv se već koristi. ")
            return False
    return True


def proveri_sifra(sifra):

    load("dodatna_oprema.txt")
    for i in dodatna_oprema:
        if sifra == i:
            print("Ovaj šifra se već koristi. ")
            return False
    return True


def dodaj_opremu():

    load("dodatna_oprema.txt")
    print("=" *50)
    print("Unos šifre dodatne opreme. ")
    print("Šifra moraju biti brojevi, minimum tri broja. ")
    while True:
        print("=" * 50)
        print("Unesite šifru. ")
        sifra = input("<< ")
        if int_provera(sifra) and len(sifra) > 2 and proveri_sifra(sifra):
            break

    print("=" * 50)
    print("Naziv dodatne opreme. ")
    while True:
        print("=" * 50)
        print("Unesite naziv. ")
        naziv = input("<< ")
        nesto = naziv.replace(" ", "")
        if korisnici.provera_str_broj(nesto) and proveri(naziv):
            break

    rez = sifra + "|" + naziv + '\n'
    with open("dodatna_oprema.txt", "a", encoding="utf-8") as file:
        file.write(rez)


def ispis(tabele):

    header = ["Šifra dodatne opreme", "Naziv"]
    print(tabulate(tabele, header, tablefmt="simple"))


def brisi(sifra):

    load("dodatna_oprema.txt")
    rez = ""
    for i in dodatna_oprema.values():
        if i["sifra"] == sifra:
            temp = ""
        else:
            temp = i["sifra"] + "|" + i["naziv"] + '\n'
        rez += temp

    with open("dodatna_oprema.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def ispis_sve():

    load("dodatna_oprema.txt")
    tabele = []
    for i in dodatna_oprema.values():
        tabele.append([i["sifra"], i["naziv"]])

    ispis(tabele)


# dodaj_dodatnu_opremu()
# dodaj_opremu()
# brisanje_dodatne_opreme()
dodatna_oprema = {}