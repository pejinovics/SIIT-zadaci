# Program racuna nagib prave koja prolazi kroz date tacke koje sami unosimo

tacka1x, tacka1y = eval(input("Unesite x i y koordinatu [, za odvajanje]: "))

tacka2x, tacka2y = eval(input("Unesite x i y koordinatu [, za odvajanje]: "))

resenje = (tacka2y - tacka1y) / (tacka2x - tacka1x)

print(f"Razdaljina je {resenje}")