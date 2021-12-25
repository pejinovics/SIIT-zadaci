# Kvadratna j-na 

from math import sqrt

def kvadratna_jna(a,b,c):

    if (b**2 - 4*a*c) < 0:
        return "Brojevi ne odgovaraju"
    diskriminanta = sqrt(b**2 - 4*a*c)

    koren1 = (-b - diskriminanta) / 2 * a
    koren2 = (-b + diskriminanta) / 2 * a

    return koren1, koren2

if __name__ == "__main__":
    print("Rez:",kvadratna_jna(1,10,6))