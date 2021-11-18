# Mozemo funkciju da obmotamo drugom funkcijom

def print_call(fn):
    def fn_wrap(*args, **kwargs): # funkcija prima bilo kakve argumente
        print("Pozivam %s" % (fn.__name__))
        return fn(*args, **kwargs) # prosledi bilo kakve argumente funkciji fn
    
    return fn_wrap

suma = print_call(sum)  # sum je ugradjena funkcija
print suma([1, 2, 3, 4])