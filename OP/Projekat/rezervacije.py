from datetime import datetime, timedelta
from random import randint
from tabulate import tabulate
import apartmani
import korisnici
import main


# uloga = ""
# trenutni_korisnik = ""
def load(file_name="rezervacije.txt"):

    with open(file_name, "r", encoding = "utf-8") as file:

        lines = file.readlines()
        global rezervacije
        rezervacije = {}
        for line in lines:

            user_data = line.replace("\n", "").split("|")
            user_dict = {

                    "SifraR":  user_data[0],
                    "SifraA":  user_data[1],
                    "Pocetni_datum": user_data[2],
                    "Broj_nocenja": user_data[3],
                    "Ukupna_cena": user_data[4],
                    "Gost": user_data[5],
                    "Status": user_data[6],

            }

            rezervacije[user_dict["SifraR"]] = user_dict

    # print(rezervacije)


def upis_fajl(file_name="ostali_gosti.txt", text = ""):

    with open(file_name, "a", encoding = "utf-8") as file:

        file.write(text)


def odabir_apartmana():

    apartmani.load("apartmani.txt")
    while True:

        print("=" * 50)
        print("Odabir apartmana. ")
        print("=" * 50)
        rez = apartmani.pretraga_sifra()
        if rez:
            break

    return rez

def pregled_i_odabir(n):

    apartmani.load("apartmani.txt")
    stari_niz = apartmani.apartmani[str(n)]["dostupnost"].split(",")
    stari_niz = apartmani.namesti_ap(stari_niz)
    niz = apartmani.apartmani[str(n)]["dostupnost"].split(",")

    # for i in niz:
    #     # print(i)

    while True:

        while True:

            print("=" * 100)
            print("Unesite dan: ")
            dan = input("<< ")
            if apartmani.int_provera(dan):
                if int(dan) > 0:
                    break
                print("Ne mozete uneti negativan dan. ")

        while True:

            print("=" * 100)
            print("Unesite mesec: ")
            mesec = input("<< ")
            if apartmani.int_provera(mesec):
                if int(mesec) > 0:
                    break
                print("Ne mozete uneti negativan mesec. ")

        while True:

            print("=" * 100)
            print("Unesite godinu: ")
            godina = input("<< ")
            if apartmani.int_provera(godina):
                if int(godina) > 0:
                    break
                print("Ne mozete uneti negativnu godinu. ")

        date_text = str(godina) + "-" + str(mesec) + "-" + str(dan)
        format = '%Y-%m-%d'
        try:
            a = datetime.strptime(date_text, format)
            # print("This is the correct date string format.")
            # print(a)
            break
        except ValueError:
            print("Nepravilan unos datuma.")

    while True:

        print("=" * 100)
        print("Unesite broj nocenja: ")
        nocenja = input("<< ")
        try:
            nocenja = int(nocenja)
            if nocenja > 0:
                break
            print("Ne može negativan broj. ")
        except ValueError:
            print("Pretraga zahteva broj kao unos, minimalno 1, ponovite unos")

    delta_x_days = timedelta(nocenja)
    krajnji = a + delta_x_days

    for index,j in enumerate(niz):
        temp = j.split("-")
        prvi = temp[0]
        prvi = prvi[1:-1]
        drugi = temp[1]
        drugi = drugi[1:-1]
        prvi = datetime.strptime(prvi, "%d.%m.%Y.")
        drugi = datetime.strptime(drugi, "%d.%m.%Y.")

        # Ovaj deo koda se brine o proracunavanju preostalih datuma
        if a >= prvi and a <= drugi and krajnji >= prvi and krajnji <= drugi:
            if (a - prvi).days == 0 and (drugi - krajnji).days == 0:
                pass
                niz.remove(j)
            elif (a - prvi).days == 0 and (drugi - krajnji).days > 0:
                krajnji = krajnji.strftime("%d.%m.%Y.")
                drugi = drugi.strftime("%d.%m.%Y.")
                rez = "(" + krajnji + " - " + drugi + ")"
                # print(rez)
                niz[index] = rez
            elif (a - prvi).days > 0 and (drugi - krajnji).days == 0:
                prvi = prvi.strftime("%d.%m.%Y.")
                a = a.strftime("%d.%m.%Y.")
                rez = "(" + prvi + " - " + a + ")"
                # print(rez)
                niz[index] = rez
            else:
                prvi = prvi.strftime("%d.%m.%Y.")
                a = a.strftime("%d.%m.%Y.")
                krajnji = krajnji.strftime("%d.%m.%Y.")
                drugi = drugi.strftime("%d.%m.%Y.")
                rez2 = "(" + krajnji + " - " + drugi + ")"
                rez1 = "(" + prvi + " - " + a + ")"
                niz[index] = rez2
                niz.insert(index,rez1)

            # print(niz)
            niz = apartmani.namesti_ap(niz)
            break
    else:
        print("Datum nije u opsegu slobodnih datuma")
        return 0, 0, 0

    print("=" *100)
    if type(a) != str:
        a = a.strftime("%d.%m.%Y.")
    if type(krajnji) != str:
        krajnji = krajnji.strftime("%d.%m.%Y.")
    zakazano = "(" + a + " - " + krajnji + ")"
    return zakazano, stari_niz, niz


