# Dodavanje korisnika i ispis kao niz

def upisiufajl(korisnik,sifra,fajl, znak):

    fajl1 = open(fajl, "a")

    fajl1.write(korisnik + '|' + sifra + '\n')

    fajl1.close()

    fajl1 = open(fajl, "r")
    n = []
    lista = []

    for i in fajl1.readlines():

        n = i.split(znak)
        n[-1] = n[-1][:-1]
        lista.append(n)

    fajl1.close()
    return lista

if __name__ == "__main__":
    print(upisiufajl("marko","markovic","../V4/korisnici1.txt", "|"))