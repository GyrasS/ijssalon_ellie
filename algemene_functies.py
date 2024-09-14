def mijn_functie_1(a):
    uitvoer = a * a
    return uitvoer
print("1. ", mijn_functie_1(2))
    
print("------------------------")

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
print("2. ", mijn_functie_2(12,3))
