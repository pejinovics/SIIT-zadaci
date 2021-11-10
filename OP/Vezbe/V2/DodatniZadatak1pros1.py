# Program generiše nasumičan broj između 1 i 9, a zatim traži od korisnika da pogodi. 
# Program treba da obavesti da li je korisnički pogodak bio veći, manji ili jednak generisanom (odnosno tačan). 
# Potrebno je obavestiti korisnika u slučaju da je njegov predlog izašao iz mogućeg opsega.

# Proširenje 1: Korisnik na početku zadaje opseg brojeva za pogađanje, donju i gornju granicu.

from random import randint

donja, gornja = eval(input("Unesite donju i gornju granicu za opseg brojeva [razdvojte brojeve zarezom]: "))
pogodak = randint(donja,gornja)

unos = eval(input("Unesite vas pokusaj [broj od donje do gornje granice ukljucujuci njih]: "))

if unos == pogodak:
    print("Svaka cast, pogodili ste")

elif unos > gornja or unos < donja:
    print("Izasli ste iz opsega")

elif unos > pogodak:
    print("Uneli ste veci broj")
    
else:
    print("Uneli ste manji broj")

print("Resenje je ", pogodak)