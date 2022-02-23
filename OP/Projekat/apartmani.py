from tabulate import tabulate
from datetime import datetime,timedelta,date
from random import randint
import korisnici
import dodatna_oprema
import rezervacije


def load(file_name="apartmani.txt"):

    with open(file_name, "r", encoding = "utf-8") as file:
        lines = file.readlines() 
        global apartmani
        apartmani = {}
        for line in lines:
            apartman = line.replace("\n", "").split("|")
            apartman_dict = {
                    "sifra":  apartman[0],
                    "tip": apartman[1],
                    "brsoba": apartman[2],
                    "brgostiju": apartman[3],
                    "lokacija": apartman[4],
                    "dostupnost": apartman[5],
                    "domacin": apartman[6],
                    "cena": apartman[7],
                    "status": apartman[8],
                    "sadrzaj": apartman[9]
            }
            apartmani[apartman_dict["sifra"]] = apartman_dict


def pregled_aktivnih():

    load("apartmani.txt")
    tabele = []
    for i in apartmani.values():
        if i["status"] == "Aktivan":
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
    ispis(tabele)


def ispis(tabele):

    global apartmani
    header = ["Sifra", "Tip apartmana", "Broj soba", "Broj gostiju", "Lokacija", "Dostupnost", "Domacin", "Cena po noci",
              "Lista sadrzaja apartmana"]
    print(tabulate(tabele, header, tablefmt="simple"))


def mesto(element):

    temp = element.split('/')
    vrednost = temp[2].split(',')
    vrednost = vrednost[0] + ',' + ' ' + vrednost[1]
    return vrednost


def pretraga_mesto(visestruk):

    sifre = []
    tabele = []
    zapamti = []
    while True:
        print("=" * 110)
        print("Unesite pun naziv ili makar prefiks mesta po kom zelite da izvrsite pretragu, ")
        unos = input(">> ")
        nesto = unos.replace(" ", "")
        greska = 0
        try:
            nesto = eval(nesto)
        except NameError:
            for i in nesto:
                if i in korisnici.br_u_str():
                    greska += 1
            if not greska:
                break
            print("Nepravilan unos.")
            # return False
        except SyntaxError:
            print("Nepravilan unos.")

    while unos[-1] == " ":
        unos = unos[:-1]

    load("apartmani.txt")
    for i in apartmani.values():
        naziv_mesta = i["lokacija"].split(',')[1].lower()
        if(unos.lower() == naziv_mesta or unos.lower() == naziv_mesta[:len(unos.lower())]) and i["status"] == "Aktivan":
            sifre.append(i["sifra"])

    if len(sifre) == 0:
        print("Niste uspeli da pronadjete apartman u zeljenim gradovima")
        return zapamti

    for j in sifre:
        for i in apartmani.values():
            if i["sifra"] == j:
                tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
                zapamti.append(i["sifra"])
    if visestruk:
        return zapamti
    else:
        ispis(tabele)


