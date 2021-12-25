# Implementiranje dve igre iz popularnog kviza "Slagalica".
# Ko zna zna
# Asocijacije

from random import randint

def ko_zna_zna(fajl):

    fajl1 = open(fajl, "r", encoding = "utf-8")

    print("\n\nDOBRODOSLI U IGRU KO ZNA ZNA!")
    print("\nPrateci uputstva programa probajte da tacno odgovorite na sto veci broj odgovora!")
    print("Za svaki tacan odgovor dobijate 4 boda, za netacan -1, a za preskocen Vam se broj bodova ne menja")
    brpit = 1
    brodg = 1
    poeni_kzz = 0

    for i in fajl1.readlines():

        pitanje = i.split("|")[0]
        odgovori = i.split("|")[1:-1]
        resenje = i.split("|")[-1]

        brodg = 1
        unos = ""

        print(f"\n{brpit}. {pitanje} \n")
        brpit += 1

        for odg in odgovori:

            print(f"    {brodg}) {odg}")
            brodg += 1

        while unos not in ['1','2','3','4','5']:

            unos = input("\nKoji je tacan odgovor?:\t1, 2, 3, 4 za odgovor, 5 za ne znam: ")

        if eval(unos) == eval(resenje):
            print("Tacno!")
            poeni_kzz += 4

        elif unos == '5':
            print("Preskocili ste, ne gubite bodove")
            poeni_kzz += 0

        else:
            print(f"Netacno!\nTacan odgovor je: {resenje}")
            poeni_kzz -= 1
        
    print(f"\nBroj bodova u ovoj igri: {poeni_kzz} \n")

def poziv_ko_zna_zna():

    if randint(1,5) == 1:
        ko_zna_zna("../Vezbe/Domaci zadatak/koznazna1.txt")
    elif randint(1,5) == 2:
        ko_zna_zna("../Vezbe/Domaci zadatak/koznazna2.txt")
    elif randint(1,5) == 3:
        ko_zna_zna("../Vezbe/Domaci zadatak/koznazna3.txt")
    elif randint(1,5) == 4:
        ko_zna_zna("../Vezbe/Domaci zadatak/koznazna4.txt")
    else:
        ko_zna_zna("../Vezbe/Domaci zadatak/koznazna5.txt")

def ispis(lista,resenje):   # f-ja za ispis tabele asocijacija

    print("\n")
    for n in range(4):
        print(f"{lista[0][n].ljust(13,' ')}\t\t\t{lista[1][n].rjust(13,' ')}")
 
    print(f"\n{resenje[0].ljust(13,' ')}\t\t\t{resenje[1].rjust(13,' ')}")
    print(f"{resenje[4].center(45)}")
    print(f"{resenje[2].ljust(13,' ')}\t\t\t{resenje[3].rjust(13,' ')}\n")
 
    for n in range(4):
        print(f"{lista[2][n].ljust(13,' ')}\t\t\t{lista[3][n].rjust(13,' ')}")


def unos(fajl,fajlr,nizresenja,nizprvi,niz): # f-ja za otvaranje sadrzaja iz fajla

    fajl2 = open(fajl, "r", encoding = "utf-8") 
    fajlresenja = open(fajlr, "r", encoding = "utf-8") 

    for i in fajlresenja.readlines():
        nizresenja.append(i)
        nizresenja[-1] = nizresenja[-1][:-1]

    nizresenja.pop() 
    br = 0

    for i in fajl2.readlines():
        a = i.split("|")
        
        for n in a: 
            niz[br].append(n)

        niz[br][-1] = niz[br][-1][:-1]
        br += 1
        print("\n")

    niz.pop()   

def konacno(niz):

    konacno_resenje = 0
    for i in niz:
        if i <= 0:
            i += 6
            konacno_resenje += i
        else:
            konacno_resenje += i
    return konacno_resenje

def nekonacno(niz):

    konacno_resenje = 0
    for i in niz:
        if i <= 0:
            konacno_resenje += 0
        else:
            konacno_resenje += i
    return konacno_resenje
             

