from tabulate import tabulate
import re

def load(file_name="korisnici.txt"):

    with open(file_name, "r", encoding = "utf-8") as file:
        lines = file.readlines() 
        global korisnici
        korisnici = {}
        for line in lines:
            user_data = line.replace("\n", "").split("|")
            user_dict = {
                    "username":  user_data[0],
                    "password": user_data[1],
                    "name": user_data[2],
                    "surname": user_data[3],
                    "gender": user_data[4],
                    "phone_number": user_data[5],
                    "email_address": user_data[6],
                    "role": user_data[7],
                    "blocked": user_data[8]
            }
            korisnici[user_dict["username"]] = user_dict


def login():

    load("korisnici.txt")
    print("=" * 50)
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    print("=" * 50)
    if username in korisnici:
        user = korisnici[username]
        if password == user["password"]:
            if user["blocked"] == "da":
                print("Dati korisnik je blokiran i nije moguće izvršiti prijavu. ")
                return 0, 0
            print("Uspesna prijava! ")
            return korisnici[username]["role"], username
    print("Neuspesna prijava. ")
    return 0,0


def registruj(status):

    load("korisnici.txt")
    while True:
        korisnicko_ime = input("Unesite Vase korisnicko ime: ")
        if validate_username(korisnicko_ime) and korisnicko_ime not in korisnici.keys():
            break
        if korisnicko_ime in korisnici.keys():
            print("Ovo korisnicko ime je vec zauzeto, unesite ponovo")

    while True:
        lozinka = input("Unesite lozinku (najviše 7 karaktera): ")
        if len(lozinka) > 0 and len(lozinka) < 8:
            break
        else:
            print("Niste uneli korektno, ponovite unos")

    while True:
        a = 0
        telefon = input("Unesite telefon: ")
        for i in telefon:
            if i not in br_u_str():
                a = 1
                break
        if telefon[0] == '0' and (len(telefon) == 9 or len(telefon) == 10) and a == 0:
            break
        print("Niste uneli korektno, ponovite unos")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    while True:
        email = input("Unesite email: ")
        if (re.fullmatch(regex, email)):
            break
        print("Niste uneli korektno, ponovite unos")

    while True:
        ime = input("Unesite vase ime: ")
        if provera_str_broj(ime):
            break

    while True:
        prezime = input("Unesite vase prezime: ")
        if provera_str_broj(prezime):
            break

    while True:
        pol = input("Unesite slovo radi odabira pola (m za muski, z za zenski): ")
        if pol.lower() == 'm' or pol.lower() == 'z':
            break
        print("Niste uneli korektno, ponovite unos")

    if pol == 'm' or 'M':
        # print(f"{korisnicko_ime}|{lozinka}|{ime}|{prezime}|muski|{telefon}|{email}|Gost")
        rez = korisnicko_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + "muski" + "|" + telefon + "|" + \
              email + "|" + status + "|" + "ne" + '\n'
        # print(rez)
    if pol == 'z' or 'Z':
        # print(f"{korisnicko_ime}|{lozinka}|{ime}|{prezime}|zenski|{telefon}|{email}|Gost")
        rez = korisnicko_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + "zenski" + "|" + telefon + "|" + \
              email + "|" + status + "|" + "ne" + '\n'
        # print(rez)

    with open("korisnici.txt", "a", encoding="utf-8") as file:
        file.write(rez)


def validate_username(username):

    if len(username) < 1:
        print("Premalo")
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[A-Za-z0-9._]*$', username):
        print("Korisnicko ime moze da sadrzi samo slova, brojeve, tacke ili donje crte")
        return False
    # Usernames can't begin with a number
    if username[0] in br_u_str():
        print("Korisnicko ime ne sme poceti sa brojem")
        return False
    return True


def passwordin(password):

    global korisnici
    a = 0
    for i in korisnici.values():
        if password == i["password"]:
            a += 1
    if a == 0:
        return True
    print("Zauzeta lozinka. ")
    return False


def br_u_str():

    a = list(range(10))
    for i, j in enumerate(a):
        a[i] = str(j)
    return a


def provera_str_broj(unos):

    greska = 0
    try:
        unos = eval(unos)
        return False
    except NameError:
        for i in unos:
            if i in br_u_str():
                greska += 1
        if not greska and len(unos) > 2:
            return True
        print("Nepravilan unos.")
        return False
    except SyntaxError:
        print("Nepravilan unos.")
        return False


