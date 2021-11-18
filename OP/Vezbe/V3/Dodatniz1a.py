# Prikaz znaka 
#        *
#        * *
#        * * *
#        * * * *
#        * * * * *
#        * * * *
#        * * *
#        * *
#        *

n = 1
s = '*'
while n < 6:
    print(n * s)
    n += 1

n -= 1

while n > 0:
    print(n * s) 
    n -= 1   