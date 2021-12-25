# Napiši program koji učitava iz tekstulanog fajla korisnička imena i ispisuje ih

def main():

    fajl = open("../V4/korisnici1.txt", "r")

    for i in fajl.readlines():
        
        print("korisnicko ime: ", i.split('|')[0])
        print("lozinka: ", i.split('|')[1])

    fajl.close()

if __name__ == "__main__":

    main()  