# futval_graph2.py

from graphics import *

def main():
    print("Iscrtava rast 10-godisnje investicije.")

    # Ucitaj osnovu i kamatu
    principal = eval(input("Unesite osnovicu: "))
    apr = eval(input("Unesite kamatu: "))

    # Kreiraj prozor sa oznakama na levoj strani
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Nacrtaj stubac za inicijalno ulaganje
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Nacrtaj stubac za svaku narednu godinu
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Pritisnite <Enter> za kraj.")
    win.close()

main()