def dodaj_ostale_goste(sifra, korisnik):

    korisnici.load("korisnici.txt")
    apartmani.load("apartmani.txt")
    niz = []
    while True:

        while True:
            print("=" *100)
            print("Unesite ime: ")
            ime = input(">> ")
            if korisnici.provera_str_broj(ime):
                break

        while True:
            print("=" *100)
            print("Unesite prezime: ")
            prezime = input(">> ")
            if korisnici.provera_str_broj(prezime):
                break

        niz.append([ime,prezime])
        nekigosti = int(apartmani.apartmani[str(sifra)]["brgostiju"])
        if len(niz) == (nekigosti - 1) or nekigosti == 1:
            break
        izlaz = 0
        while True:
            print("Da li zelite da unesete jos jednog gosta? (Y/N) ")
            unos = input("<< ")
            if unos.upper() == 'Y':
                break
            elif unos.upper() == 'N':
                izlaz += 1
                break
            else:
                print("Nepostojeca opcija. ")

        if izlaz:
            break

    neki_rez = korisnici.unpack(korisnik)
    niz.insert(0,neki_rez)
    ostali_gosti = unpack_niz(niz)
    upis_fajl("ostali_gosti.txt", ostali_gosti)
    # return niz
    arr = []
    arr.append(neki_rez)
    return arr


def unos_gostiju(sifra,korisnik):

    niz = []
    korisnici.load("korisnici.txt")
    apartmani.load("apartmani.txt")
    if apartmani.apartmani[str(sifra)]["brgostiju"] == '1':
        gosti = korisnici.korisnici[korisnik]
        neki_rez = korisnici.unpack(korisnik)
        niz.append(neki_rez)
        return niz

    while True:

        print("=" *100)
        print("Odabir: ")
        print("1. Sami idete u apartman namenjen za vise gostiju. ")
        print("2. Unos gostiju")
        unos = input("<< ")

        if unos == '1':
            gosti = korisnici.korisnici[korisnik]
            neki_rez = korisnici.unpack(korisnik)
            niz.append(neki_rez)
            return niz
        elif unos == '2':
            rez = dodaj_ostale_goste(sifra, korisnik)
            return rez
            break


def potvrda_rezervacije():

    while True:

        print("=" *50)
        print("Potvrda rezervacije.")
        print("=" * 50)
        print("Odabir: ")
        print("1. Potvrda rezervacije. ")
        print("2. Otkazivanje rezervacije. ")

        unos = input("<< ")

        if unos == '1':
            return "Kreirana"
        elif unos == '2':
            return "Odustanak"
        else:
            print("Neispravan unos. ")