def unpack(user_name):

    load("korisnici.txt")
    username = korisnici[user_name]["username"]
    password = korisnici[user_name]["password"]
    name = korisnici[user_name]["name"]
    surname = korisnici[user_name]["surname"]
    gender = korisnici[user_name]["gender"]
    phone_number = korisnici[user_name]["phone_number"]
    email_address = korisnici[user_name]["email_address"]
    role = korisnici[user_name]["role"]
    rez = username + '-' + password + '-' + name + '-' + surname + '-' + gender + '-' + phone_number + '-' + \
          email_address + '-' + role
    return rez


def ispis_korisnika(tabele):

    load("korisnici.txt")
    header = ['Korisnično ime', 'Lozinka', 'Ime', 'Prezime', 'Pol', 'Kontakt_telefon', 'Email', 'Uloga', 'Blokiran']
    print(tabulate(tabele, header, tablefmt="simple"))


def svi_sem_admina(uslov):

    load("korisnici.txt")
    rez = ""
    tabele = []
    for i in korisnici.values():
        if i['role'] != "Administrator" and i["blocked"] == uslov:
            # temp = ""
            # temp = i["username"] + "|" + i["password"] + "|" + i["name"] + "|" + i["surname"] + "|" + i["gender"] + \
            #        "|" + i["phone_number"] + "|" + i["email_address"] + "|" + i["role"] + "|" + i["blocked"] + '\n'
            tabele.append([i["username"], i["password"], i["name"], i["surname"], i["gender"], i["phone_number"],
                           i["email_address"], i["role"], i["blocked"]])
    ispis_korisnika(tabele)


def blokiraj_korisnika():

    load("korisnici.txt")
    print("=" *50)
    print("Prikaz svih korisnika koje je moguće blokirati. ")
    print("=" * 50)
    svi_sem_admina("ne")
    while True:
        print("=" * 50)
        print("Unosite korisničko ime korisnika kojeg želite da blokirate. ")
        unos = input("<< ")
        try:
            unos = eval(unos)
        except NameError:
            if unos in korisnici and korisnici[unos]["role"] != "Administrator" and korisnici[unos]["blocked"] == "ne":
                break
            else:
                print("Nepostojeći korisnik. ")
        except SyntaxError:
            print("Nepravilan unos.")
    rez = ""
    for i in korisnici.values():
        if i['username'] == unos:
            temp = i["username"] + "|" + i["password"] + "|" + i["name"] + "|" + i["surname"] + "|" + i["gender"] + \
                   "|" + i["phone_number"] + "|" + i["email_address"] + "|" + i["role"] + "|" + "da" + '\n'
        else:
            temp = i["username"] + "|" + i["password"] + "|" + i["name"] + "|" + i["surname"] + "|" + i["gender"] + \
                   "|" + i["phone_number"] + "|" + i["email_address"] + "|" + i["role"] + "|" + i["blocked"] + '\n'
        rez += temp
    with open("korisnici.txt", "w", encoding="utf-8") as file:
        file.write(rez)


def odblokiraj_korisnika():

    load("korisnici.txt")
    print("=" * 50)
    print("Prikaz svih korisnika koje je moguće odblokirati. ")
    print("=" * 50)
    svi_sem_admina("da")
    while True:
        print("=" * 50)
        print("Unosite korisničko ime korisnika kojeg želite da odblokirate. ")
        unos = input("<< ")
        try:
            unos = eval(unos)
        except NameError:
            if unos in korisnici and korisnici[unos]["role"] != "Administrator" and korisnici[unos]["blocked"] == "da":
                break
            else:
                print("Nepostojeći korisnik. ")
        except SyntaxError:
            print("Nepravilan unos.")
    rez = ""
    for i in korisnici.values():
        if i['username'] == unos:
            temp = i["username"] + "|" + i["password"] + "|" + i["name"] + "|" + i["surname"] + "|" + i["gender"] + \
                   "|" + i["phone_number"] + "|" + i["email_address"] + "|" + i["role"] + "|" + "ne" + '\n'
        else:
            temp = i["username"] + "|" + i["password"] + "|" + i["name"] + "|" + i["surname"] + "|" + i["gender"] + \
                   "|" + i["phone_number"] + "|" + i["email_address"] + "|" + i["role"] + "|" + i["blocked"] + '\n'
        rez += temp
    with open("korisnici.txt", "w", encoding="utf-8") as file:
        file.write(rez)


# login()
korisnici = {}
# print(unpack('markos'))
# load()
# login()
# registruj()
# unpack('markos')
# print(unpack('markos'))