def manjiod(parametar,visestruk):

    while True:
        print("=" * 100)
        print("Unesite maksimalan iznos po kom zelite da pretrazite, ispis ce biti sve vrednosti manje od zadate: ")
        unos = input("<< ")
        if int_provera(unos):
            break

    tabele = []
    zapamti = []
    for i in apartmani.values():
        if int(unos) > int(i[parametar]) and i["status"] == "Aktivan":
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            parametar = parametar[:2] + "oj " + parametar[2:]
            print(f"Ne postoji apartman sa tacno tom vrednoscu za {parametar} ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            parametar = parametar[:2] + "oj " + parametar[2:]
            print(f"Ne postoji apartman sa tacno tom vrednoscu za {parametar} ")
            return []


def veciod(parametar, visestruk):

    while True:
        print("=" * 100)
        print("Unesite minimalan iznos po kom zelite da pretrazite, ispis ce biti sve vrednosti vece od zadate: ")
        unos = input("<< ")
        if int_provera(unos):
            break

    tabele = []
    zapamti= []
    for i in apartmani.values():
        if int(unos) < int(i[parametar]) and i["status"] == "Aktivan":
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            parametar = parametar[:2] + "oj " + parametar[2:]
            print(f"Ne postoji apartman sa tacno tom vrednoscu za {parametar} ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            parametar = parametar[:2] + "oj " + parametar[2:]
            print(f"Ne postoji apartman sa tacno tom vrednoscu za {parametar} ")
            return []


def krajpretrage(parametar,visestruk):

    if parametar == "brsoba":
        print("=" * 50)
        print("Zavrsetak pretrage po broju soba.")
        print("=" * 50)
    if parametar == "brosoba":
        print("=" * 50)
        print("Zavrsetak pretrage po broju osoba.")
        print("=" * 50)


def pretraga_brsoba(parametar,visestruk):

    load("apartmani.txt")
    temp = ["1", "2", "x"]
    niz = [[], [], [], [], []]
    tabele = []
    sifre = []

    pretraga_br_dict = {
        "1": manjiod,
        "2": veciod,
        "x": krajpretrage
    }

    parametar_meni = parametar[2:]
    while True:

        print("=" * 60)
        print(f"Ponudjene opcije prilikom pretrage po broju {parametar_meni}: ")
        print("=" * 60)
        print(f"1. Pregled po broju {parametar_meni} manjem od unetog broja")
        print(f"2. Pregled po broju {parametar_meni} vecem od unetog broja")
        print(f"x. Izlaz iz pretrage po broju {parametar_meni}")
        unos = input(">> ")
        unos = unos.lower()
        if unos in temp:
            if unos == "1":
                a = pretraga_br_dict[unos](parametar,visestruk)
                if len(a):
                    for i in a:
                        niz[0].append(i)
                temp.remove(unos)
            elif unos == "2":
                a = pretraga_br_dict[unos](parametar,visestruk)
                if len(a):
                    for i in a:
                        niz[1].append(i)
                temp.remove(unos)
            else:
                pretraga_br_dict[unos](parametar,visestruk)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
                if len(sifre):
                    print("=" * 100)
                    print("Rezultat pretrage. ")
                    rez = sifre
                    tabele,sifre = [], []
                    return rez
                else:
                    print("=" * 100)
                    print("Niste uspeli da pronadjete apartman. ")
                    return []

        elif unos in pretraga_br_dict:
            print("Vec ste izvrsili pretragu po datom entitetu")
        else:
            print("Odabrali ste nepostojeću opciju")


def manjiodcena(visestruk):

    while True:
        print("=" * 100)
        print("Unesite maksimalan iznos po kom zelite da pretrazite, ispis ce biti sve vrednosti manje od zadate: ")
        unos = input("<< ")
        if float_provera(unos):
            break

    tabele = []
    zapamti = []
    for i in apartmani.values():
        if float(unos) > float(i["cena"]) and i["status"] == "Aktivan":
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za cenu ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za cenu ")
            return []


def vecaodcena(visestruk):

    while True:

        print("=" * 100)
        print("Unesite minimalan iznos po kom zelite da pretrazite, ispis ce biti sve vrednosti vece od zadate: ")
        unos = input("<< ")
        if float_provera(unos):
            break

    tabele = []
    zapamti = []
    for i in apartmani.values():
        if float(unos) < float(i["cena"]) and i["status"] == "Aktivan":
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za cenu ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za cenu ")
            return []


def krajpretragecena(visestruk):

    print("=" * 50)
    print("Zavrsetak pretrage po ceni.")
    print("=" * 50)


def pretraga_cena(visestruk):

    load("apartmani.txt")
    temp = ["1", "2", "x"]
    niz = [[], [], [], [], []]
    tabele= []
    sifre = []

    pretraga_cena_dict = {
        "1": manjiodcena,
        "2": vecaodcena,
        "x": krajpretragecena
    }

    while True:

        print("=" * 60)
        print("Ponudjene opcije prilikom pretrage po ceni ")
        print("=" * 60)
        print("1. Pregled po ceni manjoj od unetog broja")
        print("2. Pregled po ceni vecoj od unetog broja")
        print("x. Izlaz iz pretrage po ceni")
        unos = input(">> ")
        unos = unos.lower()
        if unos in temp:
            if unos == "1":
                a = pretraga_cena_dict[unos](visestruk)
                if len(a):
                    for i in a:
                        niz[0].append(i)
                temp.remove(unos)
                # tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            elif unos == "2":
                a = pretraga_cena_dict[unos](visestruk)
                if len(a):
                    for i in a:
                        niz[1].append(i)
                temp.remove(unos)
                # tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            else:
                pretraga_cena_dict[unos](visestruk)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
                if len(sifre):
                    print("=" * 100)
                    print("Rezultat pretrage. ")
                    rez = sifre
                    tabele,sifre = [], []
                    return rez
                else:
                    print("=" * 100)
                    print("Niste uspeli da pronadjete apartman. ")
                    return []

        elif unos in pretraga_cena_dict:
            print("Vec ste izvrsili pretragu po datom entitetu")
        else:
            print("Odabrali ste nepostojeću opciju")


def manjevremeod(visestruk):

    # print("=" * 50)
    # print("Unesite datum. ")
    datumi = []
    while True:
        print("=" * 50)
        print("Unesite datum. ")
        datum = dodaj_datum()
        if not datum or datum < datetime.today():
            print("Ovaj datum se ne može prihvatiti. ")
            continue
        break

    tabele = []
    zapamti = []
    load("apartmani.txt")
    for i in apartmani.values():
        niz = 0
        niz = i["dostupnost"].split(',')
        a = 0
        for j in niz:
            temp = j.split("-")
            prvi = temp[0]
            prvi = prvi[1:-1]
            drugi = temp[1]
            drugi = drugi[1:-1]
            prvi = datetime.strptime(prvi, "%d.%m.%Y.")
            drugi = datetime.strptime(drugi, "%d.%m.%Y.")

            if prvi < datum and i["status"] == "Aktivan":
                a += 1

        if a:
            tabele.append(
                [i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                 i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za vremenski opseg ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za vremenski opseg ")
            return []


def vecevremeod(visestruk):

    datumi = []
    while True:
        print("=" * 50)
        print("Unesite datum. ")
        datum = dodaj_datum()
        if not datum or datum < datetime.today():
            print("Ovaj datum se ne može prihvatiti. ")
            continue
        break

    tabele = []
    zapamti = []
    load("apartmani.txt")
    for i in apartmani.values():
        niz = 0
        niz = i["dostupnost"].split(',')
        a = 0
        for j in niz:
            temp = j.split("-")
            prvi = temp[0]
            prvi = prvi[1:-1]
            drugi = temp[1]
            drugi = drugi[1:-1]
            prvi = datetime.strptime(prvi, "%d.%m.%Y.")
            drugi = datetime.strptime(drugi, "%d.%m.%Y.")

            if datum < drugi and i["status"] == "Aktivan":
                a += 1

        if a:
            tabele.append(
                [i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                 i["domacin"], i["cena"], i["sadrzaj"]])
            zapamti.append(i["sifra"])

    if visestruk:
        if len(tabele) <= 0:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za vremenski opseg ")
        return zapamti
    else:
        if len(tabele) > 0:
            ispis(tabele)
            return zapamti
        else:
            print(f"Ne postoji apartman sa tacno tom vrednoscu za vremenski opseg ")
            return []



def krajpretragavreme(visestruk):

    print("=" * 50)
    print("Zavrsetak pretrage po vremenu dostupnosti.")
    print("=" * 50)


def pretraga_vreme_dostupnosti(visestruk):

    load("apartmani.txt")
    temp = ["1", "2", "x"]
    niz = [[], [], [], [], []]
    tabele = []
    sifre = []

    pretraga_vreme_dostupnosti_dict = {

        "1": manjevremeod,
        "2": vecevremeod,
        "x": krajpretragavreme
    }

    while True:

        print("=" * 60)
        print("Ponudjene opcije prilikom pretrage po vremenu dostupnosti ")
        print("=" * 60)
        print("1. Slobodni datumi pre unetog datuma. ")
        print("2. Slobodni datumi nakon unetog datuma. ")
        print("x. Izlaz iz pretrage po vremenu dostupnosti")
        unos = input(">> ")
        unos = unos.lower()
        if unos in temp:
            if unos == "1":
                a = pretraga_vreme_dostupnosti_dict[unos](visestruk)
                if len(a):
                    for i in a:
                        niz[0].append(i)
                temp.remove(unos)
            elif unos == "2":
                a = pretraga_vreme_dostupnosti_dict[unos](visestruk)
                if len(a):
                    for i in a:
                        niz[1].append(i)
                temp.remove(unos)
            else:
                pretraga_vreme_dostupnosti_dict[unos](visestruk)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
                if len(sifre):
                    print("=" * 100)
                    print("Rezultat pretrage. ")
                    rez = sifre
                    tabele,sifre = [], []
                    return rez
                else:
                    print("=" * 100)
                    print("Niste uspeli da pronadjete apartman. ")
                    return []

        elif unos in pretraga_vreme_dostupnosti_dict:
            print("Vec ste izvrsili pretragu po datom entitetu")
        else:
            print("Odabrali ste nepostojeću opciju")


def krajukupnepretrage():

    print("=" * 50)
    print("Zavrsetak pretrage. ")


def pregled_apartmana():

    load("apartmani.txt")
    pregled_dict = {
        "1": pretraga_mesto,
        "2": pretraga_vreme_dostupnosti,
        "3": pretraga_brsoba,
        "4": pretraga_brsoba,
        "5": pretraga_cena,
        "x": krajukupnepretrage
    }
    while True:

        print("=" * 30)
        print("Ponudjene opcije pretrage:")
        print("=" * 30)
        print("1. Po mestu ")
        print("2. Po vremenu dostupnosti")
        print("3. Po broju soba ")
        print("4. Po broju gostiju ")
        print("5. Po ceni ")
        print("x. Izlaz iz pretrage ")
        print("=" * 30)
        unos = input(">> ")
        unos = unos.lower()

        if unos in pregled_dict:
            if unos == "1" or unos == "2" or unos == "5":
                pregled_dict[unos](0)
            if unos == "3":
                pretraga_brsoba("brsoba",0)
            if unos == "4":
                pretraga_brsoba("brgostiju",0)
            if unos == 'x':
                pregled_dict[unos]()
                return
        else:
            print("Odabrali ste nepostojeću opciju")


def aktivni_sifre():

    niz = []
    for i in apartmani.values():
        if i["status"] == "Aktivan":
            niz.append(i["sifra"])

    return niz


def common_member(niz):

    temp_niz = []
    for i in range(len(niz)):
        if not len(niz[i]):
            niz[i] = aktivni_sifre()    # Punimo sve prazne el niza sa svim kako ne bi remetili rez logickog i
            temp_niz.append(i)

    prvi = set(niz[0])
    drugi = set(niz[1])
    treci = set(niz[2])
    cetvrti = set(niz[3])
    peti = set(niz[4])

    rez = (prvi & drugi & treci & cetvrti & peti)
    rez = list(rez)

    a = aktivni_sifre()
    a.sort()
    rez.sort()

    if len(temp_niz):
        for i in range(len(niz)):
            if i in temp_niz:
                niz[i] = []

    if rez and rez != a:
        return rez
    else:
        print("Nemaju zajednickih elemenata ")
        return 0


def visestruka_pretraga():

    load("apartmani.txt")
    pregled_dict = {
        "1": pretraga_mesto,
        "2": pretraga_vreme_dostupnosti,
        "3": pretraga_brsoba,
        "4": pretraga_brsoba,
        "5": pretraga_cena,
        "x": krajukupnepretrage
    }

    temp = ["1", "2", "3", "4", "5", "x"]
    niz = [[], [], [], [], []]
    tabele= []
    sifre = []

    while True:

        print("=" * 30)
        print("Ponudjene opcije pretrage:")
        print("=" * 30)
        print("1. Po mestu ")
        print("2. Po vremenu dostupnosti")
        print("3. Po broju soba ")
        print("4. Po broju gostiju ")
        print("5. Po ceni ")
        print("x. Izlaz iz pretrage ")
        print("=" * 30)

        unos = input(">> ")
        unos = unos.lower()
        if unos in temp:
            if unos == "1":
                a = pregled_dict[unos](1)
                if len(a):
                    for i in a:
                        niz[0].append(i)
                temp.remove(unos)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            elif unos == "2":
                a = pregled_dict[unos](1)
                if len(a):
                    for i in a:
                        niz[1].append(i)
                temp.remove(unos)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            elif unos == "3":
                a = pretraga_brsoba("brsoba",1)
                if len(a):
                    for i in a:
                        niz[2].append(i)
                temp.remove(unos)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            elif unos == "4":
                a = pretraga_brsoba("brgostiju",1)
                if len(a):
                    for i in a:
                        niz[3].append(i)
                temp.remove(unos)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            elif unos == "5":
                a = pregled_dict[unos](1)
                if len(a):
                    for i in a:
                        niz[4].append(i)
                temp.remove(unos)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
            else:
                pregled_dict[unos]()
                print("=" * 100)
                tabele, sifre  = potraga_apartmana(niz,tabele, sifre)
                # temp != ["x"]
                if len(sifre):
                    print("=" * 100)
                    print("Rezultat pretrage. ")
                    rez = sifre
                    tabele,sifre = [], []
                    return rez
                else:
                    print("=" * 100)
                    print("Niste uspeli da pronadjete apartman. ")
                    return 0

        elif unos in pregled_dict:
            print("Vec ste izvrsili pretragu po datom entitetu")
        else:
            print("Odabrali ste nepostojeću opciju")


def potraga_apartmana(niz,tabele,sifre):

    rezultat = common_member(niz)
    if not rezultat:
        return [],[]

    if len(rezultat):
        tabele = []
        sifre = []
        for i in rezultat:
            temp_niz = [apartmani[i]["sifra"], apartmani[i]["tip"], apartmani[i]["brsoba"], apartmani[i]["brgostiju"],
                        mesto(apartmani[i]["lokacija"]), apartmani[i]["dostupnost"], apartmani[i]["domacin"],
                        apartmani[i]["cena"], apartmani[i]["sadrzaj"]]
            tabele.append(temp_niz)
            sifre.append(apartmani[i]["sifra"])

        if len(tabele):
            ispis(tabele)
            return tabele, sifre


def pretraga_sifra():

    load("apartmani.txt")
    print("Ovde su predstavljeni svi aktivni apartmani. ")
    print("=" * 50)
    pregled_aktivnih()
    print("=" * 100)
    while True:
        print("=" * 100)
        print("Unesite sifru apartmana: ")
        unos = input("<< ")
        if int_provera(unos):
            break

    tabele = []
    for i in apartmani.values():

        if i["sifra"] == str(unos) and i["status"] == "Aktivan":
            tabele.append(
                [i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                 i["domacin"], i["cena"], i["sadrzaj"]])

    if not len(tabele):
        print("Ne postoji nijedan aktivan apartman sa ovom sifrom. ")
        return 0
    else:
        print("=" * 100)
        ispis(tabele)
        return unos


def float_provera(unos):

    try:
        unos = float(unos)
        return True

    except ValueError:
        print("Pretraga zahteva broj kao unos, ponovite unos")
        return False


def int_provera(unos):

    try:
        unos = int(unos)
        return True

    except ValueError:
        print("Pretraga zahteva broj kao unos, ponovite unos")
        return False


def namesti_datum(sifra, novidatum):

    load("apartmani.txt")
    rez = ""
    for i in apartmani.values():

        if sifra == i["sifra"]:
            temp = i["sifra"] + "|" + i["tip"] + "|" + i["brsoba"] + "|" + i["brgostiju"] + "|" + \
                   i["lokacija"] + "|" + novidatum + "|" + i["domacin"] + "|" + i["cena"] + "|" + \
                   i["status"] + "|" + i["sadrzaj"] + '\n'
        else:
            temp = i["sifra"] + "|" + i["tip"] + "|" + i["brsoba"] + "|" + i["brgostiju"] + "|" + \
                   i["lokacija"] + "|" + i["dostupnost"] + "|" + i["domacin"] + "|" + i["cena"] + "|" + \
                   i["status"] + "|" + i["sadrzaj"] + '\n'

        rez += temp

    with open("apartmani.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def namesti_ap(noviap):

    temp = ""
    for i in noviap:
        temp += i + ','
    return temp[:-1]


def dodaj_sifra():

    load("apartmani.txt")
    print("=" * 50)
    print("Dodelite neku šifru vašem apartmanu. ")
    while True:
        print("Šifra treba da bude u obliku brojeva (minimum 3, maksimum 7). ")
        sifra = input("<< ")
        if int_provera(sifra) and len(sifra) > 2 and len(sifra) < 8 and int(sifra) > 0:
            if sifra in apartmani:
                print("Zauzeta šifra. ")
            else:
                return sifra

def dodaj_tip():

    while True:
        print("=" *50)
        print("Odaberite tip apartmana. ")
        print("1. Ceo apartman. ")
        print("2. Soba. ")
        tip = input("<< ")
        if tip == "1":
            tip = "ceo apartman"
            return tip
        elif tip == "2":
            tip = "soba"
            return tip
        else:
            print("Nepostojeća opcija. ")


def dodaj_brsoba(tip):

    while True:
        if tip == "soba":
            return "1"
        print("=" * 50)
        print("Unesite broj soba. ")
        brsoba = input("<< ")
        if int_provera(brsoba):
            if int(brsoba) > 1 and int(brsoba) < 21:
                return brsoba


def dodaj_brgostiju(tip):

    while True:
        print("=" * 50)
        print("Unesite broj gostiju. ")
        brgostiju = input("<< ")
        if int_provera(brgostiju):
            if tip == "ceo apartman":
                if int(brgostiju) > 1 and int(brgostiju) < 51:
                    return brgostiju
            else:
                if int(brgostiju) > 0 and int(brgostiju) < 11:
                    return brgostiju


def dodaj_lokaciju():

    print("=" * 50)
    print("Unesite lokaciju apartmana. ")
    while True:
        print("=" * 50)
        print("Unesite naziv ulice. ")
        ulica = input("<< ")
        nesto = ulica.replace(" ", "")
        if korisnici.provera_str_broj(nesto):
            break

    while True:
        print("=" * 50)
        print("Unesite broj ulice. ")
        br = input("<< ")
        if int_provera(br) and int(br) > 0 and int(br) < 200:
            break

    while True:
        print("=" * 50)
        print("Unesite mesto. ")
        mesto = input("<< ")
        nesto2 = mesto.replace(" ", "")
        if korisnici.provera_str_broj(nesto2):
            break

    while True:
        print("=" *50)
        print("Unesite poštanski broj (petocifren broj). ")
        pos = input("<< ")
        if int_provera(pos) and len(pos) == 5:
            break

    krajnjirez = geosir() + "°C" + '/' + geoduz() + "°C" + '/' + namesti_lok(ulica) + " " + br + "," +\
                 namesti_lok(mesto) + ", " +  pos

    return krajnjirez


def namesti_lok(proba):

    proba.split(" ")
    rez = ""
    for i in proba.split(" "):
        rez += i[0].upper() + i[1:].lower() + " "
    return rez[:-1]


def geoduz():

    duz = randint(17, 22)
    return str(duz)

def geosir():

    sir = randint(40,48)
    return str(sir)


def dodaj_cenu():

    while True:
        print("=" * 50)
        print("Unesite ukupnu cenu. ")
        cena = input("<< ")
        if float_provera(cena) and float(cena) > 0:
            return cena


def dodaj_status():

    while True:
        print("=" * 50)
        print("Odaberite status apartmana. ")
        print("1. Aktivan. ")
        print("2. Neaktivan. ")
        status = input("<< ")
        if status == "1":
            status = "Aktivan"
            return status
        elif status == "2":
            status = "Neaktivan"
            return status
        else:
            print("Nepostojeća opcija. ")


def dodaj_datum():

    while True:
        while True:
            print("=" * 100)
            print("Unesite dan: ")
            dan = input("<< ")
            if int_provera(dan):
                if int(dan) > 0:
                    break
                print("Ne mozete uneti negativan dan. ")
        while True:
            print("=" * 100)
            print("Unesite mesec: ")
            mesec = input("<< ")
            if int_provera(mesec):
                if int(mesec) > 0:
                    break
                print("Ne mozete uneti negativan mesec. ")
        while True:
            print("=" * 100)
            print("Unesite godinu: ")
            godina = input("<< ")
            if int_provera(godina):
                if int(godina) > 0:
                    break
                print("Ne mozete uneti negativnu godinu. ")
        date_text = str(godina) + "-" + str(mesec) + "-" + str(dan)
        format = '%Y-%m-%d'
        try:
            a = datetime.strptime(date_text, format)
            return a
        except ValueError:
            print("Neispravan format datuma.")
            return 0

def dodaj_dostupnost():

    print("=" *50)
    print("Unesite dostupne termine")
    datumi = []
    while True:
        datum = []
        print("=" * 50)
        print("Unesite početni datum")
        pocetni = dodaj_datum()
        if not pocetni or pocetni < datetime.today():
            print("Ovaj datum se ne može prihvatiti. ")
            continue
        print("=" * 50)
        print("Unesite krajnji datum")
        krajnji = dodaj_datum()
        if not krajnji or krajnji < pocetni or krajnji < datetime.today():
            print("Ovaj datum se ne može prihvatiti. ")
            continue
        datumi = proveri(datumi, pocetni, krajnji)
        print("Unesite x ako ne želite više dodavati termine, bilo koje dugme za nastavak unosa. ")
        izlaz = input("<< ")
        if izlaz.lower() == "x":
            break

    svi_datumi = []
    if datumi:
        for i in datumi:
            datumi = proveri(datumi, i[0], i[1])
        for i in datumi:
            pocetni = i[0].strftime("%d.%m.%Y.")
            krajnji = i[1].strftime("%d.%m.%Y.")
            svi_datumi.append([pocetni,krajnji])

        konacno = ""
        for i in svi_datumi:
            konacno += "(" + i[0] + " - " + i[1] + ")" + ","
        return konacno[:-1]

    return ""


def proveri(datumi,pocetni,krajnji):

    if not datumi:
        datumi.append([pocetni, krajnji])
    for j,i in enumerate(datumi):
        if pocetni <= i[1] and pocetni >= i[0] and krajnji > i[1]:
            datumi.remove(datumi[j])
            rez = [i[0], krajnji]
            if rez not in datumi:
                datumi.append(rez)
        elif pocetni < i[0] and krajnji >= i[0] and krajnji <= i[1]:
            datumi.remove(datumi[j])
            rez = [pocetni, i[1]]
            if rez not in datumi:
                datumi.append(rez)
        elif pocetni < i[0] and krajnji < i[0]:
            rez = [pocetni, krajnji]
            if rez not in datumi:
                datumi.append(rez)
        elif pocetni > i[1] and krajnji > i[1]:
            rez = [pocetni, krajnji]
            if rez not in datumi:
                datumi.append(rez)
        elif pocetni < i[0] and krajnji > i[1]:
            datumi.remove(datumi[j])
            rez = [pocetni, krajnji]
            if rez not in datumi:
                datumi.append(rez)
        else:
            pass

    return datumi


def dodaj_apartman(trenutni_korisnik):

    load("apartmani.txt")
    print("=" * 50)
    print("Dodavanje novog apartmana. ")

    sifra = dodaj_sifra()
    tip = dodaj_tip()
    brsoba = dodaj_brsoba(tip)
    brgostiju = dodaj_brgostiju(tip)
    lokacija = dodaj_lokaciju()
    domacin = trenutni_korisnik
    cena = dodaj_cenu()
    dodatna_oprema = dodaj_dodatnu_opremu()
    status = dodaj_status()
    dostupnost = dodaj_dostupnost()

    rez = sifra + "|" + tip + "|" + brsoba + "|" + brgostiju + "|" + lokacija + "|" + dostupnost + "|" + domacin + "|" +\
          cena + "|" + status + "|" + dodatna_oprema + "\n"

    # print(rez)
    with open("apartmani.txt", "a", encoding="utf-8") as file:
        file.write(rez)


def ispis_domacin(trenutni_korisnik):

    load("apartmani.txt")
    tabele = []
    sifre = []
    for i in apartmani.values():
        if i["domacin"] == trenutni_korisnik:
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["status"], i["sadrzaj"]]) # ovde treba dodati i status
            sifre.append(i["sifra"])

    header = ["Šifra", "Tip apartmana", "Broj soba", "Broj gostiju", "Lokacija", "Dostupnost", "Domaćin",
              "Cena po noći","Status", "Lista sadržaja apartmana"]

    if tabele:
        print(tabulate(tabele, header, tablefmt="simple"))
        return sifre
    else:
        print("Dati domaćin nema apartmane. ")
        return 0


def izmena_apartman(trenutni_korisnik):

    load("apartmani.txt")
    print("=" *50)
    print("Ovde su prikazani svi apartmani za datog domaćina. ")
    nesto = ispis_domacin(trenutni_korisnik)
    if not nesto:
        return
    print("=" * 50)
    print("Unesite šifru apartmana koji hoćete da menjate. ")
    while True:
        unos = input("<< ")
        if int_provera(unos):
            if unos in nesto:
                break
    tabele = []
    for i in apartmani.values():
        if i["sifra"] == unos:
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["status"], i["sadrzaj"]])

    header = ["Šifra", "Tip apartmana", "Broj soba", "Broj gostiju", "Lokacija", "Dostupnost", "Domaćin",
              "Cena po noći", "Status", "Lista sadržaja apartmana"]
    print(tabulate(tabele, header, tablefmt="simple"))

    while True:
        print("=" *50)
        print("Koji deo želite da menjate? ")
        print("1. Šifra. ")
        print("2. Tip. ")
        print("3. Broj soba. ")
        print("4. Broj gostiju. ")
        print("5. Lokacija. ")
        print("6. Dostupnost. ")
        print("7. Cena. ")
        print("8. Status. ")
        print("9. Dodatna oprema. ")
        odabir = input("<< ")
        if odabir == "1":
            apartmani[unos]["sifra"] = dodaj_sifra()
            break
        elif odabir == "2":
            apartmani[unos]["tip"] = dodaj_tip()
            break
        elif odabir == "3":
            apartmani[unos]["brsoba"] = dodaj_brsoba(trenutni_korisnik)
            break
        elif odabir == "4":
            apartmani[unos]["brgostiju"] = dodaj_brgostiju(trenutni_korisnik)
            break
        elif odabir == "5":
            apartmani[unos]["lokacija"] = dodaj_lokaciju()
            break
        elif odabir == "6":
            apartmani[unos]["dostupnost"] = dodaj_dostupnost()
            break
        elif odabir == "7":
            apartmani[unos]["cena"] = dodaj_cenu()
            break
        elif odabir == "8":
            apartmani[unos]["status"] = dodaj_status()
            break
        elif odabir == "9":
            apartmani[unos]["sadrzaj"] = dodaj_dodatnu_opremu()
            break
        else:
            print("Nepostojeća opcija")

    rez = ""
    for i in apartmani.values():
        rez += i["sifra"] + "|" + i['tip'] + "|" + i['brsoba'] + "|" + i['brgostiju'] + "|" + i['lokacija'] + "|" + \
               i['dostupnost'] + "|" + i['domacin'] + "|" + i['cena'] + "|" + i['status'] + "|" +\
               i['sadrzaj'] + "\n"

    with open("apartmani.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def brisi_apartman(trenutni_korisnik):

    load("apartmani.txt")
    print("=" * 50)
    print("Ovde su prikazani svi apartmani za datog domaćina. ")
    nesto = ispis_domacin(trenutni_korisnik)
    if not nesto:
        return
    print("=" * 50)
    print("Unesite šifru apartmana koji hoćete da obrišete. ")
    while True:
        unos = input("<< ")
        if int_provera(unos):
            if unos in nesto:
                break
    tabele = []
    rez = ""
    for i in apartmani.values():
        if i["sifra"] == unos:
            tabele.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                           i["domacin"], i["cena"], i["status"], i["sadrzaj"]])
            rez += ""
        else:
            rez += i["sifra"] + "|" + i['tip'] + "|" + i['brsoba'] + "|" + i['brgostiju'] + "|" + i['lokacija'] + "|" + \
                   i['dostupnost'] + "|" + i['domacin'] + "|" + i['cena'] + "|" + i['status'] + "|" + \
                   i['sadrzaj'] + "\n"

    header = ["Šifra", "Tip apartmana", "Broj soba", "Broj gostiju", "Lokacija", "Dostupnost", "Domaćin",
              "Cena po noći", "Status", "Lista sadržaja apartmana"]

    print("=" *50)
    print("Izbrisani apartman. ")
    print("=" * 50)
    print(tabulate(tabele, header, tablefmt="simple"))

    rez1 = ""
    rezervacije.load("rezervacije.txt")
    for i in rezervacije.rezervacije.values():
        if unos == i["SifraA"] and i["Status"] != "Prihvaćena":
            temp1 = ""
        else:
            temp1 = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + i["Status"] + '\n'
        rez1 += temp1

    with open("rezervacije.txt", "w", encoding="utf-8") as file:
        file.write(rez1)
    with open("apartmani.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def brisanje_dodatne_opreme():

    sadrzaj = []
    load("apartmani.txt")
    for i in apartmani.values():
        for j in i["sadrzaj"].split(','):
            if j not in sadrzaj:
                sadrzaj.append(j)

    tabele = []
    dodatna_oprema.load("dodatna_oprema.txt")
    for i in dodatna_oprema.dodatna_oprema.values():
        if i["naziv"] not in sadrzaj:
            tabele.append([i["sifra"], i["naziv"]])

    if tabele:
        print("=" *70)
        print("Ovde je prikazana dodatna oprema koju možete izbrisati. ")
        print("=" * 70)
        ispis(tabele)
        while True:
            print("=" * 70)
            print("Unesite šifru dodatne opreme koju želite obrisati")
            unos = input("<< ")
            if int_provera(unos) and len(unos) > 2:
                if unos in dodatna_oprema.dodatna_oprema and \
                        dodatna_oprema.dodatna_oprema[unos]["naziv"] not in sadrzaj:
                    dodatna_oprema.brisi(unos)
                    break
                else:
                    print("Nepostojeća šifra. ")
    else:
        print("Sva dodatna oprema je dodeljena barem nekom apartmanu. ")


def dodaj_dodatnu_opremu():

    dodatna_oprema.load("dodatna_oprema.txt")
    print("=" *50)
    print("Ovde su prikazani svi dostupni elementi dodatne opreme. ")
    dodatna_oprema.ispis_sve()
    print("=" * 50)
    print("Unosom šifre dodajete dati element. ")
    dodati = []
    while True:
        print("=" * 50)
        print("Unosom šifre dodajete dati element, x za izlaz. ")
        unos = input("<< ")
        if unos.lower() == 'x':
            break
        if int_provera(unos):
            if unos in dodatna_oprema.dodatna_oprema:
                if unos not in dodati:
                    dodati.append(unos)
                else:
                    print('Već ste dodali ovaj elemenat.')
            else:
                print("Nepostojeća šifra. ")
    if dodati:
        rez = ""
        for i in dodati:
            rez += dodatna_oprema.dodatna_oprema[str(i)]["naziv"] + ","
        # print(rez[:-1])
        return rez[:-1]
    else:
        return ""

def potvrdjen_dan():

    rezervacije.load("rezervacije.txt")
    tabele = []
    datum = dodaj_datum()
    if not datum:
        return
    for i in rezervacije.rezervacije.values():
        pocetni = datetime.strptime(i["Pocetni_datum"], "%d.%m.%Y.")
        nocenja = int(i["Broj_nocenja"])
        krajnji = pocetni + timedelta(nocenja)
        if datum >= pocetni and datum < krajnji and i["Status"] == 'Prihvaćena':
            if i["SifraA"] not in tabele:
                tabele.append(i["SifraA"])
    if tabele:
        print("=" *100)
        print("Potvrđeni rezervisani apartmani za dati datum: ")
        print("=" * 100)
        ap = []
        load("apartmani.txt")
        for j in tabele:
            for i in apartmani.values():
                if j == i["sifra"]:
                    ap.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                       i["domacin"], i["cena"], i["sadrzaj"]])

        ispis(ap)
    else:
        print("=" * 100)
        print("Nema potvrđenih rezervisanih apartmana za dati datum: ")


