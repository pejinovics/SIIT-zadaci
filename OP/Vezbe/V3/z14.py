# Program racuna duzinu merdevina na osnovu visine i sinusa ugla

from math import sin

visina = eval(input("Unesi visinu: "))
ugao = eval(input("Unesi ugao: "))

resenje = visina / sin(ugao)

print(f"Resenje je {resenje}")