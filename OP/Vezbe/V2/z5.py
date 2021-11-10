#Ovaj program treba da konvertuje temperaturu iz Farenhajta u Celzijuse

farenheit = eval(input("Unesite vrednost u Farenhajtima: "))
celsius = (farenheit - 32) * 5/9

print(f"Za {farenheit} stepeni Farenhajta temperatura je ", celsius, " stepeni Celzijusa")