def potvrdjen_domacin():

    rezervacije.load("rezervacije.txt")
    korisnici.load("korisnici.txt")
    domacini = []
    domacini1 = []
    for i in korisnici.korisnici.values():
        if i["role"] == "Domacin":
            domacini1.append([i["username"]])
            domacini.append(i["username"])

    # print("Spisak domaćina: ")
    header = ["Spisak domaćina: "]
    print("=" *70)
    print(tabulate(domacini1, header, tablefmt="simple"))
    # for i in domacini:
    #     print(i)

    while True:
        print("=" *70)
        print("Unesite domaćina za kog želite uvid u prikaz. ")
        unos = input("<< ")
        if unos in domacini:
            break

    tabele = []
    load("apartmani.txt")
    for i in rezervacije.rezervacije.values():
        if i["SifraA"] not in apartmani:
            continue
        if i["Status"] == 'Prihvaćena' and apartmani[i["SifraA"]]["domacin"] == unos:
            if i["SifraA"] not in tabele:
                tabele.append(i["SifraA"])

    if tabele:
        print("=" *100)
        print("Potvrđeni rezervisani apartmani za datog domaćina: ")
        print("=" * 100)
        ap = []
        load("apartmani.txt")
        for j in tabele:
            for i in apartmani.values():
                if j == i["sifra"]:
                    ap.append([i["sifra"], i["tip"], i["brsoba"], i["brgostiju"], mesto(i["lokacija"]), i["dostupnost"],
                       i["domacin"], i["cena"], i["sadrzaj"]])

        ispis(ap)
    else:
        print("=" * 100)
        print("Nema potvrđenih rezervisanih apartmana za datog domaćina: ")


