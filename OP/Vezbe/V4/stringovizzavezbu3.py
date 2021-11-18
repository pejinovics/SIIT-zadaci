# Iz zadatog stringa izdvojiti i ispisati:  a.	Sve cifre   b.	Sva mala slova

def main():

    unos = input("Unesite neki string: ")
    cifre = ""
    mala_slova = ""

    for i in unos:
        if ord(i) > 47 and ord(i) < 58:
            cifre += i
        if ord(i) > 96 and ord(i) < 123:
            mala_slova += i

    print(f"Cifre: {cifre}")
    print(f"Mala slova: {mala_slova}")

if __name__ == "__main__":
    main()
