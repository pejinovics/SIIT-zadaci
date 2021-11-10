# Program generiše nasumičan broj između 1 i 9, a zatim traži od korisnika da pogodi. 
# Program treba da obavesti da li je korisnički pogodak bio veći, manji ili jednak generisanom (odnosno tačan). 
# Potrebno je obavestiti korisnika u slučaju da je njegov predlog izašao iz mogućeg opsega.

# Proširenje 1: Korisnik na početku zadaje opseg brojeva za pogađanje, donju i gornju granicu.

# Proširenje 2: Dozvoliti više uzastopnih pogađanja. 
# Kada korisnik umesto broja unese naredbu 'izlaz', izvršavanje bi trebalo da se prekine. 
# Takođe, izvršavanje se prekida kada korisnik pogodi traženi broj.

from random import randint


donja, gornja = eval(input("Unesite donju i gornju granicu za opseg brojeva [razdvojte brojeve zarezom]: "))

if donja <= gornja:

    pogodak = randint(donja,gornja)

    while True:

        unos = input("Unesite vas pokusaj [broj od donje do gornje granice ukljucujuci njih]: ")

        if unos != 'izlaz':

            x = eval(unos)

            if x == pogodak:
                print("Svaka cast, pogodili ste")
                break
            elif x > gornja or x < donja:
                print("Izasli ste iz opsega")
            elif x > pogodak:
                print("Uneli ste veci broj")
            else:
                print("Uneli ste manji broj")

        else:
            print("Izasli ste")
            break
    
    print("Resenje je ", pogodak)

else:
    
    print("Niste dobro uneli granice")