def mesecni_pregled():

    danasnji = datetime.today()
    pre_mesec = danasnji - timedelta(30)

    korisnici.load("korisnici.txt")
    rezervacije.load("rezervacije.txt")
    load("apartmani.txt")
    domacini = []
    for i in korisnici.korisnici.values():
        if i["role"] == "Domacin":
            domacini.append(i["username"])

    for i in domacini:
        ap = []
        for j in apartmani:
            if i == apartmani[j]["domacin"]:
                ap.append(apartmani[j]["sifra"])

        cena = 0
        brrez = 0
        for k in ap:
            for j in rezervacije.rezervacije.values():
                pocetni = datetime.strptime(j["Pocetni_datum"], "%d.%m.%Y.")
                nocenja = int(j["Broj_nocenja"])
                krajnji = pocetni + timedelta(nocenja)
                if j["SifraA"] == k and j["Status"] == 'Završena':
                    if krajnji > pre_mesec and krajnji < danasnji:
                        brrez += 1
                        cena += float(j["Ukupna_cena"])

        print(f"Domaćin: {i} ima {brrez} rezervacija i ukupnu zaradu {cena}.")


def godisnji_pregled():

    danasnji = datetime.today()
    pre_godinu = danasnji - timedelta(365)

    korisnici.load("korisnici.txt")
    rezervacije.load("rezervacije.txt")
    load("apartmani.txt")
    domacini = []
    for i in korisnici.korisnici.values():
        if i["role"] == "Domacin":
            domacini.append(i["username"])

    for i in domacini:
        ap = []
        for j in apartmani:
            if i == apartmani[j]["domacin"]:
                ap.append(apartmani[j]["sifra"])

        cena = 0
        brrez = 0
        for k in ap:
            for j in rezervacije.rezervacije.values():
                pocetni = datetime.strptime(j["Pocetni_datum"], "%d.%m.%Y.")
                nocenja = int(j["Broj_nocenja"])
                krajnji = pocetni + timedelta(nocenja)
                if j["SifraA"] == k and  j["Status"] == 'Završena':
                    if krajnji > pre_godinu and krajnji < danasnji:
                        brrez += 1
                        cena += float(j["Ukupna_cena"])

        print(f"Domaćin: {i} ima {brrez} rezervacija i ukupnu zaradu {cena}.")

