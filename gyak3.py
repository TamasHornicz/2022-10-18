n = int(input("Szám vége: "))

osszeg = 0
for n in range(1, n+1, 1):
    negyzet= n**2
    osszeg = osszeg+negyzet

atlag = osszeg/n
print(atlag)
