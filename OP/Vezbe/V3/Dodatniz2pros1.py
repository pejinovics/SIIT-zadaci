# Napiši program koji ispisuje sve brojeve između 1200 i 2500 koji su deljivi sa 7 i 11 koristeci continue.

def main():

    print("Brojevi deljivi sa 7 ii 11")

    for i in range(1200,2500):

        if i % 7 == 0 and i % 11 == 0:
            print(i)
        else:
            continue
        

if __name__ == "__main__":
    main()