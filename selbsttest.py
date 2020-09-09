def isPrim(i):
    if i < 2:
        return 0
    else:
        for num in range(i+1):
            if 1 < num != i and i % num == 0:
                return 0
    return 1



# aufgabe1
n = int(input("Primzahlberrechnung bis zur Zahl :"))

for num in range(n + 1):
    if isPrim(num) == 1:
        print(num)
