n = int(input("Entrez un Nombre Entier : "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i
        print("La Somme des pairs 1 à ", n, "est : ", s)