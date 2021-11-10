#Program konvertuje vrednosti iz Celzijusa u Farenhajte za vrednosti od 0 do 100 u skokovima od 10

for celsius in range(0,101,10):
    fahrenheit = 9/5 * celsius + 32 
    print(f"Za {celsius} stepeni Celzijusa temperatura je", fahrenheit, "stepeni Farenhajta.")