def ukupan_br_cena():

    rezervacije.load("rezervacije.txt")
    load("apartmani.txt")
    tabele = []
    datum = dodaj_datum()
    if not datum:
        return
    brrez = 0
    cena = 0
    for i in rezervacije.rezervacije.values():
        pocetni = datetime.strptime(i["Pocetni_datum"], "%d.%m.%Y.")
        nocenja = int(i["Broj_nocenja"])
        krajnji = pocetni + timedelta(nocenja)
        if datum >= pocetni and datum < krajnji and i["Status"] == 'Prihvaćena' and i["SifraA"] in apartmani:
            if i["SifraA"] not in tabele:
                tabele.append(i["SifraA"])
                brrez += 1
                cena += float(apartmani[i["SifraA"]]["cena"])

    korisnici.load("korisnici.txt")
    domacini = []
    domacini1 = []
    for i in korisnici.korisnici.values():
        if i["role"] == "Domacin":
            domacini1.append([i["username"]])
            domacini.append(i["username"])

    header = ["Spisak domaćina: "]
    print("=" *70)
    print(tabulate(domacini1, header, tablefmt="simple"))


    while True:
        print("=" *70)
        print("Unesite domaćina za kog želite uvid u prikaz. ")
        unos = input("<< ")
        if unos in domacini:
            break

    tabele1 = []
    load("apartmani.txt")
    for i in rezervacije.rezervacije.values():
        if i["SifraA"] not in apartmani:
            continue
        if i["Status"] == 'Prihvaćena' and apartmani[i["SifraA"]]["domacin"] == unos:
            if i["SifraA"] not in tabele1:
                tabele1.append(i["SifraA"])

    if tabele and tabele1:
        zajednicki = common_member([tabele, tabele1, [], [], []])
        if zajednicki:
            print(f"Za dati datum je domaćin ima {brrez} rezervacija i zaradio je {cena}")
        else:
            print("Taj datum se ne nalazi u rezervacijama datog domaćina. ")
    else:
        print("Taj datum se ne nalazi u rezervacijama datog domaćina. ")

