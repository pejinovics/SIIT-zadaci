# Primer obmotane funkcije -- zadrzavamo isto ime funkcije!

def print_call(fn):
    def fn_wrap(*args, **kwargs):
        print("Pozivam %s" % fn.__name__)
        retval = fn(*args, **kwargs) 
        print("Zavrsen poziv")
        return retval
    
    return fn_wrap # rezultat funkcije je funkcija!

def greeter(name):
    return("Hello, %s" % name)

greeter = print_call(greeter)
print greeter("Branko")
