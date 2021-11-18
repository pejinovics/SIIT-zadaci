# futval_graph3.py
from graphics import *

def drawBar(window, year, height):
    # Nacrtaj stubac za datu godinu i datu visinu
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)
    
def main():
    print("Iscrtava rast 10-godisnje investicije.")

    # Unesi osnovicu i kamatu
    principal = eval(input("Unesite osnovicu: "))
    apr = eval(input("Unesite kamatu: "))

    # Kreiraj prozor i oznake na levoj strani
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    drawBar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Pritisnite <Enter> za kraj.")
    win.close()
main()
