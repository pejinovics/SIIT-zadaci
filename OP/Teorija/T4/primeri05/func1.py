# funkcija se moze proslediti kao parametar

def greeter():
    print("Hello")

def repeater(func, times):
    for i in range(times):
        func()

repeater(greeter, 3)

