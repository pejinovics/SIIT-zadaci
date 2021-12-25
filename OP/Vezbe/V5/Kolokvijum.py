# Zadatak kakav bude na kol

def stanjenaracunu():

    fajl = open("../Vezbe/V5/banka.txt", "r")
    
    n = []
    lista = []

    for i in fajl.readlines():

        n = i.split()
        n[-1] = n[-1][:-1]
        lista.append(n)
    os = 0
    for i in range(len(lista)):
        for j in lista:

            if lista[i][0] == lista[i + 1][0]:
                print("Isti")

    
    fajl.close()
    

if __name__ == "__main__":
    print(stanjenaracunu())