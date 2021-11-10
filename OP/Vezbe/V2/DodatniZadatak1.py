# Program generiše nasumičan broj između 1 i 9, a zatim traži od korisnika da pogodi. 
# Program treba da obavesti da li je korisnički pogodak bio veći, manji ili jednak generisanom (odnosno tačan). 
# Potrebno je obavestiti korisnika u slučaju da je njegov predlog izašao iz mogućeg opsega.

from random import randint

pogodak = randint(1,9)

unos = eval(input("Unesite vas pokusaj [broj od 1 do 9 ukljucujuci njih]: "))

if unos == pogodak:
    print("Svaka cast, pogodili ste")

elif unos > 9 or unos < 1:
    print("Izasli ste iz opsega")

elif unos > pogodak:
    print("Uneli ste veci broj")
    
else:
    print("Uneli ste manji broj")

print("Resenje je ", pogodak)