def asocijacije(fajl, fajlresenje): 

    print("\nDOBRODOSLI U IGRU ASOCIJACIJE!\n")
    print("Pratite uputsva kroz program i probajte da ostvarite sto bolji rezultat\n")
    nizresenja = []     #niz u kome cuvamo sva resenja iz txt datoteke
    nizprvi =[['a1','a2','a3','a4'], ['b1','b2','b3','b4'], ['c1','c2','c3','c4'], ['d1','d2','d3','d4']]   #akumulator niz
    niz = [[],[],[],[],[]]      #niz u kome cuvamo sva polja iz txt datoteke
    resenjeniz = ['a','b','c','d','KONACNO']    #akumulator niz
    unetiel = [] # niz koji sadrzi unete kombinacije kolona/polje
    kolpolj = [] # kombinacija kolona/polje

    unos(fajl,fajlresenje, nizresenja,nizprvi,niz)
    
    dalje = ""
    bodovi = [0,0,0,0,0]
    brojac = 0
    kraj = 0
    kolone = ['1','2','3','4'] # sve kolone
    odabir = ['0','1','2','3','4','5'] # odabir radnji
    pogodjeni = []

    # Svaka kolona ukljucujuci i konacno resenje vredi 6 bodova, dok sa svakim otvaranjem polja gubimo bod

    for i in range(20):     # s obzirom da radimo sa 16 polja dajemo mogucnost od 20 pokusaja/otvaranja polja

        korisnik = ""
        korisnik2 = ""
        proba = ""
        pogodak = ""
        tacno = False
        
        ispis(nizprvi,resenjeniz)

        while True:

            if len(unetiel) == 16:  # ako otvorimo sva polja vise ne dajemo mogucnost otvaranja polja (br polja je 16)
                break
            korisnik = ""
            korisnik2 = ""
            kolpolj = []   # sa svakim ponovnim unosom polja praznimo ovaj niz
            while korisnik not in kolone:
                korisnik = input("\nUnesite kolonu koju zelite da otvorite (1 za a, 2 za b, 3 za c, 4 za d): ")
                kolpolj = []
                kolpolj.append(korisnik)
                if korisnik in pogodjeni:
                    print("\nVec ste pogodili ovu kolonu\n")

            while korisnik2 not in ['1','2','3','4']:
                korisnik2 = input("Unesite polje u koloni(1,2,3,4): ")
                print("\n")
                bodovi[eval(korisnik) - 1] -= 1
                kolpolj.append(korisnik2)

            if kolpolj in unetiel:  # provera da li je dato polje vec uneto, ako jeste idemo nazad na ulaz
                print("\nVec ste uneli to polje\n")
                
            else:
                unetiel.append(kolpolj)
                nizprvi[eval(korisnik) - 1][eval(korisnik2) - 1] = niz[eval(korisnik) - 1][eval(korisnik2) - 1]
                break

        ispis(nizprvi,resenjeniz)

        while proba not in odabir:
            proba = input("\nPokusajte:\n0)nastavak unosa\n1)kolona a\n2)kolona b\n3)kolona c\n4)kolona d\n5)konacno\n\n")
            if proba == '0':
                break
            if proba in pogodjeni:
                print("Vec ste pogodili ovu kolonu\n")
        
        if proba != '0':    
            pogodak = input("\nVas pokusaj: ")
            

        for i in range(4):
            if nizresenja[i] == pogodak.upper():    # resenje je caps lock pa ovim dajemo mogucnost unosa i malih slova
                print("Tacno!")
                resenjeniz[i] = nizresenja[i]
                bodovi[i] += 6
                brojac += 1
                kolone.remove(str(i + 1))
                odabir.remove(str(i + 1))
                pogodjeni.append(str(i + 1))
                tacno = True

        if nizresenja[4] == pogodak.upper():
            resenjeniz[4] = nizresenja[4]

        if tacno == False and proba != '0':        
            print("Netacno!")

        if nizresenja[4] == resenjeniz[4]:
            ispis(niz,nizresenja)
            print("\nSVAKA CAST, POBEDILII STE")
            print(f"Broj bodova: {konacno(bodovi)}")
            kraj += 1
            break

        dalje = input("Nastavak unosa? (Ne za izlaz, enter za nastavak): ")

        if dalje == "Ne":
            print("Steta sto ste odustali, vise srece sledeci put.\nResenje je: \n")
            ispis(niz, nizresenja)
            kraj += 1

            print(f"\nBroj bodova: {nekonacno(bodovi)}")
            break

    if kraj == 0:
        ispis(niz, nizresenja)
        print("\nKraj igre")
        print(f"\nBroj bodova: {nekonacno(bodovi)}")
         

def poziv_asocijacije():

    if randint(1,2) == 1:
        asocijacije("../Vezbe/Domaci zadatak/asocijacije1.txt", "../Vezbe/Domaci zadatak/asocijacije1resenja.txt")
    else:
        asocijacije("../Vezbe/Domaci zadatak/asocijacije2.txt", "../Vezbe/Domaci zadatak/asocijacije2resenja.txt")
    
def main():

    biraj = ''
    while biraj != '0':
        biraj = input("\nMENI:\n0.Izalaz\n1.Ko zna zna\n2.Asocijacije\n\n")

        if biraj == '1':
            poziv_ko_zna_zna()
        elif biraj == '2':
            poziv_asocijacije()
        elif biraj == '0':
            pass
        else:
            print("Unos nije ispravan\n")

    print("Kraj programa\n")

if __name__ == "__main__":

    main()


        
