# Napiši program koji formira akronim za zadatu frazu. 
# Akronim se sastoji od kapitalizovanih prvih slova reči u frazi. 
# Na primer RAM je akronim za frazu „random access memory“. 

def main():

    resenje = ""

    string = input("Unesite frazu: ")

    for i in string.split(" "):

        resenje += i[0].capitalize()

    print(resenje)

if __name__ == "__main__":

    main()


    