def zapamti_rezervaciju(apartman, rezervisano, gosti, status, stari_datum, novi_datum):

    apartmani.load("apartmani.txt")
    load("rezervacije.txt")
    while True:

        ima = 0
        sifra = randint(100, 999)
        for i in rezervacije.values():
            if sifra == i["SifraR"]:
                ima += 1
        if not ima:
            break
    popust = 0
    pocetni_datum = rezervisano.split('-')[0][1:-1]
    krajnji_datum = rezervisano.split('-')[1][1:-1]
    prvidatum = datetime.strptime(pocetni_datum, "%d.%m.%Y.")
    drugidatum = datetime.strptime(krajnji_datum,"%d.%m.%Y.")
    broj_nocenja = (drugidatum - prvidatum).days
    for i in rezervacije.values():
        if unpack_niz(gosti) == i["Gost"] and \
                (i["Status"] == "Kreirana" or i["Status"] == "Prihvaćena" or i["Status"] == "Završena"):
            popust += 1

    if popust:
        ukupna_cena = float(apartmani.apartmani[apartman]["cena"]) * broj_nocenja * 0.95
        ukupna_cena = "{:.2f}".format(ukupna_cena)
    else:
        ukupna_cena = float(apartmani.apartmani[apartman]["cena"]) * broj_nocenja

    rezervacija = str(sifra) + '|' +  apartman + '|' + pocetni_datum + '|' + str(broj_nocenja) + '|' + \
                  str(ukupna_cena) + '|' + unpack_niz(gosti) + '|' + status + '\n'
    # print(rezervacija)
    upis_fajl("rezervacije.txt", rezervacija)

    if status == "Kreirana":
        apartmani.namesti_datum(apartman, novi_datum)
        cuvajstari(apartman, stari_datum)


def cuvajstari(sifra, datum):

    rez = sifra + "|" + datum + "\n"
    stari_datum_load("stari_termini.txt")
    nesto = ""
    if sifra in stari_datumi:
        for i in stari_datumi.values():
            if sifra == i["sifra"]:
                temp = i["sifra"] + "|" + datum + '\n'
            else:
                temp = i["sifra"] + "|" + i["vrednost"] + '\n'
            nesto += temp
        with open("stari_termini.txt", "w", encoding="utf-8") as file:
            file.write(nesto)
    else:
        with open("stari_termini.txt", "a", encoding="utf-8") as file:
            file.write(rez)



def unpack_niz(niz):

    temp = ""
    temp += '(' + niz[0] + ')' + ','
    if len(niz) == 1:
        return temp[:-1]

    for i in range(1,len(niz)):
        temp += '(' + niz[i][0] + '-' + niz[i][1] + ')' + ','

    temp = temp[:-1]
    return temp


def rezervisanje_apartmana(trenutni_korisnik):

    load("rezervacije.txt")
    apartman = odabir_apartmana()
    rezervisano, stari_datum, novi_datum = pregled_i_odabir(apartman)
    if rezervisano:
        gosti_apartmana = unos_gostiju(apartman, trenutni_korisnik)
        status_rezervacije = potvrda_rezervacije()
        zapamti_rezervaciju(apartman, rezervisano, gosti_apartmana, status_rezervacije, stari_datum, novi_datum)

    else:
        print("Neuspesna rezervacija. ")
        return


def stari_datum_load(file_name = "stari_termini.txt"):

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        global stari_datumi
        stari_datumi = {}
        for line in lines:
            datum = line.replace("\n", "").split("|")
            datum_dict = {
                "sifra": datum[0],
                "vrednost": datum[1],
            }

            stari_datumi[datum_dict["sifra"]] = datum_dict


