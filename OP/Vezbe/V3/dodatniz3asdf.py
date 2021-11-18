# Kamen makaze list sa kompjuterom

from random import randint

def main():

    niz = ['kamen', 'makaze', 'list']
    noviunos = ''

    while noviunos != 'Ne':

        kompjuter = randint(1,3)

        while True:

            unos = eval(input("Unesite 1 za kamen, 2 za makaze ili 3 za list: ")) 
            if unos == 1 or unos == 2 or unos == 3:
                break
            print("Niste dobar broj uneli, ponovite unos") 

        if niz[unos - 1] == niz[kompjuter - 1]:
            print("Svaka cast, pobedili ste")
        
        print(f"Vas odabir je bio {niz[unos - 1]}, a kompjuterov {niz[kompjuter - 1]}")

        noviunos = (input("Jos? Ne za izlaz enter za nastavak: "))

if __name__ == "__main__":
    main()

         
