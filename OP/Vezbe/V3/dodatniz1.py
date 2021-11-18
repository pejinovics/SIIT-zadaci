# Program trazi sve delioce nekog broja

def main():

    brojac = 1
    unos = eval(input("Unesite neki broj: "))

    while brojac <= unos:

        if unos % brojac == 0:
            print(brojac)
        
        brojac += 1

if __name__ == "__main__":
    main()