def stari_datum(sifra):

    load("rezervacije.txt")
    sifra_apartmana = rezervacije[sifra]["SifraA"]
    pocetni_datum = rezervacije[sifra]["Pocetni_datum"]
    pocetni_datum = datetime.strptime(pocetni_datum, "%d.%m.%Y.")
    broj_nocenja = rezervacije[sifra]["Broj_nocenja"]
    broj_nocenja = int(broj_nocenja)
    krajnji_datum = pocetni_datum + timedelta(broj_nocenja)
    # stari_datum_load("stari_termini.txt")
    apartmani.load("apartmani.txt")
    niz = apartmani.apartmani[sifra_apartmana]["dostupnost"].split(",")
    arr1 = []
    pocetni_datum_novog = 0

    for i in niz:
        pass
        prvi = i.split('-')[0]
        drugi = i.split('-')[1]
        prvi = prvi[1:-1]
        drugi = drugi[1:-1]
        prvi = datetime.strptime(prvi, "%d.%m.%Y.")
        drugi = datetime.strptime(drugi, "%d.%m.%Y.")
        if drugi == pocetni_datum:
            prvi = prvi.strftime("%d.%m.%Y.")
            arr1.append(prvi)
            pocetni_datum_novog += 1
        if prvi == krajnji_datum:
            drugi = drugi.strftime("%d.%m.%Y.")
            arr1.append(drugi)
    print(niz)
    print(arr1)
    print(krajnji_datum)
    bastemp = ""
    if len(arr1) == 2:
        nesto1 = arr1[0]
        nesto1 = datetime.strptime(nesto1, "%d.%m.%Y.")
        nesto2 = arr1[1]
        nesto2 = datetime.strptime(nesto2, "%d.%m.%Y.")
        for i in niz:
            prvi = i.split('-')[0]
            drugi = i.split('-')[1]
            prvi = prvi[1:-1]
            drugi = drugi[1:-1]
            prvi = datetime.strptime(prvi, "%d.%m.%Y.")
            drugi = datetime.strptime(drugi, "%d.%m.%Y.")
            if prvi == krajnji_datum:
                continue
            if drugi == pocetni_datum:
                nesto1 = nesto1.strftime("%d.%m.%Y.")
                nesto2 = nesto2.strftime("%d.%m.%Y.")
                bastemp += '(' + nesto1 + " - " + nesto2 + ")" + ","
                nesto1 = datetime.strptime(nesto1, "%d.%m.%Y.")
                nesto2 = datetime.strptime(nesto2, "%d.%m.%Y.")
                continue
            prvi = prvi.strftime("%d.%m.%Y.")
            drugi = drugi.strftime("%d.%m.%Y.")
            bastemp += '(' + prvi + " - " + drugi + ")" + ","
            # onda imamo elniza + krajnji datum
        bastemp = bastemp[:-1]
        print(bastemp)
        print(niz)
        # onda imamo prvi + drugi
    elif len(arr1) == 1:
        if pocetni_datum_novog:
            nesto = arr1[0]
            nesto = datetime.strptime(nesto, "%d.%m.%Y.")
            for i in niz:
                prvi = i.split('-')[0]
                drugi = i.split('-')[1]
                prvi = prvi[1:-1]
                drugi = drugi[1:-1]
                prvi = datetime.strptime(prvi, "%d.%m.%Y.")
                drugi = datetime.strptime(drugi, "%d.%m.%Y.")
                if prvi == nesto:
                    drugi = krajnji_datum
                prvi = prvi.strftime("%d.%m.%Y.")
                drugi = drugi.strftime("%d.%m.%Y.")
                bastemp += '(' + prvi + " - " + drugi + ")" + ","
            # onda imamo elniza + krajnji datum
            bastemp = bastemp[:-1]
            print(bastemp)
            print(niz)
        else:
            nesto = arr1[0]
            nesto = datetime.strptime(nesto, "%d.%m.%Y.")
            for i in niz:
                prvi = i.split('-')[0]
                drugi = i.split('-')[1]
                prvi = prvi[1:-1]
                drugi = drugi[1:-1]
                prvi = datetime.strptime(prvi, "%d.%m.%Y.")
                drugi = datetime.strptime(drugi, "%d.%m.%Y.")
                if drugi == nesto:
                    prvi = pocetni_datum
                prvi = prvi.strftime("%d.%m.%Y.")
                drugi = drugi.strftime("%d.%m.%Y.")
                bastemp += '(' + prvi + " - " + drugi + ")" + ","
            # onda imamo elniza + krajnji datum
            bastemp = bastemp[:-1]
            print(bastemp)
            print(niz)
            # onda imamo pocetni datum + elniza
    else:
        upisao = 0
        # temp_datum = datetime.strptime(krajnji_datum, "%d.%m.%Y.")
        for i in niz:
            prvi = i.split('-')[0]
            drugi = i.split('-')[1]
            prvi = prvi[1:-1]
            drugi = drugi[1:-1]
            prvi = datetime.strptime(prvi, "%d.%m.%Y.")
            drugi = datetime.strptime(drugi, "%d.%m.%Y.")
            if prvi > krajnji_datum and upisao == 0:
                pocetni_datum = pocetni_datum.strftime("%d.%m.%Y.")
                krajnji_datum = krajnji_datum.strftime("%d.%m.%Y.")
                bastemp += '(' + pocetni_datum + " - " + krajnji_datum + ")" + ","
                upisao += 1
                pocetni_datum = datetime.strptime(pocetni_datum, "%d.%m.%Y.")
                krajnji_datum = pocetni_datum + timedelta(broj_nocenja)
            prvi = prvi.strftime("%d.%m.%Y.")
            drugi = drugi.strftime("%d.%m.%Y.")
            bastemp += '(' + prvi + " - " + drugi + ")" + ","
            # onda imamo elniza + krajnji datum
        bastemp = bastemp[:-1]
        print(bastemp)
        print(niz)

    return bastemp


