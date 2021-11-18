# Korisnik zadaje proizvoljne granice, a zatim zamišlja broj u tom opsegu. 
# Proverava se da li su zadate granice korektne, odnosno da li je donja manja od gornje.
# Računar pogađa broj na sličan način kao u prethodnom zadatku.


donja, gornja = eval(input("Unesite donju i gornju granicu za opseg brojeva [razdvojte brojeve zarezom]: "))

if donja <= gornja:

    brpokusaja = 0

    while True:

        temp = (donja + gornja) // 2
        print(f"Da li je vas pokusaj",temp, end=" ")
        unos = input("[unesite = ako jeste, > ako je rez veci i < ako je manji]: ")
        brpokusaja += 1

        if unos == '=':
            print("Svaka cast, pogodili ste")
            break
        elif unos == '>':
            donja = temp + 1
        elif unos == '<':
            gornja = temp - 1
        else:
            print("Niste uneli dobar znak")
    
    print("Resenje je ", temp)
    print(f"Pokusali ste {brpokusaja} puta da pogodite")

else:
    
    print("Niste dobro uneli granice")


