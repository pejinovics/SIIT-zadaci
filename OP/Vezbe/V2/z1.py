# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte

print("Pozdrav korisnice! Ovaj program sluzi da temperaturu koju uneses u Celzijusima konvertuje u temperaturu u Farenhajtima")
celsius = eval(input("Unesite temperaturu u C >> "))
fahrenheit = 9/5 * celsius + 32
print("Temperatura je", fahrenheit, "stepeni Farenhajta.")