def ponistavanje_rezervacija(trenutni_korisnik):

    while True:

        print("=" *50)
        print("Unesite sifru rezervacije: ")
        unos = input("<< ")
        if apartmani.int_provera(unos):
            if int(unos) > 0:
                break
            print("Ne mozete uneti negativnu sifru. ")

    sifrerez = 0
    load("rezervacije.txt")
    rez = ""
    namesti = '(' + korisnici.unpack(trenutni_korisnik) + ')'
    for i in rezervacije.values():

        if unos == i["SifraR"] and namesti == i["Gost"] and (i["Status"] == "Kreirana" or i["Status"] == "Prihvaćena"):
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + "Odustanak" + '\n'
            apartmani.namesti_datum(i["SifraA"], stari_datum(unos))
            sifrerez += 1
        else:
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + i["Status"] + '\n'

        rez += temp

    with open("rezervacije.txt", "w", encoding="utf-8") as file:
        file.write(rez)

    if not sifrerez:
        print("Ne postoji takva rezervacija koja se moze ponistiti. ")


def ispis(tabele):

    header = ["Šifra rezervacije", "Šifra apartmana", "Početni datum rezervacije", "Broj noćenja", "Ukupna cena",
              "Gost", "Status"]
    print(tabulate(tabele, header, tablefmt="simple"))


def pregled_rezervacija(trenutni_korisnik):

    load("rezervacije.txt")
    tabele = []
    niz = []
    niz.append(korisnici.unpack(trenutni_korisnik))
    for i in rezervacije.values():

        if i["Gost"] == unpack_niz(niz):
            tabele.append([i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"], i["Gost"],
                           i["Status"]])

    if tabele:
        ispis(tabele)
    else:
        print("Za sada nemate obavljenu nijednu rezervaciju. ")


def pregled_nepotvrdjene(trenutni_korisnik):

    load("rezervacije.txt")
    apartmani.load("apartmani.txt")
    tabele = []
    for i in rezervacije.values():

        if i["Status"] == "Kreirana" and apartmani.apartmani[i["SifraA"]]["domacin"] == trenutni_korisnik:
            tabele.append([i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"], i["Gost"],
                           i["Status"]])

    if tabele:
        ispis(tabele)
    else:
        print("Ne postoji nijedna nepotvrđena rezervacija. ")


