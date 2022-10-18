import random


print("10-es szorzótábla gyakorló program!")
print()
db = int(input("Hány feladatot szeretnél csinálni? "))

jo = 0

for i in range(db):
    szam1 = random.randint(1,10)
    szam2 = random.randint(1,10)

    valasz = int(input(str(szam1)+"*"+str(szam2)+"="))

    if(szam1*szam2==valasz):
        print("Helyes")
        jo = jo+1
    else:
        print("Rossz megoldás",szam1*szam2, " lett volna")

sz = (jo/db)*100
print("Statisztikád: ",db,"/",jo,sz,"%")