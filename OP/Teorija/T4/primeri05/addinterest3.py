# addinterest3.py

def addInterest(balances, rate):
    balances[0] = [1, 2, 3, 4]
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)

test()