def potvrda_odbijanje():

    load("rezervacije.txt")
    print("=" * 50)
    print("Potvrda ili odbijanje rezervacija. ")
    print("=" * 50)
    while True:

        print("Unesite sifru rezervacije. ")
        unos = input("<< ")
        if apartmani.int_provera(unos):
            if int(unos) > 0:
                break
            print("Ne mozete uneti negativnu sifru. ")

    if unos not in rezervacije:
        print("Ne postoji rezervacija sa tom sifrom. ")
        return

    while True:

        print("Odabir: ")
        print("1. Potvrda rezervacije. ")
        print("2. Odbijanje rezervacije. ")
        odabir = input("<< ")
        if apartmani.int_provera(odabir):
            if int(odabir) < 0:
                print("Ne mozete uneti negativnan broj. ")
                continue

        if odabir == "1":
            potvrda(unos)
            break
        elif odabir == "2":
            odbijanje(unos)
            break
        else:
            print("Nepostojeca opcija. ")


def potvrda(sifra):

    load("rezervacije.txt")
    rez = ""
    for i in rezervacije.values():

        if i["SifraR"] == sifra:
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + "Prihvaćena" + '\n'
        else:
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + i["Status"] + '\n'

        rez += temp

    with open("rezervacije.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def odbijanje(sifra):

    load("rezervacije.txt")
    rez = ""
    for i in rezervacije.values():

        if sifra == i["SifraR"]:
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + "Odbijena" + '\n'
            apartmani.namesti_datum(i["SifraA"], stari_datum(sifra))
        else:
            temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
                   i["Ukupna_cena"] + "|" + i["Gost"] + "|" + i["Status"] + '\n'

        rez += temp

    with open("rezervacije.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def prihvacena():

    load("rezervacije.txt")
    tabele = []
    for i in rezervacije.values():

        if i["Status"] == "Prihvaćena":
            tabele.append([i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"], i["Gost"],
                           i["Status"]])

    if tabele:
        ispis(tabele)
    else:
        print("Ne postoji nijedna prihvaćena rezervacija. ")


def odbijena():

    load("rezervacije.txt")
    tabele = []
    for i in rezervacije.values():

        if i["Status"] == "Odbijena":
            tabele.append([i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"], i["Gost"],
                           i["Status"]])

    if tabele:
        ispis(tabele)
    else:
        print("Ne postoji nijedna odbijena rezervacija. ")


def izlaz_pretraga():

    print("=" * 50)
    print("Zavrsetak pretrage po statusu rezervacija. ")


def pretraga_po_statusu():

    pretraga_po_statusu_dict = {

        "1": prihvacena,
        "2": odbijena,
        "x": izlaz_pretraga
    }

    print("=" * 50)
    print("Pretraga po statusu: ")
    print("=" * 50)
    while True:

        print("Odabir: ")
        print("1. Prihvaćena. ")
        print("2. Odbijena. ")
        print("x. Izlaz iz pretrage. ")
        unos = input("<< ")
        if unos in pretraga_po_statusu_dict:

            pretraga_po_statusu_dict[unos]()
            if unos == 'x':
                return
        else:
            print("Odabrali ste nepostojeću opciju")


def pretraga_po_adresi():

    apartmani.load("apartmani.txt")
    sifre = []
    tabele = []
    while True:
        print("=" * 110)
        print("Unesite pun naziv ili makar prefiks adrese po kojoj želite da izvršite pretragu. ")
        print("Format = Ulica Broj, Grad")
        unos = input(">> ")
        nesto = unos.replace(" ", "")

        try:
            nesto = eval(nesto)
        except NameError:
            break
        except SyntaxError:
            print("Nepravilan unos.")

    while unos[-1] == " ":
        unos = unos[:-1]

    for i in apartmani.apartmani.values():
        adresa = i["lokacija"].split('/')[2].split(',')
        adresa = adresa[0] + ', ' + adresa[1]
        adresa = adresa.lower()

        if(unos.lower() == adresa or unos.lower() == adresa[:len(unos.lower())]):
            sifre.append(i["sifra"])

    for j in sifre:
        for i in rezervacije.values():
            if i["SifraA"] == j:
                tabele.append([i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"],
                     i["Gost"], i["Status"]])
    if tabele:
        ispis(tabele)
    else:
        print("Ne postoji nijedna rezervacija u apartmanu na unetoj adresi. ")


def pretraga_po_domacinu():

    korisnici.load("korisnici.txt")
    apartmani.load("apartmani.txt")
    load("rezervacije.txt")
    apartman = []
    tabele = []
    while True:
        unos = input("Unesite korisničko ime domaćina: ")
        if korisnici.provera_str_broj(unos):

            for i in apartmani.apartmani.values():
                if unos.lower() == i["domacin"]:
                    apartman.append(i["sifra"])

            for j in apartman:
                for i in rezervacije.values():
                    if j == i["SifraA"]:
                        tabele.append(
                            [i["SifraR"], i["SifraA"], i["Pocetni_datum"], i["Broj_nocenja"], i["Ukupna_cena"],
                             i["Gost"], i["Status"]])

            if tabele:
                ispis(tabele)
            else:
                print("Ne postoji nijedna rezervacija vezana za datog domaćina. ")
            break
        else:
            print("Neispravan unos. ")


def zavrsetak_pretrage():

    print("=" *50)
    print("Kraj pretrage rezervacija. ")


def pretraga_admin_rezervacije():

    load("rezervacije.txt")

    pretraga_admin_rezervacije_dict = {

        "1": pretraga_po_statusu,
        "2": pretraga_po_adresi,
        "3": pretraga_po_domacinu,
        "x": zavrsetak_pretrage
    }

    print("=" * 50)
    print("Pretraga rezervacija: ")

    while True:

        print("=" * 50)
        print("Odabir: ")
        print("1. Pretraga po statusu rezervacije. ")
        print("2. Pretraga po adresi. ")
        print("3. Pretraga po korisničkom imenu domaćina. ")
        print("x. Završetak pretrage. ")
        unos = input("<< ")
        if unos in pretraga_admin_rezervacije_dict:

            pretraga_admin_rezervacije_dict[unos]()
            if unos == 'x':
                return
        else:
            print("Odabrali ste nepostojeću opciju")


def update_rez():

    load("rezervacije.txt")

    rez = ""
    for i in rezervacije.values():
        pocetni_datum = i["Pocetni_datum"]
        pocetni_datum = datetime.strptime(pocetni_datum, "%d.%m.%Y.")
        nocenja = int(i["Broj_nocenja"])
        krajnji_datum = pocetni_datum + timedelta(nocenja)
        if i["Status"] == "Prihvaćena" and krajnji_datum < datetime.today():
            i["Status"] = "Završena"
        if i["Status"] == "Kreirana" and pocetni_datum < datetime.today():
            i["Status"] = "Odbijena"
        temp = i["SifraR"] + "|" + i["SifraA"] + "|" + i["Pocetni_datum"] + "|" + i["Broj_nocenja"] + "|" + \
               i["Ukupna_cena"] + "|" + i["Gost"] + "|" + i["Status"] + '\n'
        rez += temp

    with open("rezervacije.txt", "w", encoding="utf-8") as file:
        file.write(rez)


# potvrdjen_dan()
# odabir_apartmana()
# pregled_i_odabir(10987)
# dodaj_ostale_goste(97832)
# rezervisanje_apartmana()
# print(unpack_niz(['dasdsd',['S', 'p'], ['s', '2']]))
# load("rezervacije.txt")
# print(rezervacije)
# stari_datum('881')
# pretraga_admin_rezervacije()
# korisnici.registruj("Gost")
rezervacije = {}
stari_datumi = {}
# apartmani.load("apartmani.txt")
# print(type(apartmani.apartmani['97832']["cena"]))

