# Napiši program koji od korisnika traži da unese dva stringa i formira i ispisuje novi string koji se 
# sastoji od dva puta ponovljena prva tri karaktera iz prvog stringa i poslednja tri karaktera prethodnog
# stringa. 

def main():

    string1 = input("Unesite string: ")
    string2 = input("Unesite string: ")

    print(2 * string1[:3] + string2[-3:])

if __name__ == "__main__":

    main()