def zastupljenost_grad():

    gradovi = {}
    load("apartmani.txt")
    for i in apartmani.values():
        grad = mesto(i["lokacija"]).split(",")[1][1:]
        if grad not in gradovi:
            gradovi[i["sifra"]] = grad
    rezervacije.load("rezervacije.txt")
    rez = {}
    for i in gradovi:
        brrez = 0
        for j in rezervacije.rezervacije.values():
            if j['SifraA'] == i:
                brrez += 1
        rez[i] = brrez

    broj = 0
    for i in rezervacije.rezervacije.values():
        broj += 1

    glava = ["Grad", "Odnos", "Procenat"]
    jedan = []
    deo = []
    for i in gradovi:
        procenat = rez[i] / broj * 100
        procenat = int(procenat)
        nes = str(procenat) + "/" + str(broj)
        deo.append(str(gradovi[i]))
        deo.append(nes)
        deo.append(str(procenat) + "%")
        jedan.append(deo)
        deo = []

    print("=" *100)
    print(tabulate(jedan, glava, tablefmt="simple"))


def najpopularniji():

    gradovi = {}
    load("apartmani.txt")
    for i in apartmani.values():
        grad = mesto(i["lokacija"]).split(",")[1][1:]

        if grad not in gradovi:
            gradovi[i["sifra"]] = grad

    rezervacije.load("rezervacije.txt")
    rez = {}
    for i in gradovi:
        brrez = 0
        for j in rezervacije.rezervacije.values():
            if j['SifraA'] == i:
                brrez += 1
        rez[i] = brrez
    broj = 0
    for i in rezervacije.rezervacije.values():
        broj += 1

    prgr = {}
    for i in gradovi:
        procenat = rez[i] / broj * 100
        procenat = int(procenat)
        prgr[gradovi[i]] = procenat

    nes = []
    nes1 = []
    s = list(prgr.values())
    s.sort()
    s.reverse()

    for j in s:
        for i in prgr:
            if prgr[i] == j and i not in nes:
                nes.append(i)
                nes1.append([i])

    header = ["Najpopularniji gradovi: "]
    print("=" * 70)
    if len(nes1) > 10:
        print(tabulate(nes1[:10], header, tablefmt="simple"))
    else:
        print(tabulate(nes1, header, tablefmt="simple"))


