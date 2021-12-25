# Sadrzaj iz fajla stvalja u niz

def citanjeizfajla(fajl, znak):

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
    print(citanjeizfajla("../V4/korisnici1.txt", "|"))