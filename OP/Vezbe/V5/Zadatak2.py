# Program racuna sumu minimum maximum i srednju vrednost niza preko fja

def max(niz):
    najveci = niz[0]

    for i in niz:
        if i > najveci:
            najveci = i

    return najveci

def min(niz):
    najmanji = niz[0]

    for i in niz:
        if i < najmanji:
            najmanji = i
    
    return najmanji

def suma(niz):
    zbir = 0

    for i in niz:
        zbir += i

    return zbir

def srednja(niz):
    zbir = 0

    for i in niz:
        zbir += i

    prosek = zbir / len(niz)
    return prosek

niz = [1,2,3,4,5]

def ispis():

    print("Karakteristike niza: ", niz)
    print("Najveci el: ",max(niz))
    print("Najmanji el: ",min(niz))
    print("Suma el: ", suma(niz))
    print("Prosek niza: ", srednja(niz))

if __name__ == "__main__":
    ispis()
