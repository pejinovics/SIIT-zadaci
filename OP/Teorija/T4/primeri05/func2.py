# funkcija moze da se definise unutar funkcije

def print_integers(values):
    def is_integer(value):
        if type(value) is int:
            return True
        else:
            return False

    for v in values:
        if is_integer(v):
            print(v)


print_integers([1,2,3,"4","tekst", 3.14])