def izlaz_izvestavanje():

    print("=" *100)
    print("Završetak izveštavanja. ")
    print("=" * 100)


def izvestavanje():

    izvestavanje_dict = {
        "1": potvrdjen_dan,
        "2": potvrdjen_domacin,
        "3": godisnji_pregled,
        "4": mesecni_pregled,
        "5": ukupan_br_cena,
        "6": zastupljenost_grad,
        "x": izlaz_izvestavanje,
        "X": izlaz_izvestavanje
    }
    print("=" *100)
    print("Izveštavanje: ")
    while True:
        print("=" * 100)
        print("1. Lista potvrđenih rezervisanih apartmana za izabran dan realizacije. ")
        print("2. Lista potvrđenih rezervisanih apartmana za izabranog domaćina. ")
        print("3. Godišnji pregled angažovanja domaćina. ")
        print("4. Mesečni pregled angažovanja po domaćinu. ")
        print("5. Ukupan broj i cena potvrđenih rezervacija za izabrani dan i izabranog domaćina. ")
        print("6. Pregled zastupljenosti pojedinačnih gradova u odnosu na ukupan broj rezervacija. ")
        print("x. Izlaz iz izveštavanja. ")
        unos = input("<< ")
        if unos in izvestavanje_dict:
            izvestavanje_dict[unos]()
            if unos == 'x' or 'X':
                return
        else:
            print("Odabrali ste nepostojeću opciju")


apartmani = {}
