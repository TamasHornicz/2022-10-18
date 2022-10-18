
a = int(input("Írja be az idnulópontot: "))
b = int(input("Írja be a végét: "))
c = int(input("Írja be a lépés nagyságát: "))


for i in range(1, c+1):
    abc = a + (i-1)*b
    print(abc)